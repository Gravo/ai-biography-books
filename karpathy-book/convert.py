#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert Karpathy book markdown to PDF"""

import markdown
from weasyprint import HTML, CSS
import os

# Paths
md_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\README.md"
pdf_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\book.pdf"
html_file = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\book.html"

# Read markdown
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Full HTML with styling
html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Andrej Karpathy——AI界的灵魂导师</title>
<style>
body { font-family: "Microsoft YaHei", "SimSun", sans-serif; margin: 50px; line-height: 1.8; font-size: 12pt; }
h1 { text-align: center; color: #1a1a2e; border-bottom: 3px solid #16213e; padding-bottom: 15px; font-size: 24pt; }
h2 { color: #16213e; border-left: 5px solid #0f3460; padding-left: 15px; margin-top: 30px; font-size: 18pt; }
h3 { color: #533483; font-size: 14pt; }
code { background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-family: Consolas, monospace; }
pre { background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; font-size: 10pt; }
table { border-collapse: collapse; width: 100%; margin: 15px 0; font-size: 11pt; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background: #16213e; color: white; }
tr:nth-child(even) { background: #f9f9f9; }
blockquote { border-left: 4px solid #e94560; margin: 15px 0; padding-left: 15px; color: #555; font-style: italic; }
ul, ol { margin: 10px 0; padding-left: 25px; }
li { margin: 5px 0; }
hr { border: none; border-top: 1px solid #ddd; margin: 30px 0; }
</style>
</head>
<body>
""" + html_body + """
</body>
</html>"""

# Write HTML file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML created: {html_file}")

# Convert HTML to PDF using weasyprint
doc = HTML(filename=html_file)
doc.write_pdf(pdf_path)

print(f"PDF created: {pdf_path}")
print(f"PDF size: {os.path.getsize(pdf_path)} bytes")