import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def scroll_and_wait():
    # 調整瀏覽器視窗(測試用)
    driver.set_window_size(900, 550)

    # 滾動滑鼠，並給予載入資訊的時間
    scroll_times = 200
    for i in range(scroll_times):
        driver.execute_script("window.scrollTo(0, 20000)")
        print(f'滑鼠已滾動{i}次')
        
        time.sleep(3)



def get_all_info(driver):
    # 取得所有資訊
    # 取得id='video-title'相關資訊
    video_informations = driver.find_elements(By.XPATH, "//a[@id='video-title']")
    with open(f'test_{key_words}.txt', 'w', encoding='UTF-8') as file:
        for video_info in video_informations:
            # 將印出的字串寫入檔案
            # 跳過Shorts影片
            if "播放 Shorts" in (video_info.get_attribute('aria-label')):
                pass
            else:
                print(video_info.get_attribute('aria-label'))
                file.write(video_info.get_attribute('aria-label')+"\n")

if __name__ == "__main__":
    print("請輸入關鍵字：")
    key_words = input()
    url = "https://www.youtube.com/results?search_query=" + key_words

    # 初始化瀏覽器驅動
    driver = webdriver.Chrome()

    # 爬蟲開始
    driver.get(url)
    scroll_and_wait()
    # 取得所有aria-label
    get_all_info(driver)
