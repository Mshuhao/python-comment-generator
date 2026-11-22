# Python 代码自动注释生成工具

基于大模型 API 的 Python 代码自动注释工具，自动为代码生成清晰的中文注释，提升代码可读性与可维护性。

## 功能特点
- 基于 AST 语法解析识别代码结构
- 调用大模型自动生成中文行注释与函数说明
- 支持批量处理单个 Python 文件
- 命令行调用，简单易用

## 技术栈
- Python 3.11+
- OpenAI 兼容大模型 API
- AST 语法树解析
- python-dotenv 环境配置

## 使用方法
1. 安装依赖
```bash
pip install -r requirements.txt
