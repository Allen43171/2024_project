# Project Record
## 2024/01/24
已完成
- web_crawler.py 
  - 爬蟲程式，可將該網址下的影片資訊存成純文字檔(.txt)
  - 需要將驅動程式 chromedriver.exe 放在相同路徑才能執行

待新增
- 明日(01/25) 開始撰寫資料分析程式，預計使用pandas套件

待優化
- 【程式優化】無UI、無法自行輸入網址
  - 目前缺少使用者自行輸入網址的部分，需要從程式碼中直接修改。
  - 日後新增簡易UI。

- 【程式優化】web_crawler.py運作時間短
  - 目前 web_crawler.py 持續爬蟲時間較短，爬蟲過程需要手動滾動至最下方。
  - 之後會調整時間或是嘗試其他方式以確保資料蒐集完整。

- 【程式優化】爬下來的資料會彼此覆蓋
  - 先進行手動改名。
  - 之後蒐集資料可嘗試帶入頻道名稱、當下時間等等來加以區分。


## 2024/01/25
已完成
- data_preprocessing.py，資料處理程式
- 可將爬蟲程式web_crawler.py 取得的資料進行資料處理，存成csv
- pie_chart.py，圓餅圖程式
- web_crawler_search.py，爬蟲程式，可讓使用者自行輸入關鍵字

遇到問題
- matplotlib套件問題，無法使用
  - 錯誤訊息「mportError: DLL load failed while importing _cext: 找不到指定的模組。」
  - 重新安裝matplotlib套件，無效
  - 嘗試 pip install msvc-runtime，無效
  - 補安裝套件 Microsoft Visual C++ 2015-2022 Redistributable (x64)，成功解決
- matplotlib套件問題，中文無法顯示
  - 可透過rcParams來調整參數，設定字型
- 反爬蟲問題，爬蟲程式滑鼠滾動問題，需要手動滾動頁面，若用程式會停住



## 2024/01/26
已完成
 - 已解決反爬蟲問題
 - 爬蟲程式模組化
   - 將爬蟲程式的各種功能切開，方便維護及使用
   - 包含初始化驅動、滑鼠滾動、存取爬取檔案、資料清洗

遇到問題
 - 反爬蟲問題(解決)
   - 堅持使用selenium無法完全解決
   - 改用autogui強制操作滑鼠，速度更快，但必須將游標放在瀏覽器視窗內
   - 有簡易防呆，但有可能因為電腦不同導致防呆失效

## 2024/01/29
已完成
1. 以文字雲方式顯示各影片標題的用詞
2. 將各個函式依照功能切開，用主程式呼叫，方便維護
   - 主程式 main_script.py
   - 網路爬蟲 web_carwler.py
   - 資料處理 data_preprocess.py
   - 文字雲 visualize_and_wordcloud.py

遇到問題
1. 文字雲繁體中文問題，顯示問題需另外安裝字型。斷詞部分加裝繁體中文版本


