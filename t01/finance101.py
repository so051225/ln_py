

def pv_f(fv, r, n):
    """
    Objective: estimate present value
    fv: future value
    r: discount periodic rate
    n: number of periods
    formula: fv/(1+r)**n
    """
    return fv / (1 + r) ** n

def pv_perpetuity(c, r, g = 0):
    """
    PV (永久年金) ＝ C / R
    c: 代表每一期期末支付的等額現金
    r: 代表每一期的折現率
    
    永續年金，換言之，計現值才有效，因為係保險畀散戶，散戶一開波交一筆，值為pv
    """
    if r - g < 0: 
        print("r < g !!!")
        # return NaN
    else:
        return c / (r - g)

"""
年金
===

Case 1: 散戶在n期內支付 PMT，在n期後有一個終值。
如果是期末支付，那麼最後一期等於 PMT。
前置年金＝＝期初年金 == annuity due (期初支付)

Case 2: 散戶得到一筆現值，然後在n期內，支付

其它留意：

ordinary annuity: 普通年金，期末支付
fv = [pmt / r] * [ (1 + r)**n - 1 ]

Growing annuity: 增長型年金
fv = [pmt / (r - g)] * [ (1 + r)**n - (1 + g)**n ]
"""

def fv_annuity (pmt, r, n):
    return pmt / r * ((1 + r) ** n - 1)

def fv_annuity_loop (pmt, r, n):
    fv = 0
    for i in range (0, n) : 
        fv = fv + (1 + r) ** i
    return fv * pmt

def pv_annuity(pmt, r, n):
    pv = 0
    for i in range (1, n + 1) : 
        pv = pv + 1 / (1 + r) ** i
    return pv * pmt

def pmt_annuity(pv, r, n):
    factor = 0
    for i in range (1, n + 1) : 
        factor = factor + 1 / (1 + r) ** i
    return pv / factor

def fv_annuity_due (pmt, r, n):
    fv = 0
    for i in range (0, n) : 
        fv = fv + (1 + r) ** i
    return fv * pmt * (1 + r)
    