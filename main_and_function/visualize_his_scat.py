# visualize_his_scat.py
import pandas as pd
import matplotlib.pyplot as plt

def preprocess_data_move_outliers(df):
    """資料前處理"""

    # 移除前5名最大數值
    df = df.nlargest(len(df) - 5, 'Views')

    # 移除最後10名最大數值
    df = df.nlargest(len(df) - 10, 'Views', 'all')

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
    plt.grid(True)

    plt.savefig('觀看數與影片時長的關係.png')
    plt.show()

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
    bin_width = 100000
    bins = range(0, int(df['Views'].max()) + bin_width, bin_width)

    # 繪製直方圖
    plt.hist(df['Views'], bins=bins, edgecolor='black', alpha=0.7)

    # 設定標籤及標題
    plt.xlabel('觀看數 (Views)')
    plt.ylabel('影片數量')
    plt.title('觀看數分佈直方圖')

    # 顯示網格
    plt.grid(True)

    # 保存直方圖影像
    output_image = f'觀看數分佈直方圖.png'
    plt.savefig(output_image)

    # 顯示直方圖
    plt.show()

def generate_table(final_csv):
    df = pd.read_csv(final_csv)

    # 資料前處理
    df = preprocess_data_move_outliers(df)

    # 繪製觀看數與影片時長的關係圖
    plot_views_duration_relationship(df)

    # 繪製直方圖
    plot_views_histogram(df)