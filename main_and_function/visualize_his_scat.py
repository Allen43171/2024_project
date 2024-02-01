# visualize_his_scat.py
import pandas as pd
import matplotlib.pyplot as plt
import time

def preprocess_data_move_outliers(df):
    """繪圖資料前處理"""
    # 移除前5名最大數值
    df = df.nlargest(len(df) - 5, 'Views')

    # 移除最後10名最大數值
    df = df.nlargest(len(df) - 10, 'Views', 'all')

    # 刪除 'Views' 欄位大於30萬的所有資料
    df = df[df['Views'] <= 300000]

    return df

def plot_views_duration_relationship(df):
    # 設定中文字型
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'sans-serif']
    plt.rcParams['font.size'] = 10  # 設定字型大小

    """繪製觀看數(Views)、影片時長(Total Second)的關係圖"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Views'], df['Total Second'], alpha=0.5)
    plt.title('觀看數與影片時長的關係')
    plt.xlabel('觀看數 (Views)')
    plt.ylabel('影片時長 (Total Second)')
    # 顯示網格
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

    plt.savefig("./result/"+'觀看數與影片時長散布圖.png')
    print("已生成散布圖")
    # plt.show()

def plot_views_histogram(df):
    """
    讀取CSV檔案，繪製觀看數分佈直方圖，並保存影像。

    Parameters:
    - csv_file (str): CSV檔案路徑，假設有一欄名為"Views"表示觀看數。
    """
    # 設定中文字型
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'sans-serif']
    plt.rcParams['font.size'] = 10  # 設定字型大小

    # 設定直方圖區間
    bin_width = 10000
    bins = range(0, int(df['Views'].max()) + bin_width, bin_width)

    # 繪製直方圖
    # plt.hist(df['Views'], bins=bins, alpha=0.7)
    plt.hist(df['Views'], bins=bins, edgecolor='black', linewidth=1.2, alpha=0.7)

    # 設定標籤及標題
    plt.xlabel('觀看數 (Views)')
    plt.ylabel('影片數量')
    plt.title('觀看數分佈直方圖')

    # 顯示網格
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

    # 保存直方圖影像
    plt.savefig("./result/" + '觀看數分佈直方圖.png')
    print("已生成直方圖")

def generate_table(final_csv):
    df = pd.read_csv(final_csv)

    # 資料前處理
    df = preprocess_data_move_outliers(df)

    # 繪製直方圖
    plot_views_histogram(df)

    time.sleep(3)

    # 繪製觀看數與影片時長的關係圖
    plot_views_duration_relationship(df)


# # ------------------------------ Test ------------------------------ #
# print("--"*10 + " 視覺化 開始 " + "--"*10)
# final_csv = f'./result/all_combine_CPU選擇.csv'
# generate_table(final_csv)
# print("--"*10 + " 視覺化 完成 " + "--"*10)
