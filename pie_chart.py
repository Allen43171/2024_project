import pandas as pd
import matplotlib.pyplot as plt


# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'sans-serif']
plt.rcParams['font.size'] = 10  # 設定字型大小

# 讀取 CSV 檔案
df = pd.read_csv('test03.csv')

# 將 Views 欄位轉換為數字型態，去除千分位逗號
df['Views'] = df['Views'].replace(',', '', regex=True).astype(int)

# 根據 Views 排序資料
df_sorted = df.sort_values(by='Views', ascending=False)

# 取出前N名資料
position_num = 10
top_three = df_sorted.head(position_num)

# 以 Views 欄位畫出圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(top_three['Views'], labels=top_three['Title'], autopct='%1.1f%%', startangle=140)
plt.title(f'觀看次數前{position_num}名圓餅圖')

# 保存圖片
plt.savefig('top_n_pie_chart.png')
plt.show()

