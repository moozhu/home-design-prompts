"""
魔塔Qwen-Image-2512生图API调用模块
用于根据提示词生成家居设计图像
"""

import os
import requests
import time
import json
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# 加载环境变量
load_dotenv()


class ImageGenerator:
    """
    图像生成器类
    封装了魔塔Qwen-Image-2512 API的调用
    """
    
    def __init__(self):
        """
        初始化图像生成器
        从.env文件加载API配置
        """
        self.base_url = os.getenv('MODELSCOPE_BASE_URL', 'https://api-inference.modelscope.cn/')
        self.api_key = os.getenv('MODELSCOPE_API_KEY')
        self.model = os.getenv('DEFAULT_IMAGE_MODEL', 'Qwen/Qwen-Image-2512')
        
        if not self.api_key:
            raise ValueError("未找到API Key，请在.env文件中设置MODELSCOPE_API_KEY")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
    
    def generate_image(
        self,
        prompt: str,
        output_path: str = "generated_image.jpg",
        loras: Optional[Dict[str, float]] = None,
        wait_interval: int = 5,
        max_wait_time: int = 300
    ) -> Dict[str, Any]:
        """
        根据提示词生成图像
        
        参数:
            prompt: 图像生成提示词
            output_path: 输出图像路径
            loras: 可选的LoRA配置，如 {"lora-id": 0.6}
            wait_interval: 轮询间隔（秒）
            max_wait_time: 最大等待时间（秒）
        
        返回:
            包含生成结果的字典
        """
        # 构建请求数据
        data = {
            "model": self.model,
            "prompt": prompt
        }
        
        # 添加LoRA配置（如果有）
        if loras:
            data["loras"] = loras
        
        print("[信息] 正在提交生图任务...")
        print(f"[信息] 提示词: {prompt[:100]}...")
        
        try:
            # 提交生图任务
            response = requests.post(
                f"{self.base_url}v1/images/generations",
                headers={**self.headers, "X-ModelScope-Async-Mode": "true"},
                data=json.dumps(data, ensure_ascii=False).encode('utf-8')
            )
            response.raise_for_status()
            task_id = response.json()["task_id"]
            print(f"[信息] 任务已提交，任务ID: {task_id}")
            
            # 轮询等待结果
            start_time = time.time()
            while True:
                # 检查是否超时
                if time.time() - start_time > max_wait_time:
                    return {
                        "success": False,
                        "error": "生成超时",
                        "task_id": task_id
                    }
                
                # 查询任务状态
                result = requests.get(
                    f"{self.base_url}v1/tasks/{task_id}",
                    headers={**self.headers, "X-ModelScope-Task-Type": "image_generation"},
                )
                result.raise_for_status()
                data = result.json()
                
                task_status = data.get("task_status")
                
                if task_status == "SUCCEED":
                    # 任务成功，下载图片
                    image_url = data["output_images"][0]
                    print("[信息] 图像生成成功，正在下载...")
                    
                    image = Image.open(BytesIO(requests.get(image_url).content))
                    image.save(output_path)
                    print(f"[信息] 图像已保存至: {output_path}")
                    
                    return {
                        "success": True,
                        "image_path": output_path,
                        "task_id": task_id,
                        "image_url": image_url
                    }
                    
                elif task_status == "FAILED":
                    error_msg = data.get("error_message", "未知错误")
                    print(f"[错误] 图像生成失败: {error_msg}")
                    return {
                        "success": False,
                        "error": error_msg,
                        "task_id": task_id
                    }
                
                # 等待后继续轮询
                print(f"[信息] 任务处理中... ({int(time.time() - start_time)}秒)")
                time.sleep(wait_interval)
                
        except requests.exceptions.RequestException as e:
            print(f"[错误] API请求错误: {e}")
            return {
                "success": False,
                "error": str(e)
            }
        except Exception as e:
            print(f"[错误] 发生错误: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def generate_from_prompt_file(
        self,
        prompt_file_path: str,
        output_dir: str = ".",
        use_english_prompt: bool = True
    ) -> Dict[str, Any]:
        """
        从提示词文件生成图像
        
        参数:
            prompt_file_path: 提示词文件路径（Markdown格式）
            output_dir: 输出目录
            use_english_prompt: 是否使用英文提示词（推荐）
        
        返回:
            包含生成结果的字典
        """
        import re
        
        # 读取提示词文件
        with open(prompt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取英文提示词
        if use_english_prompt:
            # 匹配英文提示词代码块
            match = re.search(r'### 英文提示词[\s\S]*?```\n([\s\S]*?)```', content)
            if match:
                prompt = match.group(1).strip()
                # 移除参数部分（--ar等）
                prompt = re.sub(r'\s*--[a-z]+\s+\S+', '', prompt)
            else:
                # 尝试匹配普通代码块
                match = re.search(r'```\n([\s\S]*?)```', content)
                if match:
                    prompt = match.group(1).strip()
                    prompt = re.sub(r'\s*--[a-z]+\s+\S+', '', prompt)
                else:
                    return {
                        "success": False,
                        "error": "未找到英文提示词"
                    }
        else:
            # 使用中文提示词
            match = re.search(r'### 中文参考[\s\S]*?\n([\s\S]*?)(?:\n---|\n## |\Z)', content)
            if match:
                prompt = match.group(1).strip()
            else:
                return {
                    "success": False,
                    "error": "未找到中文提示词"
                }
        
        # 生成输出文件名
        base_name = os.path.splitext(os.path.basename(prompt_file_path))[0]
        output_path = os.path.join(output_dir, "generated_image.jpg")
        
        print(f"[信息] 从文件加载提示词: {prompt_file_path}")
        return self.generate_image(prompt, output_path)


def main():
    """
    测试函数
    """
    # 创建生成器实例
    generator = ImageGenerator()
    
    # 测试生成图像
    prompt = "A modern minimalist living room with beige sofa and warm lighting"
    result = generator.generate_image(prompt, "test_image.jpg")
    
    if result["success"]:
        print(f"✅ 图像生成成功: {result['image_path']}")
    else:
        print(f"❌ 图像生成失败: {result.get('error', '未知错误')}")


if __name__ == "__main__":
    main()
