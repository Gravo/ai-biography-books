# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

font_name = "ChineseFont"
for path in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf"]:
    if os.path.exists(path):
        try:
            pdfmetrics.registerFont(TTFont(font_name, path))
            print(f"Font: {path}")
            break
        except: pass
else: font_name = "Helvetica"

md_path = r"C:\Users\Gao Wei\.qclaw\workspace\leopold-book\README.md"
pdf_path = r"C:\Users\Gao Wei\.qclaw\workspace\leopold-book\leopold-aschenbrenner-book.pdf"

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Heading1'], fontName=font_name, fontSize=24, alignment=TA_CENTER, spaceAfter=30)
h1_style = ParagraphStyle('H1', parent=styles['Heading1'], fontName=font_name, fontSize=18, spaceBefore=20)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontName=font_name, fontSize=14, spaceBefore=15)
h3_style = ParagraphStyle('H3', parent=styles['Heading3'], fontName=font_name, fontSize=12, spaceBefore=10)
body_style = ParagraphStyle('B', parent=styles['Normal'], fontName=font_name, fontSize=10, leading=14)
quote_style = ParagraphStyle('Q', parent=styles['Normal'], fontName=font_name, fontSize=10, leftIndent=20, textColor='gray')

with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
story = []
in_code = False

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

for line in lines:
    line = line.rstrip()
    if line.startswith('```'):
        in_code = not in_code
        continue
    if in_code:
        story.append(Paragraph(f"<font face='Courier' size='9'>{esc(line)}</font>", body_style))
        continue
    if line.startswith('|'):
        if '---' in line: continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if cells: story.append(Paragraph(f"<font size='9'>{esc(' | '.join(cells))}</font>", body_style))
        continue
    if not line.strip():
        story.append(Spacer(1, 6))
        continue
    t = esc(line)
    if t.startswith('# '): story.append(Paragraph(t[2:], title_style))
    elif t.startswith('## '): story.append(Paragraph(t[3:], h1_style))
    elif t.startswith('### '): story.append(Paragraph(t[4:], h2_style))
    elif t.startswith('#### '): story.append(Paragraph(t[5:], h3_style))
    elif t == '---': story.append(Spacer(1, 10))
    elif t.startswith('&gt;'): story.append(Paragraph(t[5:].strip().strip('"\''), quote_style))
    elif t.startswith('- ') or t.startswith('* '): story.append(Paragraph('\u2022 ' + t[2:], body_style))
    else: story.append(Paragraph(t, body_style))

doc.build(story)
print(f"\nPDF: {pdf_path}")
print(f"Size: {os.path.getsize(pdf_path)/1024:.1f} KB")