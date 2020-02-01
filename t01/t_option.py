


def payoff_call(sT, x):
    """
        有一個歐式看漲期權規定買方可以用行使價30美元，
        在3個月後購買某只股票，該期權在到期日的收益可
        以用以下公式計算。
        payoff(call) = Max(sT − x,0)
    """
    return (sT - x + abs(sT - x)) / 2

"""
>>> sT=np.arange(10, 50, 10)
>>> x=20
>>> payoff_call(sT, x)
array([ -95.,   10.,  -85., -180.])


但用以下簡單邏輯就不能應用於 type(sT) = array
    if (sT - x) > 0:
        return sT - x
    else:
        return 0
"""