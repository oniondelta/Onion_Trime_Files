--- @@ predictor_m_filter
--[[
（all）
改進預測詞 predictor 用
預測詞首個候選項生成一個空選項，好快速明顯的關閉關聯詞。
--]]




-- -- local M={}
-- local function init(env)
-- -- function M.init(env)
-- end

-- function M.fini(env)
-- end

local function tags_match(seg, env)
  local engine = env.engine
  local context = engine.context
  local pd = context:get_option("prediction")
  local seg_pd = seg:has_tag("prediction")
  return pd and seg_pd
  -- return seg_pd
end

-- function M.func(inp, env)
-- local function predictor_m_filter(inp, env)
local function filter(inp, env)
  -- local engine = env.engine
  -- local context = engine.context
  -- local comp = context.composition
  -- local seg = comp:back()
  local pp = "\t《預測詞》"

  -- local first_cand = Candidate("prediction_first", seg.start, seg._end, "", "")
  local first_cand = Candidate("prediction_first", 0, 0, "", "")
  first_cand.preedit = pp
  yield(first_cand)

  for cand in inp:iter() do
    local cand_p = cand
    cand_p.preedit = pp
    yield(cand_p)
  end

end


----------------
-- return predictor_filter
return { func = filter, tags_match = tags_match }
-- return { init = init, func = filter, tags_match = tags_match }
-- return M
----------------