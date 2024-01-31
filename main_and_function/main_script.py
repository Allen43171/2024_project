# main_script.py
# 整合爬蟲、資料分析等所有功能
import web_crawler
import data_preprocess
import word_top_n
import csv_combiner
import visualize_his_scat

def main():
    # 爬蟲
    key_words = web_crawler.input_keyword()
    driver, crawl_file_name = web_crawler.initialize_driver(key_words)
    scroll_time = 10
    web_crawler.scroll_and_wait(driver, scroll_time)

    # 資料前處理
    data_preprocess.get_all_info_and_save(driver, crawl_file_name)
    data_preprocess.process_data(crawl_file_name)
    output_csv_file = data_preprocess.process_data(crawl_file_name)

    # 篩選出前n名的詞語
    # ------------------------------------ word_top_n.py ------------------------------------ #
    csv_file = output_csv_file  # 請替換成實際的CSV檔案路徑
    column_name = 'Title'  # 請替換成實際的欄位名稱
    num_words = 5  # 請替換成您想要取得的詞語數量
    dictfile = "jieba_need/dict.txt"
    stopfile = "jieba_need/stopwords.txt"
    fontpath = "jieba_need/msjh.ttc"
    min_word_length = 1  # 指定最小詞語長度

    word_top_n.extract_common_words_from_column(csv_file, column_name, num_words, dictfile, stopfile, fontpath, min_word_length)
    top_nth_word = word_top_n.extract_common_words_from_column(csv_file, column_name, num_words, dictfile, stopfile, fontpath, min_word_length)
    print("#"+"---"*30+"#")
    print(top_nth_word)

    # 再次爬蟲
    for top_word in top_nth_word:
        driver, crawl_file_name = web_crawler.initialize_driver(top_word)
        scroll_time = 10
        web_crawler.scroll_and_wait(driver, scroll_time)

        data_preprocess.get_all_info_and_save(driver, crawl_file_name)
        data_preprocess.process_data(crawl_file_name)
        output_csv_file = data_preprocess.process_data(crawl_file_name)
    
    # -------------------------- combine all csv file -------------------------- #
    # 要合併的檔案名稱列表
    csv_combiner.combine_all_csv(top_nth_word)
    final_csv = csv_combiner.combine_all_csv(top_nth_word)

    # ------------------------------ Generate table ------------------------------ #
    visualize_his_scat.generate_table(final_csv)

if __name__ == "__main__":
    main()
