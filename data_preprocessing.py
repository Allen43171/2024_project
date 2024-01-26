import pandas as pd
import re

def process_data(input_file, output_txt_file, output_csv_file):
    # 讀取原始資料檔案
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.readlines()

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

if __name__ == "__main__":
    # 指定檔案
    input_file = "test_jaychou.txt"
    output_txt_file = "test02.txt"
    output_csv_file = "test03.csv"
    
    # 呼叫函式
    process_data(input_file, output_txt_file, output_csv_file)
