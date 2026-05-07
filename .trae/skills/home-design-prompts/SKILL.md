---
name: "home-design-prompts"
description: "专业家居家装Midjourney/Image2提示词生成器。当用户输入'家居提示词'、'家居设计'或需要生成室内设计AI图像提示词时激活。支持对话式引导、提示词优化、图像分析三种模式。"
---

# 家居家装提示词生成专家

## 触发条件

当用户输入以下关键词时激活此Skill：
- "家居提示词"
- "家居设计"
- "室内设计提示词"
- "家装AI绘图"
- "生成家居提示词"
- 任何与家居/室内设计相关的AI图像生成请求

## 核心功能

本Skill提供三种工作模式，根据用户输入自动判断并切换：

### 模式一：对话式引导生成（无具体要求时）

当用户没有提供具体设计需求时，通过结构化对话收集关键信息。

**询问维度清单：**

1. **空间类型**（必选）
   - 客厅 / 卧室 / 厨房 / 餐厅 / 卫生间 / 书房 / 阳台 / 玄关 / 儿童房 / 老人房

2. **设计风格**（必选）
   - 现代简约 / 北欧 / 新中式 / 轻奢 / 日式 / 美式 / 欧式古典 / 工业风 / 侘寂风 / 地中海 / 法式 / 奶油风

3. **主体元素**（多选）
   - 沙发 / 茶几 / 电视柜 / 餐桌 / 床 / 衣柜 / 书桌 / 橱柜 / 灯具 / 窗帘 / 地毯 / 装饰画 / 绿植 / 书架 / 壁炉

4. **材质偏好**（多选）
   - 实木 / 大理石 / 金属 / 玻璃 / 布艺 / 皮革 / 藤编 / 水泥 / 瓷砖 / 木地板 / 岩板 / 丝绒

5. **色调方案**（单选）
   - 暖色调（米白/驼色/暖灰/原木色）
   - 冷色调（灰蓝/墨绿/深灰/黑色）
   - 中性色调（白/灰/米色）
   - 撞色搭配（具体说明）

6. **光线氛围**（单选）
   - 自然光充足 / 柔和暖光 / 明亮冷光 / 氛围灯光 / 黄昏光线

7. **视角要求**（单选）
   - 全景视角 / 平视角度 / 俯视角度 / 细节特写

8. **特殊要求**（可选）
   - 开放式布局 / 收纳展示 / 智能家居 / 环保材料 / 宠物友好 / 儿童安全

**对话流程：**
1. 向用户说明将进行8个维度的询问
2. 逐维度提问，提供选项让用户选择
3. 每完成一个维度，简要确认已选内容
4. 全部完成后，生成完整提示词

### 模式二：提示词优化生成（有具体要求时）

当用户已提供风格、主体、材料等信息时，直接进行专业优化。

**优化策略：**

1. **结构化重组**
   - 按"主体描述 → 风格定义 → 材质细节 → 光线氛围 → 视角构图 → 技术参数"顺序组织

2. **专业术语增强**
   - 添加行业标准描述词
   - 引入设计领域专业词汇
   - 补充材质纹理细节

3. **视觉细节丰富**
   - 添加光影效果描述
   - 补充空间层次感
   - 强化材质质感表现

4. **技术参数优化**
   - 推荐合适的宽高比（--ar）
   - 设置风格化程度（--s）
   - 指定图像质量（--q）
   - 选择适合的模型版本

**输出格式：**
```markdown
## 优化后的提示词

**英文提示词（主）：**
[专业英文提示词]

**中文提示词（参考）：**
[对应中文翻译]

**生成参数：**
- 宽高比：--ar [比例]
- 风格化：--s [数值]
- 图像质量：--q [数值]
- 模型版本：--v [版本]

**设计说明：**
[设计理念和关键元素说明]
```

### 模式三：图像分析与提示词提取（图像输入时）

当用户提供家居设计图片时，进行视觉元素分析并生成提示词。

**分析维度：**

1. **空间识别**
   - 判断房间类型
   - 估算空间面积感
   - 识别布局特点

2. **风格解析**
   - 确定设计风格流派
   - 识别地域特色元素
   - 分析时代特征

