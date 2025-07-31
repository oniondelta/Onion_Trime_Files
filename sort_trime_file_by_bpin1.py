
import os
import shutil
import time


#名稱(取出來較好變換)
sort_trime="sort_trime_bpx4"
trime_files="trime﹤bpin1﹥"
the_name="洋蔥手機同文方案﹤bpin1﹥"


#※新增資料夾(多層目錄, 如前一層data資料夾不存在, 將自動新增)※
os.makedirs("./"+sort_trime+"/"+trime_files+"/opencc/", exist_ok=True)


#複製檔案(洋蔥同文注音純注音版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc.txt", "./"+sort_trime+"/"+trime_files+"/essay-zh-hant-mc.txt")
shutil.copyfile("./trimefiles/bpmfmobile.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobile.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobile.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobile.schema.yaml")
shutil.copyfile("./trimefiles/element_bpmf.yaml", "./"+sort_trime+"/"+trime_files+"/element_bpmf.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files+"/mobile_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/mobile_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files+"/mobile_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/phrases.cht.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.cht.dict.yaml")
shutil.copyfile("./trimefiles/phrases.chtp.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.chtp.dict.yaml")
shutil.copyfile("./trimefiles/punct_bpmf.yaml", "./"+sort_trime+"/"+trime_files+"/punct_bpmf.yaml")
shutil.copyfile("./trimefiles/rime.lua", "./"+sort_trime+"/"+trime_files+"/rime.lua")
shutil.copyfile("./trimefiles/sy_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files+"/sy_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files+"/sy_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion_add.dict.yaml", "./"+sort_trime+"/"+trime_files+"/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./trimefiles/terra_pinyin_onion.dict.yaml", "./"+sort_trime+"/"+trime_files+"/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥注音331k_M.trime.yaml")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.json", "./"+sort_trime+"/"+trime_files+"/opencc/bpm_moedict_big5e_hkscs_jis.json")
shutil.copyfile("./trimefiles/opencc/bpm_moedict_big5e_hkscs_jis.txt", "./"+sort_trime+"/"+trime_files+"/opencc/bpm_moedict_big5e_hkscs_jis.txt")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.json", "./"+sort_trime+"/"+trime_files+"/opencc/emoji_t_m.json")
shutil.copyfile("./trimefiles/opencc/emoji_t_m.txt", "./"+sort_trime+"/"+trime_files+"/opencc/emoji_t_m.txt")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.json", "./"+sort_trime+"/"+trime_files+"/opencc/punct_mark_t.json")
shutil.copyfile("./trimefiles/opencc/punct_mark_t.txt", "./"+sort_trime+"/"+trime_files+"/opencc/punct_mark_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_t.json", "./"+sort_trime+"/"+trime_files+"/opencc/back_mark_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_series_t.json", "./"+sort_trime+"/"+trime_files+"/opencc/back_mark_series_t.json")
shutil.copyfile("./trimefiles/opencc/back_mark_script_t.txt", "./"+sort_trime+"/"+trime_files+"/opencc/back_mark_script_t.txt")
shutil.copyfile("./trimefiles/opencc/back_mark_table_t.txt", "./"+sort_trime+"/"+trime_files+"/opencc/back_mark_table_t.txt")
shutil.copyfile("./trimefiles/predict_office.db", "./"+sort_trime+"/"+trime_files+"/predict_office.db")


