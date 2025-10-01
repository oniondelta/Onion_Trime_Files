
import os
import shutil
import time


#名稱(取出來較好變換)
sort_trime="sort_trime"
trime_files_1="洋蔥同文注音純注音版"
trime_files_2="洋蔥同文注音plus版"
trime_files_3="洋蔥同文注音mixin版"
trime_files_4="洋蔥同文注音雙拼版"
trime_ocm_folder="洋蔥手機蝦"
trime_files_5=trime_ocm_folder+"/ocm_plus"
trime_files_6=trime_ocm_folder+"/ocm_mixin"
the_name="洋蔥手機同文方案"


#※新增資料夾(多層目錄, 如前一層data資料夾不存在, 將自動新增)※
os.makedirs("./"+sort_trime+"/"+trime_files_1+"/opencc/", exist_ok=True)
os.makedirs("./"+sort_trime+"/"+trime_files_2+"/opencc/", exist_ok=True)
os.makedirs("./"+sort_trime+"/"+trime_files_3+"/opencc/", exist_ok=True)
os.makedirs("./"+sort_trime+"/"+trime_files_4+"/opencc/", exist_ok=True)
os.makedirs("./"+sort_trime+"/"+trime_files_5+"/opencc/", exist_ok=True)
os.makedirs("./"+sort_trime+"/"+trime_files_6+"/opencc/", exist_ok=True)


#複製檔案(洋蔥同文注音純注音版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc.txt", "./"+sort_trime+"/"+trime_files_1+"/essay-zh-hant-mc.txt")

shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobile.schema.yaml", "./"+sort_trime+"/"+trime_files_1+"/bpmfmobile.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./"+sort_trime+"/"+trime_files_1+"/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_1+"/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/phrases.chtp.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./"+sort_trime+"/"+trime_files_1+"/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_1+"/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_1+"/sy_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./"+sort_trime+"/"+trime_files_1+"/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_1+"/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_1+"/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_1+"/洋蔥注音331k_M.trime.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_1+"/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_1+"/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_1+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_1+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_1+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_1+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_1+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_1+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_1+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_1+"/opencc/back_mark_table_t.txt")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_1+"/predict_office.db")


#複製檔案(洋蔥同文注音plus版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc.txt", "./"+sort_trime+"/"+trime_files_2+"/essay-zh-hant-mc.txt")
shutil.copyfile("./trimefiles/essay-jp-onion.txt", "./"+sort_trime+"/"+trime_files_2+"/essay-jp-onion.txt")
shutil.copyfile("./trimefiles/essay-kr-hanja.txt", "./"+sort_trime+"/"+trime_files_2+"/essay-kr-hanja.txt")

shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobileplus.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/bpmfmobileplus.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./"+sort_trime+"/"+trime_files_2+"/element_bpmf.yaml")
shutil.copyfile("./trimefiles/hangeul_m.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hanja.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_hanja.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_m.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_hnc_m.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_hnc_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_hanja.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/hangeul_hnc_hanja.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/jpnin1.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1_hw.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/jpnin1_hw.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/jpnin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/jpnin1.schema.yaml")
shutil.copyfile("./trimefiles/latinin1.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/latinin1.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/latinin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/latinin1.schema.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkseg.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hkkseg.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkup_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hkup_w.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkmoreup_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.jp_hkmoreup_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/phrases.la_eu_w.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./"+sort_trime+"/"+trime_files_2+"/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_2+"/rime.lua")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_2+"/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_2+"/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_2+"/洋蔥注音331k_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_2+"/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_2+"/sy_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_2+"/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_2+"/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_2+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_2+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_2+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_2+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_2+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_2+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_2+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_2+"/opencc/back_mark_table_t.txt")

# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1只出假名修改檔/", "./"+sort_trime+"/"+trime_files_2+"/手機jpnin1只出假名修改檔/")
# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1精簡轉寫修改檔/", "./"+sort_trime+"/"+trime_files_2+"/手機jpnin1精簡轉寫修改檔/")
shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/", "./"+sort_trime+"/"+trime_files_2+"/custom檔_日語jpnin1精簡/")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_2+"/predict_office.db")


#複製檔案(洋蔥同文注音mixin版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc-mixin.txt", "./"+sort_trime+"/"+trime_files_3+"/essay-zh-hant-mc-mixin.txt")