3. **元素提取**
   - 主体家具识别
   - 装饰品与配饰
   - 材质纹理判断
   - 色彩搭配分析

4. **光线分析**
   - 光源类型判断
   - 光线方向识别
   - 氛围效果描述

5. **构图分析**
   - 拍摄视角
   - 景深效果
   - 画面比例

**输出格式：**
```markdown
## 图像分析报告

**空间类型：** [识别结果]

**设计风格：** [分析结果]

**关键元素识别：**
- 家具：[列表]
- 材质：[列表]
- 色彩：[主色调+辅助色]
- 光线：[描述]

**提取的提示词：**

**英文提示词：**
[基于分析生成的提示词]

**生成参数建议：**
- 宽高比：[根据图像比例]
- 其他参数：[推荐设置]

**相似风格变体建议：**
[提供2-3个风格调整方向]
```

## 文件组织规范

### 目录命名规则
格式：`JZ[编号]_[MMDD]_[风格]_[空间类型]设计`

**命名说明：**
- `JZ`：家装（Jia Zhuang）缩写
- `[编号]`：3位顺序递增编号，从001开始
- `[MMDD]`：月份和日期（4位数字）
- `[风格]`：设计风格名称
- `[空间类型]`：客厅/卧室/厨房等

**示例：**
- `JZ001_1105_现代简约_客厅设计`
- `JZ002_1106_北欧风_卧室设计`
- `JZ003_1208_法式奶油风_客餐厅设计`

### 文件创建流程

1. **获取当前编号**
   - 检查已有目录，获取最新编号
   - 新编号 = 最新编号 + 1
   - 格式化为3位数字（如：001, 002, 010）

2. **获取当前日期**
   - 格式：MMDD（月日，4位数字）
   - 示例：0506（5月6日）、1125（11月25日）

3. **提取关键信息**
   - 风格名称
   - 空间类型

4. **生成目录名**
   - 组合：JZ + 编号 + 月日 + 风格 + 空间
   - 示例：`JZ001_0506_现代简约_卧室设计`

5. **创建文件**
   - 文件名：`prompt.md`
   - 路径：`[目录名]/prompt.md`

### Markdown文件模板

```markdown
# 家居设计提示词

**创建时间：** [日期时间]
**设计类型：** [空间类型]
**设计风格：** [风格名称]

---

## 提示词内容

### 英文提示词
```
[完整英文提示词]
```

### 中文参考
[中文翻译]

---

## 生成参数

| 参数 | 设置值 | 说明 |
|------|--------|------|
| 宽高比 | --ar [值] | [说明] |
| 风格化 | --s [值] | [说明] |
| 图像质量 | --q [值] | [说明] |
| 模型版本 | --v [值] | [说明] |

---

## 设计要素解析

### 核心元素
[关键设计元素说明]

### 材质搭配
[材质组合说明]

### 色彩方案
[色彩搭配逻辑]

### 光线设计
[光线氛围营造]

---

## 变体建议

### 调整方向1：[方向名称]
**修改建议：** [具体调整内容]
**适用场景：** [场景说明]

### 调整方向2：[方向名称]
**修改建议：** [具体调整内容]
**适用场景：** [场景说明]

---

## 参考资源

- 创建来源：[模式一/二/三]
- 原始输入：[用户原始输入内容]
```

## 专业提示词库

### 空间类型关键词

| 空间 | 英文关键词 | 补充描述 |
|------|-----------|----------|
| 客厅 | living room, lounge | spacious, open-plan |
| 卧室 | bedroom, master suite | cozy, intimate |
| 厨房 | kitchen, culinary space | modern, functional |
| 餐厅 | dining room, dining area | elegant, inviting |
| 卫生间 | bathroom, powder room | spa-like, serene |
| 书房 | study, home office | productive, quiet |
| 儿童房 | kids room, nursery | playful, safe |

### 设计风格关键词

