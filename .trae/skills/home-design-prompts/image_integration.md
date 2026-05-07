# 图像生成功能集成说明

## 概述

本Skill已集成魔塔Qwen-Image-2512生图大模型，可以根据生成的提示词直接生成家居设计图像。

## 文件结构

```
家装提示词/
├── .env                          # API配置
├── image_generator.py            # 图像生成模块
├── generate_image.py             # 快速生图脚本
└── .trae/skills/home-design-prompts/
    ├── SKILL.md                  # Skill主文件
    └── image_integration.md      # 本说明文件
```

## 配置说明

### 1. 环境变量 (.env)

```env
MODELSCOPE_API_KEY=your_api_key_here
MODELSCOPE_BASE_URL=https://api-inference.modelscope.cn/
DEFAULT_IMAGE_MODEL=Qwen/Qwen-Image-2512
```

### 2. 安装依赖

```bash
pip install requests Pillow python-dotenv
```

## 使用方法

### 方法1：使用Python模块

```python
from image_generator import ImageGenerator

# 创建生成器
generator = ImageGenerator()

# 生成图像
result = generator.generate_image(
    prompt="Modern minimalist living room with beige sofa",
    output_path="output.jpg"
)

if result["success"]:
    print(f"图像已保存: {result['image_path']}")
```

### 方法2：从提示词文件生成

```python
from image_generator import ImageGenerator

generator = ImageGenerator()

# 从Markdown文件生成
result = generator.generate_from_prompt_file(
    prompt_file_path="JZ001_0506_现代简约_客厅设计/prompt.md",
    output_dir="JZ001_0506_现代简约_客厅设计"
)
```

### 方法3：使用命令行脚本

```bash
# 生成单个图像
python generate_image.py "Modern minimalist bedroom"

# 从文件生成
python generate_image.py --file JZ001_0506_现代简约_客厅设计/prompt.md
```

## 集成到Skill工作流

### 模式一：对话式引导生成（增强版）

1. 完成8个维度的对话收集
2. 生成专业提示词并保存为Markdown文件
3. **新增**：询问用户是否立即生成图像
4. 如用户确认，调用 `image_generator.generate_from_prompt_file()`
5. 显示生成结果和图像路径

### 模式二：提示词优化生成（增强版）

1. 接收用户具体需求
2. 优化生成专业提示词
3. 保存为Markdown文件
4. **新增**：自动或询问生成图像
5. 返回提示词和生成的图像

### 模式三：图像分析与提示词提取（增强版）

1. 分析用户上传的图像
2. 提取关键设计特征
3. 生成相似风格的提示词
4. **新增**：基于提取的风格生成变体图像
5. 提供原图分析和AI生成图对比

## API参数说明

### 生成参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| prompt | 图像生成提示词（英文） | 必填 |
| output_path | 输出图像路径 | generated_image.jpg |
| loras | LoRA模型配置 | None |
| wait_interval | 轮询间隔（秒） | 5 |
| max_wait_time | 最大等待时间（秒） | 300 |

### LoRA配置示例

```python
# 单个LoRA
loras = "lora-model-id"

# 多个LoRA（权重之和必须为1.0）
loras = {
    "lora-id-1": 0.6,
    "lora-id-2": 0.4
}
```

## 错误处理

### 常见错误

1. **API Key无效**
   - 检查.env文件中的API Key
   - 确认Key未过期

2. **生成超时**
   - 增加max_wait_time参数
   - 检查网络连接

3. **提示词过长**
   - 精简提示词内容
   - 保留核心描述

4. **生成失败**
   - 检查提示词是否包含敏感内容
   - 尝试修改提示词描述

## 最佳实践

### 提示词优化建议

1. **使用英文提示词**
   - 模型对英文理解更好
   - 生成效果更稳定

2. **结构化描述**
   ```
   [空间类型], [风格], [主体元素], [材质], [色彩], [光线], [视角], [质量描述]
   ```

3. **添加质量关键词**
   - professional interior photography
   - photorealistic rendering
   - interior design magazine quality

4. **控制提示词长度**
   - 建议200-500字符
   - 重点突出，避免冗余

### 图像保存建议

1. **按目录组织**
   ```
   JZ001_0506_现代简约_客厅设计/
   ├── prompt.md              # 提示词文件
   └── generated_image.jpg    # 生成的图像
   ```

2. **多版本管理**
   ```
   JZ001_0506_现代简约_客厅设计/
   ├── prompt.md
   ├── generated_v1.jpg       # 版本1
   ├── generated_v2.jpg       # 版本2
   └── generated_final.jpg    # 最终版
   ```

## 示例代码

### 批量生成示例

```python
from image_generator import ImageGenerator
import os

generator = ImageGenerator()

# 批量生成多个设计
prompts = [
    ("JZ001_0506_现代简约_客厅设计/prompt.md", "客厅设计1"),
    ("JZ002_0506_奶油侘寂风_客厅设计/prompt.md", "客厅设计2"),
    ("JZ003_0506_法式奶油风_客餐厅设计/prompt.md", "客餐厅设计"),
]

for prompt_file, name in prompts:
    print(f"\n生成: {name}")
    result = generator.generate_from_prompt_file(prompt_file)
    
    if result["success"]:
        print(f"✅ 成功: {result['image_path']}")
    else:
        print(f"❌ 失败: {result.get('error')}")
```

### 变体生成示例

```python
from image_generator import ImageGenerator

generator = ImageGenerator()

base_prompt = "Modern minimalist living room"

# 生成不同风格的变体
variations = [
    f"{base_prompt}, warm beige tones, cozy atmosphere",
    f"{base_prompt}, cool grey tones, sophisticated",
    f"{base_prompt}, Scandinavian style, natural light",
]

for i, prompt in enumerate(variations, 1):
    result = generator.generate_image(
        prompt=prompt,
        output_path=f"variation_{i}.jpg"
    )
```

## 注意事项

1. **API调用限制**
   - 注意API的调用频率限制
   - 合理安排生成任务

2. **图像版权**
   - 生成的图像仅供个人使用
   - 商用需遵守平台规定

3. **网络稳定性**
   - 确保网络连接稳定
   - 大图像下载可能需要较长时间

4. **存储空间**
   - 生成的图像占用存储空间
   - 定期清理不需要的图像

## 更新日志

### v1.0 (2026-05-06)
- 初始版本
- 集成Qwen-Image-2512模型
- 支持从提示词文件生成图像
- 支持批量生成和变体生成
