#!/usr/bin/env python3
"""Generate Ian Goodfellow research book PDF from merged markdown."""

import re
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Chinese font
pdfmetrics.registerFont(TTFont('MSYH', 'C:\\Windows\\Fonts\\msyh.ttc', subfontIndex=0))

# Styles
title_style = ParagraphStyle('Title', fontName='MSYH', fontSize=24, leading=30,
                              spaceAfter=20, alignment=1, textColor=HexColor('#1a1a2e'))
h1_style = ParagraphStyle('H1', fontName='MSYH', fontSize=18, leading=24,
                           spaceBefore=20, spaceAfter=10, textColor=HexColor('#16213e'))
h2_style = ParagraphStyle('H2', fontName='MSYH', fontSize=14, leading=18,
                           spaceBefore=15, spaceAfter=8, textColor=HexColor('#0f3460'))
h3_style = ParagraphStyle('H3', fontName='MSYH', fontSize=12, leading=16,
                           spaceBefore=10, spaceAfter=6, textColor=HexColor('#533483'))
body_style = ParagraphStyle('Body', fontName='MSYH', fontSize=10, leading=14,
                             spaceBefore=3, spaceAfter=3)
bold_style = ParagraphStyle('Bold', fontName='MSYH', fontSize=10, leading=14,
                             spaceBefore=3, spaceAfter=3)
formula_style = ParagraphStyle('Formula', fontName='MSYH', fontSize=9, leading=12,
                               spaceBefore=5, spaceAfter=5, alignment=1,
                               textColor=HexColor('#333333'))

# Read merged markdown
md_path = r'C:\Users\Gao Wei\.qclaw\workspace\ian-goodfellow-book\ian-goodfellow-book.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Parse markdown to reportlab elements
def md_to_paragraphs(text):
    elements = []
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Horizontal rule -> page break
        if line == '---':
            elements.append(PageBreak())
            i += 1
            continue
        
        # Headers
        if line.startswith('# ') and not line.startswith('## '):
            elements.append(Paragraph(line[2:], title_style))
            i += 1
            continue
        
        if line.startswith('## '):
            elements.append(Paragraph(line[3:], h2_style))
            i += 1
            continue
        
        if line.startswith('### '):
            elements.append(Paragraph(line[4:], h3_style))
            i += 1
            continue
        
        # Table rows
        if line.startswith('|') and '|' in line:
            # Collect table lines
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            
            # Skip separator lines
            data_lines = [l for l in table_lines if not re.match(r'^\|[\s\-:|]+\|$', l)]
            
            if data_lines:
                table_data = []
                for dl in data_lines:
                    cells = [c.strip() for c in dl.split('|')[1:-1]]
                    table_data.append(cells)
                
                if table_data:
                    try:
                        col_count = max(len(row) for row in table_data)
                        # Normalize row lengths
                        for row in table_data:
                            while len(row) < col_count:
                                row.append('')
                        
                        t = Table(table_data, colWidths=[150//col_count*mm]*col_count)
                        t.setStyle(TableStyle([
                            ('FONTNAME', (0,0), (-1,-1), 'MSYH'),
                            ('FONTSIZE', (0,0), (-1,-1), 8),
                            ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
                            ('BACKGROUND', (0,0), (-1,0), HexColor('#e8e8e8')),
                        ]))
                        elements.append(t)
                    except Exception:
                        for dl in data_lines:
                            elements.append(Paragraph(dl, body_style))
            continue
        
        # Code blocks
        if line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = '<br/>'.join(code_lines)
            elements.append(Paragraph(code_text, formula_style))
            continue
        
        # Escape HTML-unsafe chars before any conversion
        line = line.replace('&', '&amp;')
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        
        # Math formulas ($...$) -> bold (already escaped above, so use escaped versions)
        line = re.sub(r'\$([^$]+)\$', r'<b>\1</b>', line)
        
        # Bold (**...**)
        line = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', line)
        
        # Fix any unclosed <b> tags
        open_count = line.count('<b>')
        close_count = line.count('</b>')
        while close_count < open_count:
            line += '</b>'
            close_count += 1
        
        # Regular paragraph
        elements.append(Paragraph(line, body_style))
        i += 1
    
    return elements

# Build PDF
pdf_path = r'C:\Users\Gao Wei\.qclaw\workspace\ian-goodfellow-book\ian-goodfellow-book.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=20*mm, bottomMargin=20*mm)

# Title page
title_elements = [
    Spacer(1, 80*mm),
    Paragraph('Ian Goodfellow', title_style),
    Paragraph('深度研究书籍', ParagraphStyle('SubTitle', fontName='MSYH', fontSize=16, leading=20, alignment=1)),
    Spacer(1, 20*mm),
    Paragraph('GAN之父 · 对抗性机器学习先驱 · Deep Learning教科书作者', ParagraphStyle('Desc', fontName='MSYH', fontSize=11, leading=14, alignment=1, textColor=HexColor('#666666'))),
    Spacer(1, 40*mm),
    Paragraph('从博弈论到世界模型', ParagraphStyle('Tagline', fontName='MSYH', fontSize=13, leading=16, alignment=1, textColor=HexColor('#0f3460'))),
    Spacer(1, 30*mm),
    Paragraph('2026', ParagraphStyle('Year', fontName='MSYH', fontSize=12, leading=14, alignment=1, textColor=HexColor('#999999'))),
    PageBreak(),
]

# Content
content_elements = md_to_paragraphs(md_content)

all_elements = title_elements + content_elements

print(f"Building PDF with {len(all_elements)} elements...")
doc.build(all_elements)
print(f"PDF saved to: {pdf_path}")
print(f"File size: {os.path.getsize(pdf_path)} bytes")