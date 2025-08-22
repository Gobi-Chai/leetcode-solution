import os
import re

# 你的 leetcode-solutions 文件夹路径
ROOT = "./leetcode-solutions"
OUTPUT = "leetcode.md"

# 支持的后缀
EXTS = [".py", ".cpp", ".java"]

def extract_title(fname):
    """从文件名中提取题号和题目名"""
    base = os.path.basename(fname)
    name, ext = os.path.splitext(base)
    m = re.match(r"(\d+)[\.\-_ ]*(.*)", name)
    if m:
        qid, title = m.groups()
        title = title.replace("_", " ").replace("-", " ").title()
        return f"{qid}. {title}"
    return name

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("# LeetCode 刷题总结\n\n")
    for root, _, files in os.walk(ROOT):
        for f in sorted(files):
            if any(f.endswith(ext) for ext in EXTS):
                path = os.path.join(root, f)
                title = extract_title(f)
                out.write(f"## {title}\n\n")
                lang = "python" if f.endswith(".py") else "cpp" if f.endswith(".cpp") else "java"
                with open(path, "r", encoding="utf-8", errors="ignore") as codefile:
                    code = codefile.read()
                out.write(f"```{lang}\n{code}\n```\n\n---\n\n")

print(f"✅ 已生成 {OUTPUT}")
