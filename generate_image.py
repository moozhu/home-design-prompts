#!/usr/bin/env python3
"""
快速生图脚本
用法:
    python generate_image.py "提示词"
    python generate_image.py --file prompt.md
    python generate_image.py --file prompt.md --output result.jpg
"""

import argparse
import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from image_generator import ImageGenerator


def main():
    parser = argparse.ArgumentParser(description='生成家居设计图像')
    parser.add_argument('prompt', nargs='?', help='图像生成提示词（英文）')
    parser.add_argument('--file', '-f', help='从提示词文件生成（Markdown格式）')
    parser.add_argument('--output', '-o', default='generated_image.jpg', help='输出图像路径')
    parser.add_argument('--dir', '-d', default='.', help='输出目录')
    
    args = parser.parse_args()
    
    # 创建生成器
    try:
        generator = ImageGenerator()
    except ValueError as e:
        print(f"[错误] {e}")
        print("请确保.env文件中设置了MODELSCOPE_API_KEY")
        sys.exit(1)
    
    # 从文件生成
    if args.file:
        if not os.path.exists(args.file):
            print(f"[错误] 文件不存在 {args.file}")
            sys.exit(1)
        
        print(f"[信息] 从文件加载提示词: {args.file}")
        result = generator.generate_from_prompt_file(
            prompt_file_path=args.file,
            output_dir=args.dir
        )
    
    # 从提示词生成
    elif args.prompt:
        print(f"[信息] 生成图像: {args.prompt[:50]}...")
        result = generator.generate_image(
            prompt=args.prompt,
            output_path=os.path.join(args.dir, args.output)
        )
    
    else:
        parser.print_help()
        sys.exit(1)
    
    # 显示结果
    if result["success"]:
        print(f"\n[成功] 图像生成成功!")
        print(f"[信息] 保存路径: {result['image_path']}")
        if 'image_url' in result:
            print(f"[信息] 在线地址: {result['image_url']}")
    else:
        print(f"\n[失败] 图像生成失败")
        print(f"错误信息: {result.get('error', '未知错误')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
