# word_top_n.py
import pandas as pd
import jieba
from collections import Counter

def load_custom_dict(dictfile, stopfile):
    # 載入自定義字典
    jieba.load_userdict(dictfile)

    # 載入停用詞
    with open(stopfile, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]

    return stopwords

def extract_common_words_from_column(csv_file, column_name, num_words=5, dictfile=None, stopfile=None, fontpath=None, min_word_length=1):
    # 讀取CSV檔案
    df = pd.read_csv(csv_file)

    # 取得指定欄位的文字內容
    text_content = ' '.join(df[column_name].dropna())

    # 載入自定義字典和停用詞
    if dictfile and stopfile:
        stopwords = load_custom_dict(dictfile, stopfile)
    else:
        stopwords = []

    # 使用jieba進行分詞，並過濾停用詞
    words = [word for word in jieba.lcut(text_content) if word not in stopwords and len(word) > min_word_length]

    # 使用Counter計算詞頻
    word_count = Counter(words)

    # 取得詞頻最高的num_words個詞語
    common_words = word_count.most_common(num_words)

    # 印出結果
    top_nth_word = []
    print(f"長度大於{min_word_length}的最常出現的{num_words}個詞語：")
    for word, count in common_words:
        # print(f"{word}: {count}次")
        top_nth_word.append(word)
        print(f"{word}")

    return top_nth_word 