| 风格 | 英文关键词 | 特征描述 |
|------|-----------|----------|
| 现代简约 | modern minimalist, contemporary | clean lines, uncluttered |
| 北欧 | Scandinavian, Nordic | hygge, natural light |
| 新中式 | neo-Chinese, modern oriental | traditional meets contemporary |
| 轻奢 | light luxury, understated elegance | premium materials, subtle opulence |
| 日式 | Japanese, Zen, wabi-sabi | tatami, shoji, natural materials |
| 工业风 | industrial, loft style | exposed brick, metal, raw |
| 侘寂风 | wabi-sabi, imperfect beauty | weathered textures, muted tones |
| 法式 | French, Parisian | ornate details, romantic |
| 奶油风 | cream style, soft neutral | warm whites, curved forms |

### 材质关键词

| 材质 | 英文关键词 | 质感描述 |
|------|-----------|----------|
| 实木 | solid wood, natural wood | grain texture, warm |
| 大理石 | marble, Carrara | veining, luxurious |
| 金属 | brass, copper, gold | metallic sheen, reflective |
| 玻璃 | glass, tempered glass | transparent, glossy |
| 布艺 | linen, cotton, velvet | soft, tactile |
| 皮革 | leather, suede | supple, aged patina |
| 水泥 | concrete, cement | raw, industrial |
| 岩板 | sintered stone, porcelain slab | sleek, durable |

### 光线氛围关键词

| 氛围 | 英文关键词 | 效果描述 |
|------|-----------|----------|
| 自然光 | natural light, sunlight | bright, airy |
| 柔和暖光 | soft warm lighting, ambient | cozy, inviting |
| 明亮冷光 | bright cool lighting, daylight | crisp, modern |
| 氛围灯光 | mood lighting, accent lighting | dramatic, intimate |
| 黄昏光线 | golden hour, sunset glow | warm, romantic |

### 视角构图关键词

| 视角 | 英文关键词 | 适用场景 |
|------|-----------|----------|
| 全景 | wide angle, panoramic | 展示整体空间 |
| 平视 | eye level, straight on | 真实感，沉浸式 |
| 俯视 | overhead, bird's eye | 展示布局，平面图感 |
| 特写 | close-up, detail shot | 强调材质细节 |
| 透视 | perspective, depth | 强调空间纵深感 |

## 提示词构建公式

### 基础公式
```
[空间类型] + [设计风格] + [主体元素] + [材质细节] + [色彩搭配] + [光线氛围] + [视角构图] + [技术参数]
```

### 高级公式（添加情感与品质）
```
[空间类型] + [设计风格] + [主体元素] + [材质细节] + [色彩搭配] + [光线氛围] + [情感氛围] + [品质描述] + [专业摄影] + [技术参数]
```

### 情感氛围词汇
- cozy and inviting（温馨宜人）
- serene and peaceful（宁静平和）
- luxurious and sophisticated（奢华精致）
- bright and energetic（明亮活力）
- calm and relaxing（平静放松）
- elegant and refined（优雅精致）

### 品质描述词汇
- high-end residential（高端住宅）
- architectural photography（建筑摄影）
- interior design magazine quality（室内设计杂志品质）
- photorealistic rendering（照片级渲染）
- professional staging（专业陈设）

## 完整示例

### 示例1：现代简约客厅

**用户输入：** 想要一个现代简约风格的客厅设计

**对话收集：**
- 空间：客厅
- 风格：现代简约
- 主体：L型沙发、茶几、电视柜
- 材质：布艺沙发、大理石茶几、原木电视柜
- 色调：中性色调（白、灰、米色）
- 光线：自然光充足
- 视角：全景视角

**生成提示词：**

英文：
```
Spacious modern minimalist living room, L-shaped beige linen sofa with clean lines, white marble coffee table with subtle grey veining, light oak TV console, neutral color palette of white, grey and warm beige, floor-to-ceiling windows with abundant natural light, airy and uncluttered space, wide angle architectural photography, photorealistic, interior design magazine quality --ar 16:9 --s 250 --q 2 --v 6
```

中文参考：
宽敞的现代简约客厅，L型米色亚麻沙发线条简洁，白色大理石茶几带有细腻灰色纹理，浅橡木电视柜，白、灰、暖米色的中性色调，落地窗引入充足自然光，通透整洁的空间，广角建筑摄影，照片级真实感，室内设计杂志品质

