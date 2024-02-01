# web_crawler.py
import time
import pyautogui
import random
from selenium import webdriver

def input_keyword():
    print("請輸入關鍵字：")
    key_words = input()
    return key_words

def initialize_driver(key_words):
    crawl_file_name = f'./temp/{key_words}.txt'
    url = "https://www.youtube.com/results?search_query=" + key_words
    # 初始化瀏覽器驅動
    driver = webdriver.Chrome()
    # 爬蟲開始
    driver.get(url)

    return driver, crawl_file_name

def scroll_and_wait(driver, scroll_time):
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

