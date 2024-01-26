# web_crawler_search.py
import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

def initialize_driver(key_words):
    crawl_file_name = f'test_{key_words}.txt'
    url = "https://www.youtube.com/results?search_query=" + key_words
    # 初始化瀏覽器驅動
    driver = webdriver.Chrome()
    # 爬蟲開始
    driver.get(url)

    return driver, crawl_file_name

def scroll_and_wait(driver):
    # 調整瀏覽器視窗大小(測試用)
    driver.set_window_size(900, 550)

    # 調整瀏覽器頁面大小，可載入更多資料
    zoom_out = "document.body.style.zoom='0.5'"
    driver.execute_script(zoom_out)

    # 滾動滑鼠，並給予載入資訊的時間
    # 利用pyautogui直接持續滾動
    pyautogui.moveTo(400, 250, duration=0.1)
    for i in range(scroll_time):
        pyautogui.scroll((-1)*(random.randint(4000, 5000)))
        print(f'滑鼠已滾動{i}次')
    time.sleep(5)

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

# 資料前處理未完成，先分段作業
'''
def process_data(crawl_file_name):
    # 讀取原始資料檔案
    with open(crawl_file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    # 指定檔案名稱
    output_txt_file = crawl_file_name.replace(".txt", "01.txt")
    output_csv_file = crawl_file_name.replace(".txt", "02.csv")

    # 建立 DataFrame 並將資料改寫為指定形式
    df = pd.DataFrame(columns=['Title', 'Uploader', 'Views', 'Time Ago', 'Duration'])
    for line in data:
        match = re.search(r'(.+)上傳者：(.+)觀看次數：(.+)次 (.+)前 (.+) (.+)', line)
        if match:
            title = match.group(1).strip()
            uploader = match.group(2).strip()
            views = match.group(3).strip()
            time_ago = match.group(4).strip()
            duration = match.group(5).strip()
            df = pd.concat([df, pd.DataFrame({'Title': [title], 'Uploader': [uploader], 'Views': [views], 'Time Ago': [time_ago], 'Duration': [duration]})], ignore_index=True)

    # 將改寫後的資料寫入新檔案
    df.to_csv(output_txt_file, index=False, sep=',', encoding='utf-8')

    # 再保存一個額外的 CSV 檔案 (test03.csv)
    df.to_csv(output_csv_file, index=False, encoding='utf-8')

    # 檢查 DataFrame 的內容
    print(df)
    print("檔案轉換完畢！")
'''
if __name__ == "__main__":
    print("請輸入關鍵字：")
    key_words = input()

    # 初始化驅動器並取得檔案名稱
    driver, crawl_file_name = initialize_driver(key_words)

    # 滾動開始
    scroll_time = 200
    scroll_and_wait(driver)
    # 取得資料及保存
    get_all_info_and_save(driver, crawl_file_name)

    # 資料前處理
    # process_data(crawl_file_name)