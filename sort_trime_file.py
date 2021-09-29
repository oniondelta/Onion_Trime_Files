
import os
import shutil
import time

#※新增資料夾(多層目錄, 如前一層data資料夾不存在, 將自動新增)※
os.makedirs('./sort_trime/洋蔥同文注音純注音版/opencc/', exist_ok=True)
os.makedirs('./sort_trime/洋蔥同文注音雙拼版/opencc/', exist_ok=True)
os.makedirs('./sort_trime/洋蔥同文注音plus版/opencc/', exist_ok=True)
os.makedirs('./sort_trime/洋蔥同文注音mixin版/opencc/', exist_ok=True)
os.makedirs('./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/', exist_ok=True)
os.makedirs('./sort_trime/洋蔥手機蝦/ocm_plus/opencc/', exist_ok=True)


#複製檔案(洋蔥同文注音純注音版)
shutil.copyfile("./trimefiles/essay-zh-hant-onion.txt", "./sort_trime/洋蔥同文注音純注音版/essay-zh-hant-onion.txt")

shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobile.schema.yaml", "./sort_trime/洋蔥同文注音純注音版/bpmfmobile.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./sort_trime/洋蔥同文注音純注音版/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音純注音版/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/phrases.chtp.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./sort_trime/洋蔥同文注音純注音版/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥同文注音純注音版/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音純注音版/sy_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./sort_trime/洋蔥同文注音純注音版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/洋蔥注音_H.trime.yaml", "./sort_trime/洋蔥同文注音純注音版/洋蔥注音_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_L.trime.yaml", "./sort_trime/洋蔥同文注音純注音版/洋蔥注音_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_M.trime.yaml", "./sort_trime/洋蔥同文注音純注音版/洋蔥注音_M.trime.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥同文注音純注音版/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥同文注音純注音版/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥同文注音純注音版/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥同文注音純注音版/opencc/emoji_s.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥同文注音純注音版/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥同文注音純注音版/opencc/punct_mark_t.txt")


#複製檔案(洋蔥同文注音雙拼版版)
shutil.copyfile("./trimefiles/essay-zh-hant-onion.txt", "./sort_trime/洋蔥同文注音雙拼版/essay-zh-hant-onion.txt")

shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobiledouble.schema.yaml", "./sort_trime/洋蔥同文注音雙拼版/bpmfmobiledouble.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/phrases.chtp.dict.yaml")

shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥同文注音雙拼版/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音雙拼版/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_d_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音雙拼版/sy_d_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/洋蔥注音_H.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥注音_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_L.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥注音_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_M.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥注音_M.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥雙拼注音_H.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥雙拼注音_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥雙拼注音_L.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥雙拼注音_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥雙拼注音_M.trime.yaml", "./sort_trime/洋蔥同文注音雙拼版/洋蔥雙拼注音_M.trime.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥同文注音雙拼版/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥同文注音雙拼版/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥同文注音雙拼版/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥同文注音雙拼版/opencc/emoji_s.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥同文注音雙拼版/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥同文注音雙拼版/opencc/punct_mark_t.txt")


#複製檔案(洋蔥同文注音mixin版)
shutil.copyfile("./trimefiles/essay-zh-hant-onion.txt", "./sort_trime/洋蔥同文注音mixin版/essay-zh-hant-onion.txt")

shutil.copyfile("./trimefiles/bo_mixin_jp.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/bo_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/bo_mixin_kr.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_la.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/bo_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin.extended.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/bo_mixin.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin2.schema.yaml", "./sort_trime/洋蔥同文注音mixin版/bpmfmobilemixin2.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixins.schema.yaml", "./sort_trime/洋蔥同文注音mixin版/bpmfmobilemixins.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin4.schema.yaml", "./sort_trime/洋蔥同文注音mixin版/bpmfmobilemixin4.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./sort_trime/洋蔥同文注音mixin版/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音mixin版/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkreduce.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.jp_hkkreduce.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/phrases.la_py_w.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./sort_trime/洋蔥同文注音mixin版/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥同文注音mixin版/rime.lua")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/洋蔥注音_H.trime.yaml", "./sort_trime/洋蔥同文注音mixin版/洋蔥注音_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_L.trime.yaml", "./sort_trime/洋蔥同文注音mixin版/洋蔥注音_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_M.trime.yaml", "./sort_trime/洋蔥同文注音mixin版/洋蔥注音_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音mixin版/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音mixin版/sy_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./sort_trime/洋蔥同文注音mixin版/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_t.txt", "./sort_trime/洋蔥同文注音mixin版/opencc/back_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥同文注音mixin版/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥同文注音mixin版/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥同文注音mixin版/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥同文注音mixin版/opencc/emoji_s.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥同文注音mixin版/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥同文注音mixin版/opencc/punct_mark_t.txt")


