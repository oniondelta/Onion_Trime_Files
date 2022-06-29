# Onion_Trime_Files：手機同文輸入法（注音、雙拼、形碼）洋蔥方案

####  ※ 請勿使用於商業營利相關行為
####  ※ Commercial use is prohibited
####  ※ 預設鍵盤檔只適用[ trime 3.2.6 版](https://github.com/osfans/trime/releases/tag/v3.2.6)
####  ※ 內附舊版[ trime 3.2.1 版](https://github.com/osfans/trime/releases/tag/v3.2.1) 鍵盤檔
####  ※ 3.2.6 版不知為何，方案部署比舊版慢很多，需耐心
### 內容說明：

- trimefiles 中包含六個主方案（三個注音、一個注音雙拼、二個形碼）和一眾掛接方案

- 二個形碼方案無法使用，因已刪除碼表內容！

- trimefiles 中的檔案不以一個資料夾一個方案，為了較好更新（不用同一個檔案更新數次）

- 提供 Python (sort_trime_file.py) 文件，把 Rime 文件分門別類到各個方案資料夾，使其易安裝部署

### sort_trime_file.py 使用方法：
- 於本倉庫 Onion_Trime_Files 中按右上綠色 〔↓Code〕 ⇨ Download ZIP ⇨ 解壓縮 ZIP ⇨ 進入解壓縮後的資料夾，確認 trimefiles 資料夾 和 sort_trime_file.py 是在同一層 ⇨ 執行 sort_trime_file.py ⇨ 產生一個『洋蔥手機同文方案_{當天日期}』資料夾

- 產生的『洋蔥手機同文方案_{當天日期}』該資料夾內，會把各方案所須文件，分別在該『方案名稱』資料夾內。

- 選擇想要的方案，把內含文件通通放入『 rime 』資料夾。一般裡面已有 opencc 資料夾，移動 opencc 裡面檔案到 opencc 資料夾內，沒有的話，整個 opencc 移過去 ，「重新部署」即可。

  > 如果缺少檔案，會立即出錯無法執行！



### 各方案說明：

- [手機同文輸入法『注音 洋蔥純注音版』](http://deltazone.pixnet.net/blog/post/321396937)

- [手機同文輸入法『注音 洋蔥plus版 』](http://deltazone.pixnet.net/blog/post/348003908)

- [手機同文輸入法『注音 洋蔥mix‧in版 』](http://deltazone.pixnet.net/blog/post/347908319)

- [手機同文輸入法『注音 洋蔥雙拼版 』](https://deltazone.pixnet.net/blog/post/360004547)

### 虛擬鍵盤圖示：

 > 20220628 更新，與下方有些微不同 。

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


### 虛擬鍵盤功能說明：

 > 20220628 更新，右上角向上滑動鍵位與下面說明不同 。
 
 > 3.2.6 版鍵盤檔，新增剪貼簿功能，合併「顏文字」和「符號 emoji 」鍵盤 。

---

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/mix-in_description.png" alt="介紹PURE" width="600" />

---

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/plus_description.png" alt="介紹PLUS" width="600" />

---

<img src="https://github.com/oniondelta/Onion_Trime_Files/blob/master/img/pure_description.png" alt="介紹MIXIN" width="600" />

---

### 贊助 Donate：

  > 從第一個方案上傳已持續更新四年！方案從頭到尾大改、新創、新增非常多功能！且做了許多圖文說明！花了族繁不及備載的心力！

  > 懇請贊助 (Donate) 支持，讓 Rime 洋蔥的一系列方案更新更有動力！

- [按此以〈綠界〉贊助 Donate：](https://p.ecpay.com.tw/D555162)

  #### [![donate1](https://payment.ecpay.com.tw/Upload/QRCode/202010/QRCode_170c287e-2db8-4b50-b87f-8d36500a3958.png)](https://p.ecpay.com.tw/D555162)

- [按此以〈歐付寶〉贊助 Donate：](https://qr.opay.tw/q1ql7)

  #### [![donate2](https://payment.opay.tw/Upload/Broadcaster/2294343/QRcode/QRCode_7AC0FA1CAD39F0B66CFD5513A2173D1A.png)](https://qr.opay.tw/q1ql7)

