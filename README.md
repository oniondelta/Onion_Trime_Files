# 手機同文輸入法 Trime 洋蔥方案（注音、雙拼、形碼）

####  ※ 請勿使用於商業營利相關行為
####  ※ Commercial use is prohibited

## 版本與先導：

- 預設鍵盤檔只適用[ trime 3.2.6 版](https://github.com/osfans/trime/releases/tag/v3.2.6) 和[ trime 3.2.7 版](https://github.com/osfans/trime/releases/tag/v3.2.7)

- 內附舊版[ trime 3.2.1 版](https://github.com/osfans/trime/releases/tag/v3.2.1) 鍵盤檔

- 3.2.6 和 3.2.7 版方案部署比舊版慢很多，需很有耐心，全部方案一次性加入「部署」需要50分鐘XD

- 建議把手機「設定」「螢幕亮屏」時間拉到最長再「部署」。「螢幕關閉休眠」會影響「部署」時間，甚至「部署」不起來。

- 建議先安裝精簡的 [初始化方案](https://github.com/oniondelta/Onion_Trime_Files/tree/master/trimefiles/%E5%88%9D%E5%A7%8B%E5%8C%96%E6%96%B9%E6%A1%88)，可正常運作再裝這邊重型方案。

## 內容說明：

- trimefiles 包含六個主方案（三個注音、一個注音雙拼、二個形碼）和一眾掛接方案

- 二個形碼方案已刪除碼表內容，無法使用！

- 為較好更新，不用同一檔案更新數次，trimefiles 中文件不先分方案。

- 提供 sort_trime_file.py，把所需 Trime 文件放到各個方案資料夾。

## sort_trime_file.py 使用方法：

- 於本倉庫 Onion_Trime_Files 按右上綠色 〔↓Code〕 ⇨ Download ZIP ⇨ 解壓縮 ZIP 進入資料夾 ⇨ 用 Python 執行 sort_trime_file.py ⇨ 產生『洋蔥手機同文方案_{當天日期}』資料夾

- 『洋蔥手機同文方案_{當天日期}』，各個方案所需文件，分別放置於下層『方案名稱』資料夾。

- 選取欲使用方案，內含文件通通放入『 rime 』資料夾。裡面已有 opencc 資料夾，移動 opencc 裡面檔案到 opencc 資料夾內，沒有則整個 opencc 移過去 ，「重新部署」方可。

## 各方案說明：

- [手機同文輸入法『注音 洋蔥純注音版』](http://deltazone.pixnet.net/blog/post/321396937)

- [手機同文輸入法『注音 洋蔥plus版 』](http://deltazone.pixnet.net/blog/post/348003908)

- [手機同文輸入法『注音 洋蔥mix‧in版 』](http://deltazone.pixnet.net/blog/post/347908319)

- [手機同文輸入法『注音 洋蔥雙拼版 』](https://deltazone.pixnet.net/blog/post/360004547)

## 虛擬鍵盤圖示：

 > 以下為 20220628 更新適用於 3.2.6 版鍵盤檔圖示

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_01.png" alt="介紹1" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_01-4.png" alt="介紹1-4" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_01-2.png" alt="介紹1-2" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_01-3.png" alt="介紹1-3" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_ocm-mixin.jpg" alt="介紹ocm-mixin" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_02.png" alt="介紹2" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_03.png" alt="介紹3" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_04.png" alt="介紹4" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_05.png" alt="介紹5" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_06.png" alt="介紹6" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_07.png" alt="介紹7" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_08.png" alt="介紹8" width="400" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/onion_mobile_09.png" alt="介紹9" width="400" />


## 虛擬鍵盤功能說明：
 
 > 3.2.6 版鍵盤檔，新增剪貼簿功能，合併「顏文字」和「符號 emoji 」鍵盤 。

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/mix-in_description.png" alt="介紹PURE" width="600" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/plus_description.png" alt="介紹PLUS" width="600" />

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/pure_description.png" alt="介紹MIXIN" width="600" />

## 贊助 Donate：

  > 從第一個方案上傳已持續更新五年以上！方案從頭到尾大改、新創、新增非常多功能！且做了許多圖文說明！花了族繁不及備載的心力！

  > 懇請贊助 (Donate) 支持，讓 Rime 洋蔥的一系列方案更新更有動力！

- [按此以〈綠界〉贊助 Donate：](https://p.ecpay.com.tw/D555162)

  #### [![donate1](https://payment.ecpay.com.tw/Upload/QRCode/202010/QRCode_170c287e-2db8-4b50-b87f-8d36500a3958.png)](https://p.ecpay.com.tw/D555162)

- [按此以〈歐付寶〉贊助 Donate：](https://qr.opay.tw/q1ql7)

  #### [![donate2](https://payment.opay.tw/Upload/Broadcaster/2294343/QRcode/QRCode_7AC0FA1CAD39F0B66CFD5513A2173D1A.png)](https://qr.opay.tw/q1ql7)

