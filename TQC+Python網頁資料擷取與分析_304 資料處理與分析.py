'''
請讀取read.csv中的資料轉換成numpy陣列，並輸出以下資訊：
資料集型態
平均數
中位數
標準差
變異數
極差值
註：數值需四捨五入至小數點後兩位
'''

# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組縮
import pandas as pd

# 讀入 read.csv 檔案
df = pd.read_csv('read.csv')
# 將df中的data欄位取出為ndarray
# data = df['data'].values
data = np.array(df)

# 使用type函數判斷資料型態
print('資料型態：%s' % type(data))
# 使用np.mean()計算平均數
print('平均值：%.2f' % np.mean(data))
# 使用np.median()計算中位數
print('中位數：%.2f' % np.median(data))
# 使用np.std()計算標準差
print('標準差：%.2f' % np.std(data))
# 使用np.var()計算變異數
print('變異數：%.2f' % np.var(data))
# 使用np.ptp()計算極差值
print('極差值：%.2f' % np.ptp(data))
