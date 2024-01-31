# visualize_and_wordcloud.py
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_custom_dict(dictfile, stopfile):
    # 載入自定義字典
    jieba.load_userdict(dictfile)

    # 載入停用詞
    with open(stopfile, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]

    return stopwords

def analyze_and_visualize_wordcloud(output_csv_file, top_n=10, dictfile="jieba_need/dict.txt", stopfile="jieba_need/stopwords.txt", fontpath="jieba_need/msjh.ttc"):
    # 讀取 CSV 檔案
    df = pd.read_csv(output_csv_file)

    # 載入自定義字典和停用詞
    stopwords = load_custom_dict(dictfile, stopfile)

    # 根據 Views 排序資料
    df_sorted = df.sort_values(by='Views', ascending=False)

    # 取出前N名資料
    top_videos = df_sorted.head(top_n)

    # 將標題拆分成短詞，並進行分詞
    all_titles = ' '.join(top_videos['Title'])
    words = jieba.lcut(all_titles)

    # 去除停用詞
    words = [word for word in words if word not in stopwords]

    # 設定中文字型的路徑
    font_path = fontpath

    # 生成文字雲
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(' '.join(words))

    # 繪製文字雲
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # 保存圖片
    plt.savefig(f'{output_csv_file.replace(".csv", "")}_前{top_n}文字雲圖.png')
    
    # plt.show()