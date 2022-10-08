--- @@ charset_filter2
--[[
（ocm_onionmix）（手機全方案會用到）
把 opencc 轉換成「᰼」(或某個符號)，再用 lua 功能去除「᰼」
--]]

-- charset2 = {
--  ["Deletesymbol"] = { first = 0x1C3C } }

-- function exists2(single_filter2, text)
--   for i in utf8.codes(text) do
--    local c = utf8.codepoint(text, i)
--    if (not single_filter2(c)) then
--   return false
--    end
--   end
--   return true
-- end

-- function is_charset2(s)
--  return function (c)
--     return c == charset2[s].first
--  end
-- end

-- function is_symbol_ext(c)
--  return is_charset2("Deletesymbol")(c)
-- end

-- function charset_filter2(input)
--  for cand in input:iter() do
--     if (not exists2(is_symbol_ext, cand.text))
--     then
--     yield(cand)
--     end
--  end
-- end

function charset_filter2(input, env)
  local c_f2_s = env.engine.context:get_option("character_range_bhjm")
  if (c_f2_s) then
    for cand in input:iter() do
      if (not string.find(cand.text, '᰼᰼' )) then
      -- if (not string.find(cand.text, '.*᰼᰼.*' )) then
        yield(cand)
      end
    end
  else
    for cand in input:iter() do
      yield(cand)
    end
    -- if (input == nil) then
    --   cand = nil
    -- end
  end
  -- return nil
end




-- --- @@ mobile_bpmf
-- --[[
-- （手機注音用）
-- 使 email_url_translator 功能按空白都能直接上屏
-- --]]
function mobile_bpmf(key, env)
  local engine = env.engine
  local context = engine.context
  local input_m = context.input
  local orig_m = context:get_commit_text()
  if context:get_option('ascii_mode') then
    return 2
  elseif (not context:is_composing()) then
    return 2
  elseif (key:repr() == "space") then
    -- local input_m = context.input
    if (string.find(input_m, "^[a-z][-_.0-9a-z]*@.*$")) or (string.find(input_m, "^https?:.*$")) or (string.find(input_m, "^ftp:.*$")) or (string.find(input_m, "^mailto:.*$")) or (string.find(input_m, "^file:.*$")) then
    -- if ( string.find(input_m, "[@:]")) then
      -- local orig_m = context:get_commit_text()
      engine:commit_text(orig_m)
      context:clear()
      return 1 -- kAccepted
    end
  end
  return 2 -- kNoop
end




--- @@ email_url_translator
--[[
把 recognizer 正則輸入 email 使用 lua 實現，使之有選項，避免設定空白清屏時無法上屏。
把 recognizer 正則輸入網址使用 lua 實現，使之有選項，避免設定空白清屏時無法上屏。
--]]
function email_url_translator(input, seg)
  local email_in = string.match(input, "^([a-z][-_.0-9a-z]*@.*)$")
  local url1_in = string.match(input, "^(https?:.*)$")
  local url2_in = string.match(input, "^(ftp:.*)$")
  local url3_in = string.match(input, "^(mailto:.*)$")
  local url4_in = string.match(input, "^(file:.*)$")
  if (url1_in~=nil) or (url2_in~=nil) or (url3_in~=nil) or (url4_in~=nil) then
    yield(Candidate("englishtype", seg.start, seg._end, input , "〔URL〕"))
    return
  end
  if (email_in~=nil) then
    yield(Candidate("englishtype", seg.start, seg._end, email_in , "〔e-mail〕"))
    return
  end
end


--- @@ email_urlw_translator
--[[
把 recognizer 正則輸入網址使用 lua 實現，使之有選項，避免設定空白清屏時無法上屏。
該項多加「www.」
--]]
function email_urlw_translator(input, seg)
  local email_in = string.match(input, "^([a-z][-_.0-9a-z]*@.*)$")
  local www_in = string.match(input, "^(www[.][-_0-9a-z]*[-_.0-9a-z]*)$")
  local url1_in = string.match(input, "^(https?:.*)$")
  local url2_in = string.match(input, "^(ftp:.*)$")
  local url3_in = string.match(input, "^(mailto:.*)$")
  local url4_in = string.match(input, "^(file:.*)$")
  if (www_in~=nil) or (url1_in~=nil) or (url2_in~=nil) or (url3_in~=nil) or (url4_in~=nil) then
    yield(Candidate("englishtype", seg.start, seg._end, input , "〔URL〕"))
    return
  end
  if (email_in~=nil) then
    yield(Candidate("englishtype", seg.start, seg._end, email_in , "〔e-mail〕"))
    return
  end
end
