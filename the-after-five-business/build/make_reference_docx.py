"""Create a pandoc reference.docx with book-style formatting.

Usage: python3 build/make_reference_docx.py build/reference.docx
"""
import subprocess
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt

out = sys.argv[1]
subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)

doc = Document(out)


class Styles:
    """Look up styles by their displayed name (pandoc uses 'Heading 1', which
    python-docx's built-in name translation does not find)."""

    def __init__(self, raw):
        self.raw = raw
        self.by_name = {st.name: st for st in raw}

    def __contains__(self, name):
        return name in self.by_name

    def __getitem__(self, name):
        return self.by_name[name]

    def add_style(self, *args):
        st = self.raw.add_style(*args)
        self.by_name[st.name] = st
        return st


styles = Styles(doc.styles)

BODY_FONT = "Georgia"

def font(style, size=None, italic=None, bold=None, name=BODY_FONT):
    style.font.name = name
    if size:
        style.font.size = Pt(size)
    if italic is not None:
        style.font.italic = italic
    if bold is not None:
        style.font.bold = bold

for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    if name in styles:
        st = styles[name]
        font(st, 11.5)
        pf = st.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = 1.25

styles["Body Text"].paragraph_format.first_line_indent = Inches(0)
styles["Body Text"].paragraph_format.space_after = Pt(6)
styles["First Paragraph"].paragraph_format.first_line_indent = Inches(0)

h1 = styles["Heading 1"]
font(h1, 20, bold=False)
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h1.paragraph_format.page_break_before = True
h1.paragraph_format.space_before = Pt(72)
h1.paragraph_format.space_after = Pt(30)

h2 = styles["Heading 2"]
font(h2, 12.5, bold=False)
h2.font.bold = True
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h2.paragraph_format.space_before = Pt(24)
h2.paragraph_format.space_after = Pt(12)

for name in ("Heading 1", "Heading 2"):
    styles[name].font.color.rgb = None

bt = styles["Block Text"]
font(bt, 12, italic=True)
bt.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
bt.paragraph_format.left_indent = Inches(0.4)
bt.paragraph_format.right_indent = Inches(0.4)
bt.paragraph_format.space_before = Pt(12)
bt.paragraph_format.space_after = Pt(12)

for name, size, italic in (("Title", 28, False), ("Subtitle", 15, True), ("Author", 13, False)):
    if name in styles:
        st = styles[name]
        font(st, size, italic=italic, bold=False)
        st.font.color.rgb = None
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

from docx.enum.style import WD_STYLE_TYPE
sb = styles.add_style("Scene Break", WD_STYLE_TYPE.PARAGRAPH)
sb.base_style = styles["Normal"]
sb.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
sb.paragraph_format.first_line_indent = Inches(0)
sb.paragraph_format.space_before = Pt(12)
sb.paragraph_format.space_after = Pt(12)

for sname, mono in (("Box Text", False), ("Prompt Text", True), ("Session Text", False)):
    st = styles.add_style(sname, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = styles["Normal"]
    st.paragraph_format.left_indent = Inches(0.3)
    st.paragraph_format.right_indent = Inches(0.2)
    st.paragraph_format.first_line_indent = Inches(0)
    st.paragraph_format.space_after = Pt(4)
    if mono:
        st.font.name = "Courier New"
        st.font.size = Pt(9.5)

h3 = styles["Heading 3"]
font(h3, 11.5, italic=True, bold=True)
h3.font.color.rgb = None

doc.save(out)
print("wrote", out)