#複製檔案(洋蔥同文注音plus版)
shutil.copyfile("./trimefiles/essay-zh-hant-onion.txt", "./sort_trime/洋蔥同文注音plus版/essay-zh-hant-onion.txt")
shutil.copyfile("./trimefiles/essay-jp-onion.txt", "./sort_trime/洋蔥同文注音plus版/essay-jp-onion.txt")

shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./sort_trime/洋蔥同文注音plus版/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobileplus.schema.yaml", "./sort_trime/洋蔥同文注音plus版/bpmfmobileplus.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./sort_trime/洋蔥同文注音plus版/element_bpmf.yaml")
shutil.copyfile("./trimefiles/hangeul.dict.yaml", "./sort_trime/洋蔥同文注音plus版/hangeul.dict.yaml")
shutil.copyfile("./trimefiles/hangeul.extended.dict.yaml", "./sort_trime/洋蔥同文注音plus版/hangeul.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul.schema.yaml", "./sort_trime/洋蔥同文注音plus版/hangeul.schema.yaml")
shutil.copyfile("./trimefiles/jpnin1.dict.yaml", "./sort_trime/洋蔥同文注音plus版/jpnin1.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.extended.dict.yaml", "./sort_trime/洋蔥同文注音plus版/jpnin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.schema.yaml", "./sort_trime/洋蔥同文注音plus版/jpnin1.schema.yaml")
shutil.copyfile("./trimefiles/jpnin1.custom.yaml", "./sort_trime/洋蔥同文注音plus版/jpnin1.custom.yaml")
shutil.copyfile("./trimefiles/latinin1.dict.yaml", "./sort_trime/洋蔥同文注音plus版/latinin1.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.extended.dict.yaml", "./sort_trime/洋蔥同文注音plus版/latinin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.schema.yaml", "./sort_trime/洋蔥同文注音plus版/latinin1.schema.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音plus版/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音plus版/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkseg.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hkkseg.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkup_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hkup_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkmoreup_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.jp_hkmoreup_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./sort_trime/洋蔥同文注音plus版/phrases.la_py_w.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./sort_trime/洋蔥同文注音plus版/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥同文注音plus版/rime.lua")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./sort_trime/洋蔥同文注音plus版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./sort_trime/洋蔥同文注音plus版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/洋蔥注音_H.trime.yaml", "./sort_trime/洋蔥同文注音plus版/洋蔥注音_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_L.trime.yaml", "./sort_trime/洋蔥同文注音plus版/洋蔥注音_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥注音_M.trime.yaml", "./sort_trime/洋蔥同文注音plus版/洋蔥注音_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./sort_trime/洋蔥同文注音plus版/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./sort_trime/洋蔥同文注音plus版/sy_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./sort_trime/洋蔥同文注音plus版/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_t.txt", "./sort_trime/洋蔥同文注音plus版/opencc/back_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥同文注音plus版/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥同文注音plus版/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥同文注音plus版/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥同文注音plus版/opencc/emoji_s.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥同文注音plus版/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥同文注音plus版/opencc/punct_mark_t.txt")


#複製檔案(洋蔥手機蝦-mixin)
shutil.copyfile("./trimefiles/ocm_mixin_jp.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_kr.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_la.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ocm_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile.extended.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ovffmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ovffmobile.schema.yaml")
shutil.copyfile("./trimefiles/punct_ovff.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/punct_ovff.yaml")
shutil.copyfile("./trimefiles/element_ovff.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/element_ovff.yaml")
shutil.copyfile("./trimefiles/punt_ocm.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/punt_ocm.dict.yaml")
shutil.copyfile("./trimefiles/punt_ocm.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/punt_ocm.schema.yaml")

shutil.copyfile("./trimefiles/phrases.ocmtc_terra.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.ocmtc_terra.dict.yaml")
shutil.copyfile("./trimefiles/phrases.ocmtc_essay_new_m.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.ocmtc_essay_new_m.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/phrases.en_u_w.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥手機蝦/ocm_mixin/rime.lua")
shutil.copyfile("./trimefiles/ocm_tc_m.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/ocm_tc_m.dict.yaml")
shutil.copyfile("./trimefiles/uniabcdword.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/uniabcdword.dict.yaml")

