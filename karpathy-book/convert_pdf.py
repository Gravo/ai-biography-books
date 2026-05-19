# -*- coding: utf-8 -*-
"""Convert Karpathy book to PDF using ReportLab"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register Chinese font
font_paths = [
    "C:/Windows/Fonts/msyh.ttc",  # Microsoft YaHei
    "C:/Windows/Fonts/simhei.ttf",  # SimHei
    "C:/Windows/Fonts/simsun.ttc",  # SimSun
]

font_name = "ChineseFont"
for path in font_paths:
    if os.path.exists(path):
        try:
            pdfmetrics.registerFont(TTFont(font_name, path))
            print(f"Font loaded: {path}")
            break
        except:
            continue
else:
    font_name = "Helvetica"
    print("Using default font (Chinese may not display correctly)")

# Paths
md_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\README.md"
pdf_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\karpathy-book.pdf"

# Create styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName=font_name,
    fontSize=24,
    alignment=TA_CENTER,
    spaceAfter=30,
)

h1_style = ParagraphStyle(
    'CustomH1',
    parent=styles['Heading1'],
    fontName=font_name,
    fontSize=18,
    spaceBefore=20,
    spaceAfter=12,
)

h2_style = ParagraphStyle(
    'CustomH2',
    parent=styles['Heading2'],
    fontName=font_name,
    fontSize=14,
    spaceBefore=15,
    spaceAfter=8,
)

h3_style = ParagraphStyle(
    'CustomH3',
    parent=styles['Heading3'],
    fontName=font_name,
    fontSize=12,
    spaceBefore=10,
    spaceAfter=6,
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontName=font_name,
    fontSize=10,
    leading=14,
    spaceBefore=3,
    spaceAfter=3,
)

code_style = ParagraphStyle(
    'CustomCode',
    parent=styles['Code'],
    fontName='Courier',
    fontSize=9,
    leading=11,
    leftIndent=20,
    spaceBefore=5,
    spaceAfter=5,
)

quote_style = ParagraphStyle(
    'CustomQuote',
    parent=styles['Normal'],
    fontName=font_name,
    fontSize=10,
    leftIndent=20,
    textColor='gray',
    spaceBefore=5,
    spaceAfter=5,
)

# Read markdown
with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Create PDF
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        rightMargin=2*cm, leftMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm)

story = []
in_code = False
code_buffer = []

for line in lines:
    line = line.rstrip()
    
    # Code blocks
    if line.startswith('```'):
        if in_code:
            # End code block
            if code_buffer:
                code_text = '\n'.join(code_buffer)
                story.append(Paragraph(f"<font face='Courier' size='9'>{code_text}</font>", body_style))
            code_buffer = []
        in_code = not in_code
        continue
    
    if in_code:
        code_buffer.append(line.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;'))
        continue
    
    # Skip empty lines
    if not line.strip():
        story.append(Spacer(1, 6))
        continue
    
    # Escape HTML
    text = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Headers
    if text.startswith('# '):
        story.append(Paragraph(text[2:], title_style))
    elif text.startswith('## '):
        story.append(Paragraph(text[3:], h1_style))
    elif text.startswith('### '):
        story.append(Paragraph(text[4:], h2_style))
    elif text.startswith('#### '):
        story.append(Paragraph(text[5:], h3_style))
    elif text == '---':
        story.append(Spacer(1, 10))
    elif text.startswith('&gt;'):  # Blockquote
        story.append(Paragraph(text[5:].strip(), quote_style))
    elif text.startswith('- ') or text.startswith('* '):
        story.append(Paragraph('• ' + text[2:], body_style))
    elif text.startswith('|'):  # Table - skip for now
        continue
    else:
        # Handle inline code
        text = text.replace('`', "'")
        story.append(Paragraph(text, body_style))

# Build PDF
doc.build(story)

print(f"\nPDF created: {pdf_path}")
print(f"Size: {os.path.getsize(pdf_path)} bytes ({os.path.getsize(pdf_path)/1024:.1f} KB)")