#複製檔案(洋蔥同文注音plus版)
shutil.copyfile("./trimefiles/essay-jp-onion.txt", "./"+sort_trime+"/"+trime_files+"/essay-jp-onion.txt")
shutil.copyfile("./trimefiles/essay-kr-hanja.txt", "./"+sort_trime+"/"+trime_files+"/essay-kr-hanja.txt")
shutil.copyfile("./trimefiles/bpmfmobileplus.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobileplus.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_m.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hanja.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_hanja.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_m.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul.schema.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.schema.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_hnc_m.schema.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_hnc_m.extended.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_m.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/hangeul_hnc_hanja.dict.yaml", "./"+sort_trime+"/"+trime_files+"/hangeul_hnc_hanja.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.dict.yaml", "./"+sort_trime+"/"+trime_files+"/jpnin1.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1_hw.dict.yaml", "./"+sort_trime+"/"+trime_files+"/jpnin1_hw.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/jpnin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/jpnin1.schema.yaml", "./"+sort_trime+"/"+trime_files+"/jpnin1.schema.yaml")
shutil.copyfile("./trimefiles/latinin1.dict.yaml", "./"+sort_trime+"/"+trime_files+"/latinin1.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/latinin1.extended.dict.yaml")
shutil.copyfile("./trimefiles/latinin1.schema.yaml", "./"+sort_trime+"/"+trime_files+"/latinin1.schema.yaml")
shutil.copyfile("./trimefiles/phrases.en_l_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.en_l_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_o_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.en_o_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.en_u_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.en_u_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hk_more.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkk.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkseg.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hkkseg.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkup_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hkup_w.dict.yaml")
# shutil.copyfile("./trimefiles/phrases.jp_hkmoreup_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hkmoreup_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.kr.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.kr.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_py_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.la_py_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.la_eu_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.la_eu_w.dict.yaml")
# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1只出假名修改檔/", "./"+sort_trime+"/"+trime_files+"/手機jpnin1只出假名修改檔/")
# shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/手機jpnin1精簡轉寫修改檔/", "./"+sort_trime+"/"+trime_files+"/手機jpnin1精簡轉寫修改檔/")
shutil.copytree("./trimefiles/custom檔_日語jpnin1精簡/", "./"+sort_trime+"/"+trime_files+"/custom檔_日語jpnin1精簡/")


#複製檔案(洋蔥同文注音mixin版)
shutil.copyfile("./trimefiles/essay-zh-hant-mc-mixin.txt", "./"+sort_trime+"/"+trime_files+"/essay-zh-hant-mc-mixin.txt")
shutil.copyfile("./trimefiles/bo_mixin_jp.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin_jp.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_m.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin_kr_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_kr_hnc_m.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin_kr_hnc_m.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_la.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin_la.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin_en.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin_en.dict.yaml")
shutil.copyfile("./trimefiles/bo_mixin.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bo_mixin.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin2.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobilemixin2.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixins.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobilemixins.schema.yaml")
shutil.copyfile("./trimefiles/bpmfmobilemixin4.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobilemixin4.schema.yaml")
shutil.copyfile("./trimefiles/phrases.cht_en_w.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./trimefiles/phrases.jp_hkkreduce.dict.yaml", "./"+sort_trime+"/"+trime_files+"/phrases.jp_hkkreduce.dict.yaml")


#複製檔案(洋蔥同文注音雙拼版版)
shutil.copyfile("./trimefiles/bpmfmobiledouble.extended.dict.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobiledouble.extended.dict.yaml")
shutil.copyfile("./trimefiles/bpmfmobiledouble.schema.yaml", "./"+sort_trime+"/"+trime_files+"/bpmfmobiledouble.schema.yaml")
shutil.copyfile("./trimefiles/mixin_bpmf.dict.yaml", "./"+sort_trime+"/"+trime_files+"/mixin_bpmf.dict.yaml")
shutil.copyfile("./trimefiles/sy_d_bpmf.schema.yaml", "./"+sort_trime+"/"+trime_files+"/sy_d_bpmf.schema.yaml")
shutil.copyfile("./trimefiles/element_d_bpmfmobiledouble.yaml", "./"+sort_trime+"/"+trime_files+"/element_d_bpmfmobiledouble.yaml")
shutil.copyfile("./trimefiles/punct_d_bpmf.yaml", "./"+sort_trime+"/"+trime_files+"/punct_d_bpmf.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_H.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥雙拼注音331k_H.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_L.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥雙拼注音331k_L.trime.yaml")
shutil.copyfile("./trimefiles/3.3.1鍵盤檔/洋蔥雙拼注音331k_M.trime.yaml", "./"+sort_trime+"/"+trime_files+"/洋蔥雙拼注音331k_M.trime.yaml")
shutil.copytree("./trimefiles/custom檔_手機注音雙拼不開頭簡拼/", "./"+sort_trime+"/"+trime_files+"/custom檔_手機注音雙拼不開頭簡拼/")


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
os.rename("./"+sort_trime+"/"+trime_files+"/", "./"+sort_trime+"/"+trime_files+"_"+localtime)
os.rename("./"+sort_trime+"/", "./"+the_name+"_"+localtime)



