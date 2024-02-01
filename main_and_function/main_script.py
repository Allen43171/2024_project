# main_script.py
# 整合爬蟲、資料分析等所有功能
import web_crawler
import data_preprocess
import temporary_data_processor
import csv_combiner
import word_top_n
import visualize_and_wordcloud
import visualize_his_scat

def main():
    print("--"*10 + " 建立資料夾 開始 " + "--"*10)
    temporary_data_processor.create_folder("temp")
    temporary_data_processor.create_folder("result")
    print("--"*10 + " 建立資料夾 結束 " + "--"*10)

    # 爬蟲
    print("--"*10 + " 初步爬蟲 開始 " + "--"*10)
    key_words = web_crawler.input_keyword()
    driver, crawl_file_name = web_crawler.initialize_driver(key_words)
    scroll_time = 100
    web_crawler.scroll_and_wait(driver, scroll_time)
    print("--"*10 + " 初步爬蟲 完成 " + "--"*10)

    # 資料前處理
    print("--"*10 + " 資料前處理 開始 " + "--"*10)
    data_preprocess.get_all_info_and_save(driver, crawl_file_name)
    data_preprocess.process_data(crawl_file_name)
    output_csv_file = data_preprocess.process_data(crawl_file_name)
    print("--"*10 + " 資料前處理 完成 " + "--"*10)
    
    # 篩選出前n名的詞語
    csv_file = output_csv_file
    column_name = 'Title'  # 請替換成實際的欄位名稱
    num_words = 5  # 請替換成您想要取得的詞語數量
    dictfile = "jieba_need/dict.txt"
    stopfile = "jieba_need/stopwords.txt"
    fontpath = "jieba_need/msjh.ttf"
    min_word_length = 1  # 指定最小詞語長度
    
    word_top_n.extract_common_words_from_column(csv_file, column_name, num_words, dictfile, stopfile, fontpath, min_word_length)
    top_nth_word = word_top_n.extract_common_words_from_column(csv_file, column_name, num_words, dictfile, stopfile, fontpath, min_word_length)
    print("#"+"---"*30+"#")
    print("篩選資料 完成")
    print(top_nth_word)
    
    print("--"*10 + " 文字雲 開始 " + "--"*10)
    temporary_data_processor.create_top_n_txt(txt_content=str(top_nth_word), key_words=key_words)
    
    # 視覺化與文字雲
    visualize_and_wordcloud.analyze_and_visualize_wordcloud(output_csv_file, dictfile=dictfile, stopfile=stopfile, fontpath=fontpath)
    print("--"*10 + "文字雲 完成" + "--"*10)
    
    print("--"*10 + " 再次爬蟲 開始 " + "--"*10)
    # 再次爬蟲
    for top_word in top_nth_word:
        driver, crawl_file_name = web_crawler.initialize_driver(top_word)
        scroll_time = 10
        web_crawler.scroll_and_wait(driver, scroll_time)

        data_preprocess.get_all_info_and_save(driver, crawl_file_name)
        data_preprocess.process_data(crawl_file_name)
        output_csv_file = data_preprocess.process_data(crawl_file_name)
    print("--"*10 + " 再次爬蟲 完成 " + "--"*10)

    # -------------------------- combine all csv file -------------------------- #
    # 要合併的檔案名稱列表
    print("--"*10 + " 合併資料 開始 " + "--"*10)
    csv_combiner.combine_all_csv(top_nth_word, key_words=key_words)
    final_csv = csv_combiner.combine_all_csv(top_nth_word, key_words=key_words)
    print("--"*10 + " 合併資料 完成 " + "--"*10)

    # ------------------------------ Generate table ------------------------------ #
    
    print("--"*10 + " 視覺化 開始 " + "--"*10)
    # final_csv = './result/all_combine_AI科技.csv'
    print(final_csv)
    visualize_his_scat.generate_table(final_csv)
    print("--"*10 + " 視覺化 完成 " + "--"*10)

    # ------------------------------ Delete temp ------------------------------ #
    temporary_data_processor.delete_temp_folder()

if __name__ == "__main__":
    main()
