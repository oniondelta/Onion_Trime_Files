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
  local engine = env.engine
  local context = engine.context
  local c_f2_s = context:get_option("character_range_bhjm")
  if c_f2_s then
    for cand in input:iter() do
      if not string.match(cand.text, "᰼᰼" ) then
      -- if not string.match(cand.text, ".*᰼᰼.*" ) then
        yield(cand)
      end
    end
  else
    for cand in input:iter() do
      yield(cand)
    end
    -- if input == nil then
    --   cand = nil
    -- end
  end
  -- return nil
end




--- @@ mobile_bpmf
--[[
（手機注音用）
使 email_url_translator 功能按空白都能直接上屏
--]]

function mobile_bpmf(key, env)
-- local function processor(key, env)
  local engine = env.engine
  local context = engine.context
  local c_input = context.input
  local comp = context.composition
  local seg = comp:back()
  local g_c_t = context:get_commit_text()
  local o_ascii_mode = context:get_option("ascii_mode")
  -- local check_i1 = string.match(c_input, "^[a-z][-_.0-9a-z]*@.*$")
  -- local check_i2 = string.match(c_input, "^https?:.*$")
  -- local check_i3 = string.match(c_input, "^ftp:.*$")
  -- local check_i4 = string.match(c_input, "^mailto:.*$")
  -- local check_i5 = string.match(c_input, "^file:.*$")
  -- local check_i = string.match(c_input, "^[a-z][-_.0-9a-z]*@.*$") or
  --                 string.match(c_input, "^https?:.*$") or
  --                 string.match(c_input, "^ftp:.*$") or
  --                 string.match(c_input, "^mailto:.*$") or
  --                 string.match(c_input, "^file:.*$")

  -- if context:get_option("ascii_mode") then
  if o_ascii_mode then
    return 2
  elseif not context:is_composing() then
    return 2
  elseif key:repr() == "space" then
  -- if key:repr() == "space" and context:is_composing() then
    if seg:has_tag("email_url_translator") then
    -- if check_i then
    -- if check_i1 or check_i2 or check_i3 or check_i4 or check_i5 then
    -- if ( string.match(c_input, "[@:]")) then
      engine:commit_text(g_c_t)
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
可多加「www.」
--]]
-- local function init(env)
-- end

function email_url_translator(input, seg)
-- local function translate(input, seg)
  -- local www_in = string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$")
  -- local url1_in = string.match(input, "^https?:.*$")
  -- local url2_in = string.match(input, "^ftp:.*$")
  -- local url3_in = string.match(input, "^mailto:.*$")
  -- local url4_in = string.match(input, "^file:.*$")
  -- local www_url_in = string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$") or
  --                    string.match(input, "^https?:.*$") or
  --                    string.match(input, "^ftp:.*$") or
  --                    string.match(input, "^mailto:.*$") or
  --                    string.match(input, "^file:.*$")
  -- local url_in = string.match(input, "^https?:.*$") or
  --                string.match(input, "^ftp:.*$") or
  --                string.match(input, "^mailto:.*$") or
  --                string.match(input, "^file:.*$")
  -- local email_in = string.match(input, "^[a-z][-_.0-9a-z]*@.*$")

  -- local url_cand = Candidate("englishtype", seg.start, seg._end, input , "〔URL〕")
  -- local email_cand = Candidate("englishtype", seg.start, seg._end, input , "〔e-mail〕")

  if seg:has_tag("email_url_translator") then
    if not string.match(input, "@") then
    -- if string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$") or string.match(input, "^https?:.*$") or string.match(input, "^ftp:.*$") or string.match(input, "^mailto:.*$") or string.match(input, "^file:.*$") then
    -- if www_in or url1_in or url2_in or url3_in or url4_in then
    -- if www_url_in then
    -- if url_in then
      yield(Candidate("englishtype", seg.start, seg._end, input , "〔URL〕"))
      -- yield(url_cand)
      -- return
    -- end
    else
    -- elseif string.match(input, "^[a-z][-_.0-9a-z]*@.*$") then
    -- elseif email_in then
      yield(Candidate("englishtype", seg.start, seg._end, input , "〔e-mail〕"))
      -- yield(email_cand)
      -- return
    end
  end

end
