from config import Config

class LLMClient:
    def __init__(self):
        # 接入真实大模型时取消下方注释，并在 .env 中配置对应参数即可
        # from openai import OpenAI
        # self.client = OpenAI(
        #     api_key=Config.API_KEY,
        #     base_url=Config.BASE_URL
        # )
        # self.model = Config.MODEL
        pass

    def generate_comment(self, code_snippet: str) -> str:
        """
        生成代码注释
        演示版本：模拟大模型返回带注释的代码
        接入真实大模型时，直接替换本方法内部逻辑即可
        """
        lines = code_snippet.splitlines()
        result = []
        in_class = False
        for line in lines:
            stripped = line.strip()
            # 类定义前加注释
            if stripped.startswith("class "):
                result.append("# 类定义：封装用户相关数据与方法")
                in_class = True
            # 函数定义前加注释
            elif stripped.startswith("def "):
                if in_class and "__init__" in stripped:
                    result.append("    # 初始化方法：设置类的初始属性")
                elif "get_info" in stripped:
                    result.append("    # 获取用户信息方法：返回格式化的用户信息字符串")
                elif "calculate_total" in stripped:
                    result.append("# 计算总价函数：接收价格列表，返回累加后的总金额")
            result.append(line)
        return "\n".join(result)
