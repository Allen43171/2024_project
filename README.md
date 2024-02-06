# 2024 專題
## 程式
 - 主程式
   - main_script.py
   - 主程式會呼叫其他程式
 - 爬蟲程式碼
   - web_crawler.py
   - 根據輸入關鍵字，會爬取該網頁資料
   - **爬取過程勿自行移動滑鼠**
 - 文字雲程式
   - visualize_and_wordcloud.py
   - 將較常見(前10名)的標題文字以文字雲方式視覺化，並存檔
 - 提取常用字 
   - word_top_n.py
   - 提取標題中的常用字
 - 資料前處理程式
   - data_preprocess.py
   - 將爬取到的資料整理為csv檔
 - 合併再次爬蟲資料 
   - csv_combiner.py
   - 主程式會根據文字雲程式中的常見詞(前5)再次爬蟲，此程式碼會將爬取到的資料整合
 - 處理暫存資料 
   - temporary_data_processor.py
   - 處理掉程式運行的暫存資料
 - 繪圖 
   - visualize_his_scat.py
   - 資料視覺化

## 使用方式
1. 下載所有檔案(包含.py、jieba_need資料夾以及資料夾內檔案)
2. 執行main_script.py
3. cmd介面輸入要爬蟲的關鍵字即可
4. 爬蟲期間，勿移動滑鼠

## 紀錄
 - daily_record.md
   - 整理後的每日記錄，寫在老師excel上面，方便報告
 - just_record.md
   - 詳細紀錄