shutil.copyfile("./trimefiles/bo_mixin_jp.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_m.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin_kr_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_hnc_m.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin_kr_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_la.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_en.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin_en.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/bo_mixin.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin2.schema.yaml", "./"+sort_trime+"/"+trime_files_3+"/bpmfmobilemixin2.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixins.schema.yaml", "./"+sort_trime+"/"+trime_files_3+"/bpmfmobilemixins.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin4.schema.yaml", "./"+sort_trime+"/"+trime_files_3+"/bpmfmobilemixin4.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./"+sort_trime+"/"+trime_files_3+"/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_3+"/mobile_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkreduce.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.jp_hkkreduce.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/phrases.la_eu_w.dict.yaml")

shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./"+sort_trime+"/"+trime_files_3+"/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_3+"/rime.lua")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_3+"/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_3+"/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_3+"/洋蔥注音331k_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_3+"/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_3+"/sy_bpmf.schema.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_3+"/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_3+"/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_3+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_3+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_3+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_3+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_3+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_3+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_3+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_3+"/opencc/back_mark_table_t.txt")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_3+"/predict_office.db")


#複製檔案(洋蔥同文注音雙拼版版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc.txt", "./"+sort_trime+"/"+trime_files_4+"/essay-zh-hant-mc.txt")

shutil.copyfile("./trimefiles/bpmfmobiledouble.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/bpmfmobiledouble.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobiledouble.schema.yaml", "./"+sort_trime+"/"+trime_files_4+"/bpmfmobiledouble.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobiledouble_t2.schema.yaml", "./"+sort_trime+"/"+trime_files_4+"/bpmfmobiledouble_t2.schema.yaml")

shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/phrases.chtp.dict.yaml")

shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./trimefiles/mixin_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/mixin_bpmf.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_4+"/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files_4+"/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_d_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files_4+"/sy_d_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/element_d_bpmfmobiledouble.yaml", "./"+sort_trime+"/"+trime_files_4+"/element_d_bpmfmobiledouble.yaml")
shutil.copyfile("./trimefiles/punct_d_bpmf.yaml", "./"+sort_trime+"/"+trime_files_4+"/punct_d_bpmf.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥注音331k_M.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥雙拼注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥雙拼注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_4+"/洋蔥雙拼注音331k_M.trime.yaml")

shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_4+"/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_4+"/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_4+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_4+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_4+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_4+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_4+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_4+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_4+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_4+"/opencc/back_mark_table_t.txt")

# shutil.copytree("./trimefiles/custom檔_手機注音雙拼不開頭簡拼/", "./"+sort_trime+"/"+trime_files_4+"/custom檔_手機注音雙拼不開頭簡拼/")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_4+"/predict_office.db")


#複製檔案(洋蔥手機蝦-plus)
shutil.copyfile("./trimefiles/omp_jp.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_jp.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_jphi.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_jphi.schema.yaml")
shutil.copyfile("./trimefiles/omp_jpka.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_jpka.schema.yaml")
shutil.copyfile("./trimefiles/omp_kr.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_kr.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_kr.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_kr.schema.yaml")
shutil.copyfile("./trimefiles/omp_la.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_la.extended.dict.yaml")
shutil.copyfile("./trimefiles/omp_la.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/omp_la.schema.yaml")

shutil.copyfile("./trimefiles/ocm_mixin_jp.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_kr.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_la.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/ocm_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile_plus.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/ovffmobile_plus.extended.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile_plus.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/ovffmobile_plus.schema.yaml")
shutil.copyfile("./trimefiles/punct_ovff.yaml", "./"+sort_trime+"/"+trime_files_5+"/punct_ovff.yaml")
shutil.copyfile("./trimefiles/element_ovff.yaml", "./"+sort_trime+"/"+trime_files_5+"/element_ovff.yaml")
shutil.copyfile("./trimefiles/punt_ocm.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/punt_ocm.dict.yaml")
shutil.copyfile("./trimefiles/punt_ocm.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/punt_ocm.schema.yaml")

shutil.copyfile("./trimefiles/phrases.ocmtc_essay_mc.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.ocmtc_essay_mc.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.la_eu_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/phrases.en_u_w.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_5+"/rime.lua")
shutil.copyfile("./trimefiles/ocm_tc_mc_m.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/ocm_tc_mc_m.dict.yaml")
shutil.copyfile("./trimefiles/uniabcdword.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/uniabcdword.dict.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_5+"/洋蔥蝦米331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_5+"/洋蔥蝦米331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_5+"/洋蔥蝦米331k_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_ocm.dict.yaml", "./"+sort_trime+"/"+trime_files_5+"/sy_ocm.dict.yaml")
shutil.copyfile("./trimefiles/sy_ocm.schema.yaml", "./"+sort_trime+"/"+trime_files_5+"/sy_ocm.schema.yaml")

shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_5+"/opencc/ocm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_5+"/opencc/ocm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_5+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_5+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_5+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_5+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_5+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_5+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_5+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_5+"/opencc/back_mark_table_t.txt")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_5+"/predict_office.db")


