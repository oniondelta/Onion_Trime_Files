
import os
import shutil
import time

#※新增資料夾(多層目錄, 如前一層data資料夾不存在, 將自動新增)※
os.makedirs("./sort_trime_bpx4/trime﹤bpin1﹥/opencc/", exist_ok=True)


#複製檔案(洋蔥同文注音純注音版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/essay-zh-hant-mc.txt")
shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobile.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobile.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/mobile_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./sort_trime_bpx4/trime﹤bpin1﹥/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/sy_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥注音331k_M.trime.yaml")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/opencc/back_mark_table_t.txt")


#複製檔案(洋蔥同文注音plus版)
shutil.copyfile("./trimefiles/essay-jp-onion.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/essay-jp-onion.txt")
shutil.copyfile("./trimefiles/essay-kr-hanja.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/essay-kr-hanja.txt")
shutil.copyfile("./trimefiles/bpmfmobileplus.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobileplus.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_m.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hanja.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_hanja.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_m.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_hnc_m.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_hnc_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_hanja.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/hangeul_hnc_hanja.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/jpnin1.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1_hw.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/jpnin1_hw.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/jpnin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/jpnin1.schema.yaml")
shutil.copyfile("./trimefiles/latinin1.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/latinin1.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/latinin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/latinin1.schema.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkseg.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hkkseg.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkup_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hkup_w.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkmoreup_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hkmoreup_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.la_eu_w.dict.yaml")
# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1只出假名修改檔/", "./sort_trime_bpx4/trime﹤bpin1﹥/手機jpnin1只出假名修改檔/")
# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1精簡轉寫修改檔/", "./sort_trime_bpx4/trime﹤bpin1﹥/手機jpnin1精簡轉寫修改檔/")
shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/", "./sort_trime_bpx4/trime﹤bpin1﹥/custom檔_日語jpnin1精簡/")


#複製檔案(洋蔥同文注音mixin版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc-mixin.txt", "./sort_trime_bpx4/trime﹤bpin1﹥/essay-zh-hant-mc-mixin.txt")
shutil.copyfile("./trimefiles/bo_mixin_jp.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_m.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin_kr_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_hnc_m.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin_kr_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_la.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_en.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin_en.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bo_mixin.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin2.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobilemixin2.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixins.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobilemixins.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin4.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobilemixin4.schema.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkreduce.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/phrases.jp_hkkreduce.dict.yaml")


#複製檔案(洋蔥同文注音雙拼版版)
shutil.copyfile("./trimefiles/bpmfmobiledouble.extended.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobiledouble.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobiledouble.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/bpmfmobiledouble.schema.yaml")
shutil.copyfile("./trimefiles/mixin_bpmf.dict.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/mixin_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_d_bpmf.schema.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/sy_d_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/element_d_bpmfmobiledouble.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/element_d_bpmfmobiledouble.yaml")
shutil.copyfile("./trimefiles/punct_d_bpmf.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/punct_d_bpmf.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_H.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥雙拼注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_L.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥雙拼注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_M.trime.yaml", "./sort_trime_bpx4/trime﹤bpin1﹥/洋蔥雙拼注音331k_M.trime.yaml")
shutil.copytree("./trimefiles/custom檔_手機注音雙拼不開頭簡拼/", "./sort_trime_bpx4/trime﹤bpin1﹥/custom檔_手機注音雙拼不開頭簡拼/")


#實體(藍牙)鍵盤專用
shutil.copytree("./trimefiles/實體(藍牙)鍵盤專用/", "./sort_trime_bpx4/實體(藍牙)鍵盤專用/")


#各版主程式
shutil.copytree("./trimefiles/各版主程式/", "./sort_trime_bpx4/各版主程式/")


#適用3.2.1鍵盤檔
shutil.copytree("./trimefiles/3.2.1鍵盤檔/", "./sort_trime_bpx4/3.2.1鍵盤檔/")
#適用3.2.8鍵盤檔
shutil.copytree("./trimefiles/3.2.8鍵盤檔/", "./sort_trime_bpx4/3.2.8鍵盤檔/")
#適用3.2.14鍵盤檔
shutil.copytree("./trimefiles/3.2.14鍵盤檔/", "./sort_trime_bpx4/3.2.14鍵盤檔/")
#適用3.3.1鍵盤檔
shutil.copytree("./trimefiles/3.3.1鍵盤檔/", "./sort_trime_bpx4/3.3.1鍵盤檔/")


#初始化方案
shutil.copytree("./trimefiles/初始化方案/", "./sort_trime_bpx4/初始化方案/")


#OpenCC_ocd_64位元
shutil.copytree("./trimefiles/OpenCC_ocd_64位元/", "./sort_trime_bpx4/OpenCC_ocd_64位元/")


#font字型
shutil.copytree("./trimefiles/fonts/", "./sort_trime_bpx4/fonts/")


#名稱增加日期
localtime=time.strftime("%Y%m%d", time.localtime())

os.rename("./sort_trime_bpx4/trime﹤bpin1﹥/", "./sort_trime_bpx4/trime﹤bpin1﹥_"+localtime)

os.rename("./sort_trime_bpx4/", "./洋蔥手機同文方案﹤bpin1﹥_"+localtime)