shutil.copyfile("./trimefiles/洋蔥蝦米_H.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/洋蔥蝦米_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥蝦米_L.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/洋蔥蝦米_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥蝦米_M.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/洋蔥蝦米_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_ocm.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/sy_ocm.dict.yaml")
shutil.copyfile("./trimefiles/sy_ocm.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_mixin/sy_ocm.schema.yaml")

shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/ocm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/ocm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_t.txt", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/back_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥手機蝦/ocm_mixin/opencc/emoji_s.txt")


#複製檔案(洋蔥手機蝦-plus)
shutil.copyfile("./trimefiles/omp_jp.extended.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_jp.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_jphi.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_jphi.schema.yaml")
shutil.copyfile("./trimefiles/omp_jpka.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_jpka.schema.yaml")
shutil.copyfile("./trimefiles/omp_kr.extended.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_kr.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_kr.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_kr.schema.yaml")
shutil.copyfile("./trimefiles/omp_la.extended.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_la.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_la.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/omp_la.schema.yaml")

shutil.copyfile("./trimefiles/ocm_mixin_jp.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_kr.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_la.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ocm_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile_plus.extended.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ovffmobile_plus.extended.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile_plus.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ovffmobile_plus.schema.yaml")
shutil.copyfile("./trimefiles/punct_ovff.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/punct_ovff.yaml")
shutil.copyfile("./trimefiles/element_ovff.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/element_ovff.yaml")
shutil.copyfile("./trimefiles/punt_ocm.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/punt_ocm.dict.yaml")
shutil.copyfile("./trimefiles/punt_ocm.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/punt_ocm.schema.yaml")

shutil.copyfile("./trimefiles/phrases.ocmtc_terra.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.ocmtc_terra.dict.yaml")
shutil.copyfile("./trimefiles/phrases.ocmtc_essay_new_m.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.ocmtc_essay_new_m.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/phrases.en_u_w.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./sort_trime/洋蔥手機蝦/ocm_plus/rime.lua")
shutil.copyfile("./trimefiles/ocm_tc_m.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/ocm_tc_m.dict.yaml")
shutil.copyfile("./trimefiles/uniabcdword.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/uniabcdword.dict.yaml")

shutil.copyfile("./trimefiles/洋蔥蝦米_H.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/洋蔥蝦米_H.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥蝦米_L.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/洋蔥蝦米_L.trime.yaml")
shutil.copyfile("./trimefiles/洋蔥蝦米_M.trime.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/洋蔥蝦米_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_ocm.dict.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/sy_ocm.dict.yaml")
shutil.copyfile("./trimefiles/sy_ocm.schema.yaml", "./sort_trime/洋蔥手機蝦/ocm_plus/sy_ocm.schema.yaml")

shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.json", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/ocm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.txt", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/ocm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_t.txt", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/back_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/emoji_s.json", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/emoji_s.json")
shutil.copyfile("./trimefiles/opencc/emoji_s.txt", "./sort_trime/洋蔥手機蝦/ocm_plus/opencc/emoji_s.txt")


#實體(藍牙)鍵盤專用
shutil.copytree('./trimefiles/實體(藍牙)鍵盤專用/', './sort_trime/實體(藍牙)鍵盤專用/')


#舊312版主程式
shutil.copytree('./trimefiles/舊312版主程式/', './sort_trime/舊312版主程式/')


#OpenCC_ocd_64位元
shutil.copytree('./trimefiles/OpenCC_ocd_64位元/', './sort_trime/OpenCC_ocd_64位元/')


#font字型
shutil.copytree('./trimefiles/fonts/', './sort_trime/fonts/')


#名稱增加日期
localtime=time.strftime("%Y%m%d", time.localtime())

os.rename('./sort_trime/洋蔥同文注音純注音版/', './sort_trime/洋蔥同文注音純注音版_'+localtime)
os.rename('./sort_trime/洋蔥同文注音雙拼版/', './sort_trime/洋蔥同文注音雙拼版_'+localtime)
os.rename('./sort_trime/洋蔥同文注音mixin版/', './sort_trime/洋蔥同文注音mixin版_'+localtime)
os.rename('./sort_trime/洋蔥同文注音plus版/', './sort_trime/洋蔥同文注音plus版_'+localtime)

os.rename('./sort_trime/洋蔥手機蝦/ocm_plus/', './sort_trime/洋蔥手機蝦/ocm_plus_'+localtime)
os.rename('./sort_trime/洋蔥手機蝦/ocm_mixin/', './sort_trime/洋蔥手機蝦/ocm_mixin_'+localtime)
os.rename('./sort_trime/洋蔥手機蝦/', './sort_trime/洋蔥手機蝦_'+localtime)

os.rename('./sort_trime/', './洋蔥手機同文方案_'+localtime)

