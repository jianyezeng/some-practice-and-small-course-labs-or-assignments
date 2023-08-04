import pandas as pd

# 创建DataFrame来存储数据
df = pd.read_excel('spss_data_版本2.xlsx')
df = df.astype({'mrTRG': int, '肿瘤分级': int,'微血管浸润':int,'神经侵犯':int})
# 计算LRG的类别
def calculate_lrg(df):
    y_rate = df['阳性淋巴结数']/df['总淋巴结数目']
    y_lrg = 0
    if df['pT'] == 0 and df['pN'] == 0 and y_rate == 0:
        y_lrg = 0
    elif y_rate == 0 and ~(df['pT'] == 0 and df['pN'] == 0):
        y_lrg = 1
    elif y_rate > 0 and y_rate <= 0.25:
        y_lrg = 2 
    elif y_rate > 0.25 and y_rate <= 0.5:
        y_lrg = 3
    elif y_rate > 0.5 and y_rate <= 0.75:
        y_lrg = 4
    else:
        y_lrg = 5
    if y_lrg >= df['LRGmax']:
        return y_lrg
    else:
        return df['LRGmax']

df['LRG类别'] = df.apply(calculate_lrg, axis=1)
print(df[['淋巴结初始报告总计', 'LRG类别']])
df.to_excel('./final_data.xlsx', index=False)