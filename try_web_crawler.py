from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import os

def initialize_driver(driver_path):
    # 初始化瀏覽器驅動
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service)

def open_browser(driver, url):
    # 開啟瀏覽器
    driver.get(url)
    time.sleep(200)

def get_all_info(driver):
    # 取得所有資訊
    video_informations = driver.find_elements(By.XPATH, "//a[@id='video-title-link']")
    with open('test.txt', 'w', encoding='UTF-8') as file:
        for video_info in video_informations:
            # 將印出的字串寫入檔案
            print(video_info.get_attribute('aria-label'))
            file.write(video_info.get_attribute('aria-label')+"\n")

if __name__ == "__main__":
    # 指定驅動路徑
    # 相對路徑，此驅動程式chromedriver.exe需要和此python放置在同個路徑下
    driver_path = ".\chromedriver.exe"

    # 檢查驅動是否存在
    if not os.path.exists(driver_path):
        print(f"錯誤：找不到 {driver_path} 檔案。請檢查路徑是否正確。")
    else:
        print("請輸入頻道網址：")
        channel_url = "https://www.youtube.com/channel/UC8CU5nVhCQIdAGrFFp4loOQ" + "/videos"
        # url = channel_url + "/videos"
        url = channel_url

        # 切換到腳本所在目錄
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        # 初始化瀏覽器驅動
        driver = initialize_driver(driver_path)

        # 爬蟲開始
        open_browser(driver, url)

        # # 移至最底
        # # ------------------------- try to transform this to function ------------------------- # 
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        # # ------------------------- try to transform this to function ------------------------- # 

        # 取得所有aria-label
        get_all_info(driver)
