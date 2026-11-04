-- Format tweaks for The After-Five Business.
--   EPUB/HTML: copyright and dedication headings are kept (needed to split
--   files) and hidden with CSS.
--   DOCX: those headings become page breaks; boxes, prompts and session
--   panels get custom paragraph styles from reference.docx.
local hidden = { copyright = true, dedication = true }
local divstyle = { box = "Box Text", prompt = "Prompt Text", session = "Session Text" }

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
  if not FORMAT:match("docx") then return nil end
  for _, c in ipairs(el.classes) do
    if divstyle[c] then
      el.attributes["custom-style"] = divstyle[c]
      return el
    end
  end
  return nil
end
