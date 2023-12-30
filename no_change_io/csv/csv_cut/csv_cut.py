############ Python Module の 説明 ############
# CSVを指定の行数までのものに Cut する Python Module
##############################################

import os
import pandas as pd

# 1. カットしたい CSVの ファイル名 & ファイル・Path
csv_file = 'robotama.csv'
csv_file_path = f'{os.getcwd()}/{csv_file}'

# 2. カットする行数(上から)
cut_row_num = 8

# 3. 業種分類の DataFlame を作成する
df = pd.read_csv(csv_file_path, encoding="utf-8")


def dataframe_cutter(df, start, end):
    """
    指定の区間だけDataFlameを切り取る関数

    Parameters:
    df (pandas.DataFrame): 切り取る元のDataFlame
    start (int): 切り取る開始行
    end (int): 切り取る終了行

    Returns:
    pandas.DataFrame: 指定の区間だけ切り取られたDataFlame
    """
    df = df.iloc[int(start):int(end), :]
    return df


# 4. DataFlameから、指定の区間(行数)だけ、切り取る Func
cut_df = dataframe_cutter(df, 0, cut_row_num)
print(cut_df)

new_csv_file = 'result.csv'
create_csv_file_path = f'{os.getcwd()}/{new_csv_file}'

# 5. DataFlame を CSV に変換して Export する
cut_df.to_csv(create_csv_file_path, index=None, header=True)