**生成参数：**
- --ar 16:9（适合展示完整空间）
- --s 250（适度风格化）
- --q 2（最高图像质量）
- --v 6（最新模型版本）

### 示例2：轻奢卧室

**用户输入：** 轻奢风格卧室，要有丝绒床头和金属灯具

**优化后提示词：**

英文：
```
Luxurious light luxury master bedroom, plush velvet upholstered headboard in deep emerald green, brass bedside lamps with fabric shades, cream colored silk bedding, marble nightstands with gold accents, soft ambient lighting creating intimate atmosphere, neutral walls with subtle texture, full length mirror with brass frame, high-end residential interior, sophisticated and elegant, professional interior photography, warm color palette with metallic touches --ar 4:5 --s 300 --q 2 --v 6
```

中文参考：
奢华轻奢主卧，深翠绿色丝绒软包床头，黄铜材质配布艺灯罩的床头灯，奶油色真丝床品，带金色装饰的大理石床头柜，柔和的环境光营造亲密氛围，带有细腻纹理的中性墙面，黄铜边框全身镜，高端住宅室内，精致优雅，专业室内摄影，暖色调搭配金属点缀

## 执行流程

1. **识别触发词**
   - 检测用户输入是否包含触发关键词

2. **判断工作模式**
   - 无具体要求 → 模式一（对话引导）
   - 有具体要求 → 模式二（直接优化）
   - 有图像输入 → 模式三（图像分析）

3. **执行对应模式**
   - 按模式流程处理用户请求

4. **生成提示词**
   - 根据收集/分析的信息构建专业提示词

5. **创建输出文件**
   - 按命名规则创建目录
   - 生成Markdown格式提示词文件

6. **图像生成（可选）**
   - 询问用户是否需要生成图像
   - 如用户确认，调用魔塔Qwen-Image-2512 API
   - 生成图像并保存到同一目录

7. **呈现结果**
   - 向用户展示生成的提示词
   - 说明文件保存位置
   - 如生成图像，展示图像路径
   - 提供使用建议

## 图像生成功能

本Skill已集成魔塔Qwen-Image-2512生图大模型，可根据提示词直接生成家居设计图像。

### 使用方法

#### 方法1：自动生成（推荐）
生成提示词后，Skill会自动询问：
> "提示词已生成并保存。是否需要立即生成图像？（是/否）"

用户确认后，自动调用API生成图像。

#### 方法2：命令行生成
```bash
# 从提示词文件生成
python generate_image.py --file JZ001_0506_现代简约_客厅设计/prompt.md

# 直接输入提示词生成
python generate_image.py "Modern minimalist living room with beige sofa"
```

#### 方法3：Python代码调用
```python
from image_generator import ImageGenerator

generator = ImageGenerator()
result = generator.generate_from_prompt_file("prompt.md")
```

### 配置要求

1. **安装依赖**
   ```bash
   pip install requests Pillow python-dotenv
   ```

2. **配置API Key**
   在根目录 `.env` 文件中设置：
   ```env
   MODELSCOPE_API_KEY=your_api_key_here
   MODELSCOPE_BASE_URL=https://api-inference.modelscope.cn/
   ```

### 生成参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| prompt | 图像生成提示词（自动提取英文） | 从文件读取 |
| output_path | 输出图像路径 | 同目录下的generated_image.jpg |
| wait_interval | 轮询间隔 | 5秒 |
| max_wait_time | 最大等待时间 | 300秒 |

### 输出结果

生成成功后，图像将保存在：
```
JZ001_0506_现代简约_客厅设计/
├── prompt.md              # 提示词文件
└── generated_image.jpg    # 生成的图像
```

## 注意事项

1. **专业准确性**
   - 使用准确的室内设计专业术语
   - 确保材质、风格描述符合行业标准

2. **细节完整性**
   - 提示词需包含足够细节以确保生成质量
   - 避免过于笼统的描述

3. **用户体验**
   - 对话模式要友好引导，不要一次性问太多问题
   - 及时确认用户选择，避免误解

4. **文件管理**
   - 确保目录命名唯一性
   - 文件内容格式规范统一