#複製檔案(洋蔥手機蝦-mixin)
shutil.copyfile("./trimefiles/ocm_mixin_jp.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_kr.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./trimefiles/ocm_mixin_la.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/ocm_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile.extended.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/ovffmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/ovffmobile.schema.yaml", "./"+sort_trime+"/"+trime_files_6+"/ovffmobile.schema.yaml")
shutil.copyfile("./trimefiles/punct_ovff.yaml", "./"+sort_trime+"/"+trime_files_6+"/punct_ovff.yaml")
shutil.copyfile("./trimefiles/element_ovff.yaml", "./"+sort_trime+"/"+trime_files_6+"/element_ovff.yaml")
shutil.copyfile("./trimefiles/punt_ocm.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/punt_ocm.dict.yaml")
shutil.copyfile("./trimefiles/punt_ocm.schema.yaml", "./"+sort_trime+"/"+trime_files_6+"/punt_ocm.schema.yaml")

shutil.copyfile("./trimefiles/phrases.ocmtc_essay_mc.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.ocmtc_essay_mc.dict.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.la_eu_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/phrases.en_u_w.dict.yaml")

shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files_6+"/rime.lua")
shutil.copyfile("./trimefiles/ocm_tc_mc_m.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/ocm_tc_mc_m.dict.yaml")
shutil.copyfile("./trimefiles/uniabcdword.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/uniabcdword.dict.yaml")

shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files_6+"/洋蔥蝦米331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files_6+"/洋蔥蝦米331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥蝦米331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files_6+"/洋蔥蝦米331k_M.trime.yaml")

shutil.copyfile("./trimefiles/sy_ocm.dict.yaml", "./"+sort_trime+"/"+trime_files_6+"/sy_ocm.dict.yaml")
shutil.copyfile("./trimefiles/sy_ocm.schema.yaml", "./"+sort_trime+"/"+trime_files_6+"/sy_ocm.schema.yaml")

shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files_6+"/opencc/ocm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/ocm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files_6+"/opencc/ocm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files_6+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files_6+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files_6+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files_6+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files_6+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files_6+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files_6+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files_6+"/opencc/back_mark_table_t.txt")

shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files_6+"/predict_office.db")


#實體(藍牙)鍵盤專用
shutil.copytree("./trimefiles/實體(藍牙)鍵盤專用/", "./"+sort_trime+"/實體(藍牙)鍵盤專用/")


#各版主程式
shutil.copytree("./trimefiles/各版主程式/", "./"+sort_trime+"/各版主程式/")


#適用3.2.1鍵盤檔
shutil.copytree("./trimefiles/3.2.1鍵盤檔/", "./"+sort_trime+"/3.2.1鍵盤檔/")
#適用3.2.8鍵盤檔
shutil.copytree("./trimefiles/3.2.8鍵盤檔/", "./"+sort_trime+"/3.2.8鍵盤檔/")
#適用3.2.14鍵盤檔
shutil.copytree("./trimefiles/3.2.14鍵盤檔/", "./"+sort_trime+"/3.2.14鍵盤檔/")
#適用3.3.1鍵盤檔
shutil.copytree("./trimefiles/3.3.1鍵盤檔/", "./"+sort_trime+"/3.3.1鍵盤檔/")


#初始化方案
shutil.copytree("./trimefiles/初始化方案/", "./"+sort_trime+"/初始化方案/")


#OpenCC_ocd_64位元
shutil.copytree("./trimefiles/OpenCC_ocd_64位元/", "./"+sort_trime+"/OpenCC_ocd_64位元/")


#font字型
shutil.copytree("./trimefiles/fonts/", "./"+sort_trime+"/fonts/")


#名稱增加日期
localtime=time.strftime("%Y%m%d", time.localtime())

os.rename("./"+sort_trime+"/"+trime_files_1+"/", "./"+sort_trime+"/"+trime_files_1+"_"+localtime)
os.rename("./"+sort_trime+"/"+trime_files_2+"/", "./"+sort_trime+"/"+trime_files_2+"_"+localtime)
os.rename("./"+sort_trime+"/"+trime_files_3+"/", "./"+sort_trime+"/"+trime_files_3+"_"+localtime)
os.rename("./"+sort_trime+"/"+trime_files_4+"/", "./"+sort_trime+"/"+trime_files_4+"_"+localtime)

os.rename("./"+sort_trime+"/"+trime_files_5+"/", "./"+sort_trime+"/"+trime_files_5+"_"+localtime)
os.rename("./"+sort_trime+"/"+trime_files_6+"/", "./"+sort_trime+"/"+trime_files_6+"_"+localtime)
os.rename("./"+sort_trime+"/"+trime_ocm_folder+"/", "./"+sort_trime+"/"+trime_ocm_folder+"_"+localtime)

os.rename("./"+sort_trime+"/", "./"+the_name+"_"+localtime)



