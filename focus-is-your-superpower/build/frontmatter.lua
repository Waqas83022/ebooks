-- Format tweaks.
--   Copyright and dedication headings: hidden with CSS in EPUB/HTML, replaced by a page break in DOCX.
--   Worksheet boxes (::: worksheet): styled with CSS in EPUB/HTML, a custom paragraph style in DOCX.
local hidden = { copyright = true, dedication = true }

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

function Div(el)
  if FORMAT:match("docx") and el.classes:includes("worksheet") then
    el.attributes["custom-style"] = "Worksheet Box"
    return el
  end
  return nil
end
