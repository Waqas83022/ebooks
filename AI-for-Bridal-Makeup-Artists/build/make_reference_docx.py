"""Create a pandoc reference.docx with nonfiction book formatting.

Usage: python3 build/make_reference_docx.py build/reference.docx
"""
import subprocess
import sys

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

out = sys.argv[1]
subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)
doc = Document(out)
by_name = {st.name: st for st in doc.styles}
BODY = "Georgia"
INK = RGBColor(0x2B, 0x22, 0x30)


def font(st, size=None, italic=None, bold=None, name=BODY, color=None):
    st.font.name = name
    if size:
        st.font.size = Pt(size)
    if italic is not None:
        st.font.italic = italic
    if bold is not None:
        st.font.bold = bold
    st.font.color.rgb = color


def shade(st, fill, border=None):
    ppr = st.element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    ppr.append(shd)
    if border:
        bdr = OxmlElement("w:pBdr")
        for side in ("top", "left", "bottom", "right"):
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "8")
            b.set(qn("w:space"), "6")
            b.set(qn("w:color"), border)
            bdr.append(b)
        ppr.append(bdr)


for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    if name in by_name:
        st = by_name[name]
        font(st, 11)
        pf = st.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(8)
        pf.line_spacing = 1.2
        pf.first_line_indent = Inches(0)
by_name["Compact"].paragraph_format.space_after = Pt(3)

for name, size, before, after in (("Heading 1", 22, 48, 18), ("Heading 2", 14, 18, 6), ("Heading 3", 12, 12, 4)):
    st = by_name[name]
    font(st, size, bold=True, italic=False, color=INK)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    st.paragraph_format.space_before = Pt(before)
    st.paragraph_format.space_after = Pt(after)
    st.paragraph_format.keep_with_next = True
by_name["Heading 1"].paragraph_format.page_break_before = True

bt = by_name["Block Text"]
font(bt, 11, italic=False)
bt.paragraph_format.left_indent = Inches(0.3)
bt.paragraph_format.right_indent = Inches(0.2)
bt.paragraph_format.space_after = Pt(6)
shade(bt, "F8F1EF")

for nm, fill, border in (("Prompt Box", "F1ECEF", "2B2230"), ("Template Box", "FFFFFF", "2B2230"), ("Checklist Box", "FAF5EC", "9A7440")):
    st = doc.styles.add_style(nm, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = by_name["Body Text"]
    st.font.size = Pt(10.5)
    st.paragraph_format.left_indent = Inches(0.15)
    st.paragraph_format.right_indent = Inches(0.15)
    st.paragraph_format.space_after = Pt(4)
    shade(st, fill, border)

for name, size, italic in (("Title", 28, False), ("Subtitle", 14, True), ("Author", 13, False)):
    if name in by_name:
        st = by_name[name]
        font(st, size, italic=italic, bold=False, color=INK)
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

for name in ("Image Caption", "Caption"):
    if name in by_name:
        font(by_name[name], 9.5, italic=True)
        by_name[name].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save(out)
print("wrote", out)
