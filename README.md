# Home Design Prompts - 家居家装AI提示词生成器

**本项目免费开源，仅供学习！！怕有的小白不会用，这里说明一下。直接下载整个项目，然后用字节的TRAE软件打开这个文件夹，让它直接跑起来就行了。如果只是单纯要skill，直接下载".trae/skills/home-design-prompts"目录下的SKILL.md 文件就行**

一个专业的家居家装Midjourney/Image2提示词生成工具，支持对话式引导、提示词优化和图像生成功能。

## 功能特点

- **三种工作模式**
  - 对话式引导生成：通过8个维度收集需求
  - 提示词优化生成：直接优化已有描述
  - 图像分析与提取：分析参考图片生成提示词

- **AI图像生成**
  - 可接入AI生图大模型
  - 一键生成家居设计效果图

- **专业提示词库**
  - 空间类型关键词
  - 设计风格关键词
  - 材质、光线、视角等专业术语

## 快速开始

### 1. 安装依赖

```bash
pip install requests Pillow python-dotenv
```

### 2. 配置API Key

编辑 `.env` 文件，填入你的魔塔API Key：

```env
MODELSCOPE_API_KEY=your_api_key_here
MODELSCOPE_BASE_URL=https://api-inference.modelscope.cn/
DEFAULT_IMAGE_MODEL=Qwen/Qwen-Image-2512
```

> 获取API Key：[魔塔ModelScope](https://www.modelscope.cn/)

### 3. 使用方法

#### 方式一：对话式生成
```bash
# 运行后会通过对话收集需求
python generate_image.py
```

#### 方式二：直接输入提示词
```bash
python generate_image.py "现代简约客厅，米色沙发，暖色调"
```

#### 方式三：从文件生成
```bash
python generate_image.py --file JZ001_0506_现代简约_客厅设计/prompt.md
```

#### 方式四：Python代码调用
```python
from image_generator import ImageGenerator

generator = ImageGenerator()
result = generator.generate_from_prompt_file("prompt.md")
```

## 项目结构

```
home-design-prompts/
├── .env                          # API配置文件
├── README.md                     # 项目说明
├── image_generator.py            # 图像生成模块
├── generate_image.py             # 命令行工具
├── .trae/skills/home-design-prompts/
│   ├── SKILL.md                  # Skill定义文件
│   └── image_integration.md      # 集成说明
└── JZ001_0506_xxx/               # 生成的提示词目录
    ├── prompt.md                 # 提示词文件
    └── generated_image.jpg       # 生成的图像
```

## 目录命名规则

生成的目录按以下格式命名：
```
JZ[编号]_[MMDD]_[风格]_[空间类型]设计
```

示例：
- `JZ001_0506_现代简约_卧室设计`
- `JZ002_0510_北欧风_客厅设计`

## 提示词示例

### 现代简约卧室（冷调）
```
Modern minimalist bedroom with serene atmosphere, low platform bed 
with clean geometric lines, sleek minimalist nightstand in matte 
black finish, cool color palette of soft grey and pale blue tones, 
ambient mood lighting creating subtle shadows, eye level perspective 
showcasing balanced composition
```

### 法式奶油风客餐厅
```
Bright and airy French cream style open living dining space, 
elegant arched doorway with decorative molding, plush cream colored 
linen sofa, natural oak wood coffee table, soft cream and ivory 
color palette with warm wood accents
```

## 技术参数说明

| 参数 | 说明 | 常用值 |
|------|------|--------|
| --ar | 宽高比 | 16:9, 4:5, 9:16 |
| --s | 风格化程度 | 200-300 |
| --q | 图像质量 | 2 |
| --v | 模型版本 | 6 |

## 贡献指南

欢迎提交Issue和Pull Request！

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎通过GitHub Issues交流。
