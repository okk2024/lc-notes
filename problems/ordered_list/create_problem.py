for i in range(51):
    filename = f"q{i}xx.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# LeetCode 题解 {i*100}~{i*100+99}\n\n")
        # 可选：写入一个占位符，后面再填内容
        f.write("<!-- 每道题的简化描述 -->\n")
    print(f"已创建: {filename}")