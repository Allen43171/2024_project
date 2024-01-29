# web_crawler_search.py
import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def input_keyword():
    print("請輸入關鍵字：")
    key_words = input()
    return key_words

def initialize_driver(key_words):
    crawl_file_name = f'{key_words}.txt'
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
    # pyautogui簡易防呆，讓滑鼠在視窗中間
    pyautogui.moveTo(400, 250, duration=0.1)
    # 利用pyautogui直接持續滾動
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

def load_custom_dict(dictfile, stopfile):
    # 載入自定義字典
    jieba.load_userdict(dictfile)

    # 載入停用詞
    with open(stopfile, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]

    return stopwords

def analyze_and_visualize_wordcloud(output_csv_file, top_n=10, dictfile="jieba_need/dict.txt", stopfile="jieba_need/stopwords.txt", fontpath="jieba_need/msjh.ttc"):
    # 讀取 CSV 檔案
    df = pd.read_csv(output_csv_file)

    # 載入自定義字典和停用詞
    stopwords = load_custom_dict(dictfile, stopfile)

    # 根據 Views 排序資料
    df_sorted = df.sort_values(by='Views', ascending=False)

    # 取出前N名資料
    top_videos = df_sorted.head(top_n)

    # 將標題拆分成短詞，並進行分詞
    all_titles = ' '.join(top_videos['Title'])
    words = jieba.lcut(all_titles)

    # 去除停用詞
    words = [word for word in words if word not in stopwords]

    # 設定中文字型的路徑
    font_path = fontpath

    # 生成文字雲
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(' '.join(words))

    # 繪製文字雲
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # 保存圖片
    plt.savefig(f'{key_words}_前{top_n}文字雲圖.png')
    
    plt.show()

if __name__ == "__main__":  
    key_words = input_keyword()
    # 初始化驅動器並取得檔案名稱
    driver, crawl_file_name = initialize_driver(key_words)

    # 滾動開始
    scroll_time = 200
    scroll_and_wait(driver)
    # 取得資料及保存
    get_all_info_and_save(driver, crawl_file_name)

    # 資料前處理
    process_data(crawl_file_name)

    output_csv_file = process_data(crawl_file_name)

    dictfile = "jieba_need/dict.txt"  # 字典檔
    stopfile = "jieba_need/stopwords.txt"  # stopwords
    fontpath = "jieba_need/msjh.ttc"  # 字型檔
    analyze_and_visualize_wordcloud(output_csv_file, dictfile=dictfile, stopfile=stopfile, fontpath=fontpath)
    