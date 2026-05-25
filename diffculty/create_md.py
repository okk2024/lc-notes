import os
from pathlib import Path

# ================= 配置区 =================
DIRS = ['simple', 'medium', 'hard']   # 目标目录
START = 0                             # 起始序号（包含）
END = 50                              # 结束序号（包含） → 共 51 个数字/目录
# 如果想生成 150 个文件（每个目录 50 个），请将 END 改为 49
# =========================================

for dir_name in DIRS:
    dir_path = Path(dir_name)
    # 确保目录存在（如果不存在则创建）
    dir_path.mkdir(exist_ok=True)
    
    for i in range(START, END + 1):
        # 文件名格式：{序号}xx_{目录名}.md
        filename = f"{i}xx_{dir_name}.md"
        file_path = dir_path / filename
        
        # 写入文件（'w' 模式会覆盖已存在的同名文件）
        with open(file_path, 'w', encoding='utf-8') as f:
            # 可选：写入一个简单的 markdown 标题，方便后续编辑
            f.write(f"# {dir_name.upper()} Problem {i}\n\n")
            f.write("<!-- 题解内容 -->\n")
        
        print(f"已创建: {file_path}")

print("全部文件生成完毕！")