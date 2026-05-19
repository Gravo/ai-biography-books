# -*- coding: utf-8 -*-
"""Simple markdown to HTML converter"""

md_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\README.md"
html_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\book.html"

with open(md_path, "r", encoding="utf-8") as f:
    md = f.read()

lines = md.split("\n")
html = ["<!DOCTYPE html><html><head><meta charset='utf-8'><title>Andrej Karpathy</title></head><body>"]

for line in lines:
    s = line.strip()
    if not s:
        html.append("<br>")
    elif s.startswith("# "):
        html.append(f"<h1>{s[2:]}</h1>")
    elif s.startswith("## "):
        html.append(f"<h2>{s[3:]}</h2>")
    elif s.startswith("### "):
        html.append(f"<h3>{s[4:]}</h3>")
    elif s == "---":
        html.append("<hr>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write("".join(html) + "</body></html>")

import os
print(f"HTML: {html_path}")
print(f"Size: {os.path.getsize(html_path)} bytes")