# csv_combiner.py
import pandas as pd

def combine_all_csv(file_names):
    # 利用列表生成式將檔案名稱加上 '.csv' 並存儲在新的列表中
    new_file_names = [name + '.csv' for name in file_names]

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
    merged_df.to_csv('合併後的檔案.csv', index=False)
    final_csv = '合併後的檔案.csv'

    return final_csv