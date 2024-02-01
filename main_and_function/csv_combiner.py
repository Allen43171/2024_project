# csv_combiner.py
import pandas as pd

def combine_all_csv(file_names, key_words):
    # 調整路徑
    new_file_names = ['./temp/' + name + '.csv' for name in file_names]
    # 用於存儲資料框的列表
    dfs = []

    # 讀取每個檔案並將其添加到列表中
    for file_name in new_file_names:
        df = pd.read_csv(file_name)
        dfs.append(df)

    # 合併資料框
    merged_df = pd.concat(dfs, ignore_index=True)

    # 刪除重複資料
    merged_df.drop_duplicates(inplace=True)

    # 將合併後的資料框保存成新的CSV檔案
    merged_df.to_csv(f'./result/all_combine_{key_words}.csv', index=False)
    final_csv = f'./result/all_combine_{key_words}.csv'

    return final_csv
