# data_preprocess.py
from selenium.webdriver.common.by import By
import pandas as pd
import re

def get_all_info_and_save(driver, crawl_file_name):
    # 取得所有資訊
    # 取得id='video-title'相關資訊
    video_informations = driver.find_elements(By.XPATH, "//a[@id='video-title']")
    # crawl_file_name = 'test_{key_words}.txt'
    with open(crawl_file_name, 'w', encoding='UTF-8') as file:
        print("檔案生成中")
        for video_info in video_informations:
            # 跳過Shorts影片
            if "播放 Shorts" in (video_info.get_attribute('aria-label')):
                pass
            # 將印出的字串寫入檔案
            else:
                print(video_info.get_attribute('aria-label'))
                file.write(video_info.get_attribute('aria-label')+"\n")
    print("檔案生成完畢！")

def process_data(crawl_file_name):
    # 讀取原始資料檔案
    with open(crawl_file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    # 指定檔案名稱
    output_csv_file = crawl_file_name.replace(".txt", ".csv")

    # 建立 DataFrame 並將資料改寫為指定形式
    df = pd.DataFrame(columns=['Title', 'Uploader', 'Views', 'Time Ago', 'Minute', 'Second'])
    for line in data:
        match = re.search(r'(.+)上傳者：(.+)觀看次數：(.+)次 (.+)前 (.+) 分鐘 (.+) 秒', line)
        if match:
            title = match.group(1).strip()
            uploader = match.group(2).strip()
            views = match.group(3).strip()
            time_ago = match.group(4).strip()
            minute = match.group(5).strip()
            second = match.group(6).strip()
            # df = pd.concat([df, pd.DataFrame({'Title': [title], 'Uploader': [uploader], 'Views': [views], 'Time Ago': [time_ago], 'Duration': [duration]})], ignore_index=True)  
            df = pd.concat([df, pd.DataFrame({'Title': [title], 'Uploader': [uploader], 'Views': [views], 'Time Ago': [time_ago], 'Minute': [int(minute)], 'Second': [int(second)]})], ignore_index=True)  
    
    # 將 Views 欄位轉換為數字型態，去除千分位逗號
    df['Views'] = df['Views'].replace(',', '', regex=True).astype(int)

    # 保存一個額外的 CSV 檔案
    df.to_csv(output_csv_file, index=False, encoding='utf-8')

    # 檢查 DataFrame 的內容
    print(df)
    print("檔案轉換完畢！")

    return output_csv_file
