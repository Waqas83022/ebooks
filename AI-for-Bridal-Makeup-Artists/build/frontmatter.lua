-- Format tweaks for front matter, boxed prompts/templates/checklists and figures.
local hidden = { copyright = true, dedication = true }
local boxes = { prompt = "Prompt Box", template = "Template Box", checklist = "Checklist Box" }

function Header(el)
  if FORMAT:match("docx") and el.level == 1 then
    for _, c in ipairs(el.classes) do
      if hidden[c] then
        return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
      end
    end
  end
  return nil
end

function Div(el)
  if FORMAT:match("docx") then
    for _, c in ipairs(el.classes) do
      if boxes[c] then
        el.attributes["custom-style"] = boxes[c]
        return el
      end
    end
  end
  return nil
end
