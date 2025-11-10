# ComfyUI 火山引擎 Doubao-Seed-1.6 节点

这个自定义节点包为 ComfyUI 提供了与火山引擎的 Doubao-Seed-1.6 多模态模型的集成功能。

## 功能特点

- 支持图像内容理解和分析
- 同时输出中文和英文分析结果
- 可调节的思考模式（reasoning effort）
- 用户友好的界面

## 安装说明

1. 确保已安装 ComfyUI
2. 将此仓库克隆到 ComfyUI 的 `custom_nodes` 目录中：
```bash
cd custom_nodes
git clone [仓库地址]
```
3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 准备工作
1. 获取火山引擎的 API 密钥
2. 在节点的 API_KEY 输入框中填入您的密钥

### 节点配置
- **图像输入**：连接需要分析的图像
- **API_KEY**：输入您的火山引擎 API 密钥
- **System Prompt**：设置系统提示词
- **User Prompt**：设置用户提示词
- **Reasoning Effort**：选择思考模式
  - minimal：不思考
  - low：低度思考
  - medium：中度思考
  - high：高度思考

### 输出说明
- **中文输出**：模型生成的中文分析结果
- **英文输出**：自动翻译的英文分析结果

## 注意事项

- API 调用可能需要一定时间，请耐心等待
- 建议合理设置 System Prompt 和 User Prompt 以获得更好的分析结果
- 请确保您有足够的 API 调用额度

## 环境要求

- Python 3.8+
- ComfyUI
- 见 requirements.txt 的其他依赖

## 许可证

MIT License

## 作者

Fredy

## 更新日期

2025-11-08
