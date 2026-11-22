import ast
from typing import List, Dict

class CodeParser:
    def __init__(self, code: str):
        self.code = code
        self.tree = ast.parse(code)
        self.lines = code.splitlines()

    def extract_functions(self) -> List[Dict]:
        """提取所有函数信息"""
        funcs = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                funcs.append({
                    "name": node.name,
                    "lineno": node.lineno,
                    "end_lineno": node.end_lineno,
                    "args": [arg.arg for arg in node.args.args],
                    "code": "\n".join(self.lines[node.lineno-1 : node.end_lineno])
                })
        return funcs

    def extract_classes(self) -> List[Dict]:
        """提取所有类信息"""
        classes = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                classes.append({
                    "name": node.name,
                    "lineno": node.lineno,
                    "end_lineno": node.end_lineno,
                    "code": "\n".join(self.lines[node.lineno-1 : node.end_lineno])
                })
        return classes
