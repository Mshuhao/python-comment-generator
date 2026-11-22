import argparse
from comment_generator import CommentGenerator

def main():
    parser = argparse.ArgumentParser(description="Python代码自动注释生成工具")
    parser.add_argument("input", help="输入的Python文件路径")
    parser.add_argument("-o", "--output", default="output.py", help="输出文件路径")
    args = parser.parse_args()

    generator = CommentGenerator()
    generator.process_file(args.input, args.output)

if __name__ == "__main__":
    main()
