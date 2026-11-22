from ast_parser import CodeParser
from llm_client import LLMClient

class CommentGenerator:
    def __init__(self):
        self.llm = LLMClient()

    def process_file(self, input_path: str, output_path: str):
        """处理单个Python文件，生成带注释的文件"""
        with open(input_path, "r", encoding="utf-8") as f:
            code = f.read()

        parser = CodeParser(code)
        funcs = parser.extract_functions()
        classes = parser.extract_classes()

        # 整体生成注释
        commented_code = self.llm.generate_comment(code)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(commented_code)

        print(f"✅ 注释生成完成，已保存到 {output_path}")
