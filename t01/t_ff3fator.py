import pandas as pd
import tushare as ts
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
sns.set()
# mpl.rcParams['font.sans-serif'] = 'WenQuanYi Micro Hei'


def cal_smb_hml(df):
    # 划分大小市值公司
    df['SB'] = df['circ_mv'].map(lambda x: 'B' if x >= df['circ_mv'].median() else 'S')

    # 求账面市值比：PB的倒数
    df['BM'] = 1 / df['pb']

    # 划分高、中、低账面市值比公司
    border_down, border_up = df['BM'].quantile([0.3, 0.7])
    border_down, border_up
    df['HML'] = df['BM'].map(lambda x: 'H' if x >= border_up else 'M')
    df['HML'] = df.apply(lambda row: 'L' if row['BM'] <= border_down else row['HML'], axis=1)

    # 组合划分为6组
    df_SL = df.query('(SB=="S") & (HML=="L")')
    df_SM = df.query('(SB=="S") & (HML=="M")')
    df_SH = df.query('(SB=="S") & (HML=="H")')
    df_BL = df.query('(SB=="B") & (HML=="L")')
    df_BM = df.query('(SB=="B") & (HML=="M")')
    df_BH = df.query('(SB=="B") & (HML=="H")')

    # 计算各组收益率
    R_SL = (df_SL['pct_chg'] * df_SL['circ_mv'] / 100).sum() / df_SL['circ_mv'].sum()
    R_SM = (df_SM['pct_chg'] * df_SM['circ_mv'] / 100).sum() / df_SM['circ_mv'].sum()
    R_SH = (df_SH['pct_chg'] * df_SH['circ_mv'] / 100).sum() / df_SH['circ_mv'].sum()
    R_BL = (df_BL['pct_chg'] * df_BL['circ_mv'] / 100).sum() / df_BL['circ_mv'].sum()
    R_BM = (df_BM['pct_chg'] * df_BM['circ_mv'] / 100).sum() / df_BM['circ_mv'].sum()
    R_BH = (df_BH['pct_chg'] * df_BH['circ_mv'] / 100).sum() / df_BH['circ_mv'].sum()

    # 计算SMB, HML并返回
    smb = (R_SL + R_SM + R_SH - R_BL - R_BM - R_BH) / 3
    hml = (R_SH + R_BH - R_SL - R_BL) / 2
    return smb, hml




pro = ts.pro_api('xx')

"""
    接口：daily
    接口：daily_basic

    pro.daily_basic(): https://tushare.pro/document/2?doc_id=32
    circ_mv	float: 流通市值（万元）
    pb: 市净率（总市值/净资产）
    sse: 上交所

    接口：trade_cal
    描述：获取各大交易所交易日历数据,默认提取的是上交所

    交易所 SSE上交所, SZSE深交所, CFFEX 中金所, SHFE 上期所, CZCE 郑商所, DCE 大商所,
    INE 上能源, IB 银行间,
    XHKG 港交所

    is_open: 是否交易 '0'休市 '1'交易
"""
data = []
df_cal = pro.trade_cal(start_date='20170101', end_date='20190110')
df_cal = df_cal.query('(exchange=="SSE") & (is_open==1)')
for date in df_cal.cal_date:
    df_daily = pro.daily(trade_date=date)
    df_basic = pro.daily_basic(trade_date=date)
    df = pd.merge(df_daily, df_basic, on='ts_code', how='inner')
    smb, hml = cal_smb_hml(df)
    data.append([date, smb, hml])
    print(date, smb, hml)

df_tfm = pd.DataFrame(data, columns=['trade_date', 'SMB', 'HML'])
df_tfm['trade_date'] = pd.to_datetime(df_tfm.trade_date)
df_tfm = df_tfm.set_index('trade_date')
df_tfm.to_csv('df_three_factor_model.csv')
df_tfm.head()

# 获取数据
wanke = pro.daily(ts_code='000002.SZ', start_date='20170101', end_date='20190110')
pingan = pro.daily(ts_code='601318.SH', start_date='20170101', end_date='20190110')
maotai = pro.daily(ts_code='600519.SH', start_date='20170101', end_date='20190110')
wanhua = pro.daily(ts_code='002415.SZ', start_date='20170101', end_date='20190110')
keda = pro.daily(ts_code='002230.SZ', start_date='20170101', end_date='20190110')
# gzA = pro.index_daily(ts_code='399317.SZ', start_date='20170101', end_date='20190110')

# 仅保留收益率数据，且用日期作为index
# 然后按照日期排序（增序）
stock_list = [wanke, pingan, maotai, wanhua, keda]

# Use daily as index
for trade_date in stock_list:
    stock.index = pd.to_datetime(stock.trade_date)
df_stock = pd.concat([stock.pct_chg / 100 for stock in stock_list], axis=1)
df_stock.columns = ['wanke', 'pingan', 'maotai', 'wanhua', 'keda']
df_stock = df_stock.sort_index(ascending=True)
df_stock.head()


# 整合数据，并简单探索
df = pd.merge(df_stock, df_tfm, left_index=True, right_index=True, how='inner')
df = df.fillna(0)
rf = 1.032 ** (1/360) - 1
df = df - rf
df2 = df.copy()
df = df['20180101':]
df.head()


# 观察数据间的相关性
sns.heatmap(df.corr(), cmap='bwr')

# 收益率时序图
plt.figure(figsize=(10, 5))
for col in df.columns:
    plt.plot(df[col], label=col)
plt.title('日收益率时序图(2018至今)', fontsize=20)
plt.legend()

# 累计收益率时序图
plt.figure(figsize=(10, 5))
for col in df.columns:
    plt.plot((df[col]+1).cumprod()-1, label=col)
plt.title('累计收益率时序图(2017至今)', fontsize=20)
plt.legend()


import statsmodels.api as sm

stock_names = {
    'wanke': '万科A',
    'pingan': '中国平安',
    'maotai': '贵州茅台',
    'wanhua': '万华化学',
    'keda': '科大讯飞'
}
for stock in ['wanke', 'pingan', 'maotai', 'wanhua', 'keda']:
    model = sm.OLS(df[stock], sm.add_constant(
        df[['gzA', 'SMB', 'HML']].values))
    result = model.fit()
    print(stock_names[stock] + '\n')
    print(result.summary())
    print('\n\n')