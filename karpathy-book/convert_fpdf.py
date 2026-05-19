#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert Karpathy book markdown to PDF using FPDF"""

import os
import re

# Try markdown conversion
try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("markdown not available, using simple parsing")

from fpdf import FPDF

class PDFBook(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.alias_nb_pages()
        self.chapter_count = 0
        
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Andrej Karpathy', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 6, 'AI界的灵魂导师 - 深度解析', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Paths
md_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\README.md"
pdf_path = r"C:\Users\Gao Wei\.qclaw\workspace\karpathy-book\karpathy-book.pdf"

# Create PDF
pdf = PDFBook()
pdf.add_page()

# Set font
pdf.set_font('Arial', '', 10)

# Read markdown and convert simply
with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Simple conversion
in_code_block = False
for line in lines:
    line = line.rstrip()
    
    # Skip empty lines at start
    if not line.strip() and pdf.get_y() < 20:
        continue
        
    # Code blocks
    if line.startswith('```'):
        in_code_block = not in_code_block
        if in_code_block:
            pdf.set_font('Courier', '', 9)
        else:
            pdf.set_font('Arial', '', 10)
        continue
        
    if in_code_block:
        pdf.cell(0, 5, line[:80], 0, 1, 'L')
        continue
        
    # Headers
    if line.startswith('# '):
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 8, line[2:], 0, 1, 'L')
        pdf.set_font('Arial', '', 10)
    elif line.startswith('## '):
        pdf.ln(3)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 7, line[3:], 0, 1, 'L')
        pdf.set_font('Arial', '', 10)
    elif line.startswith('### '):
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(0, 6, line[4:], 0, 1, 'L')
        pdf.set_font('Arial', '', 10)
    # Horizontal line
    elif line == '---':
        pdf.ln(2)
        pdf.cell(0, 1, '', 0, 1, 'L')
        pdf.ln(2)
    # Empty line
    elif not line.strip():
        pdf.ln(2)
    # Regular text
    else:
        # Handle long lines
        if len(line) > 90:
            pdf.multi_cell(0, 5, line[:90], 0, 'L')
            if len(line) > 180:
                pdf.multi_cell(0, 5, line[90:180], 0, 'L')
        else:
            pdf.cell(0, 5, line[:90], 0, 1, 'L')

# Output
pdf.output(pdf_path)
file_size = os.path.getsize(pdf_path)
print(f"PDF created: {pdf_path}")
print(f"Size: {file_size} bytes ({file_size/1024:.1f} KB)")