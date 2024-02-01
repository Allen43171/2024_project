# temporary_data_processor.py
import os
import time
import shutil

def create_folder(folder_name):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)

    # 判斷資料夾是否存在，不存在則創建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'{folder_name} 已建立在 {folder_path}')
    else:
        print(f'{folder_name} 已存在於 {folder_path}')

def create_top_n_txt(txt_content, key_words):
    temp_folder_path = os.path.join(os.getcwd(), 'result')
    test_file_path = os.path.join(temp_folder_path, f'{key_words}top_n.txt')

    # 生成.txt檔案
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write(txt_content)

def delete_temp_folder():
    current_directory = os.getcwd()
    temp_folder_path = os.path.join(current_directory, 'temp')

    time.sleep(5)

    # 刪除temp資料夾及其內容
    shutil.rmtree(temp_folder_path)
    print(f'Temp folder {temp_folder_path} deleted.')

