# main_script.py
import web_crawler
import data_preprocess
import visualize_and_wordcloud

if __name__ == "__main__": 
    # 爬蟲
    key_words = web_crawler.input_keyword()
    driver, crawl_file_name = web_crawler.initialize_driver(key_words)
    scroll_time = 10
    web_crawler.scroll_and_wait(driver, scroll_time)

    # 資料前處理
    data_preprocess.get_all_info_and_save(driver, crawl_file_name)
    data_preprocess.process_data(crawl_file_name)
    output_csv_file = data_preprocess.process_data(crawl_file_name)

    # 視覺化與文字雲
    dictfile = "jieba_need/dict.txt"  # 字典檔
    stopfile = "jieba_need/stopwords.txt"  # stopwords
    fontpath = "jieba_need/msjh.ttc"  # 字型檔
    visualize_and_wordcloud.analyze_and_visualize_wordcloud(output_csv_file, dictfile=dictfile, stopfile=stopfile, fontpath=fontpath)