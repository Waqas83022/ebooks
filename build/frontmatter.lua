-- Format tweaks for the copyright, dedication and epigraph pages and scene breaks.
--   EPUB: headings are kept (needed to split files) and hidden with CSS.
--   HTML (proof PDF): headings are kept for section classes and hidden with CSS.
--   DOCX: headings are replaced by a page break.
local hidden = { copyright = true, dedication = true, epigraph = true }

function Header(el)
  if not FORMAT:match("docx") then return nil end
  if el.level == 1 then
    for _, c in ipairs(el.classes) do
      if hidden[c] then
        return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
      end
    end
  end
  return nil
end

-- Scene breaks ("* * *" in the manuscript).
function HorizontalRule()
  if FORMAT:match("docx") then
    local para = pandoc.Para({ pandoc.Str("*"), pandoc.Space(), pandoc.Str("*"), pandoc.Space(), pandoc.Str("*") })
    return pandoc.Div({ para }, pandoc.Attr("", {}, { { "custom-style", "Scene Break" } }))
  elseif FORMAT:match("html") then
    return pandoc.RawBlock("html", '<p class="scenebreak">*&#160;&#160;&#160;*&#160;&#160;&#160;*</p>')
  end
  return nil
end
