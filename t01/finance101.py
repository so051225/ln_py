

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

def PVIFA (r, n):
    """
        PVIFA(r, n)為!普通年金!現值利率因子(Present Value Interest Factor of Annuity, PVIFA)
        i 由 1 到 n 期，加總 1/(1+r) ** i
        你問點解?
        畫下 cashflow diagram
        TEST: PVIFA(.1, 4)=3.169865446349293
    """
    factor = 0
    for i in range (1, n + 1):
        factor = factor + 1 / (1 + r) ** i
    return factor

def FVIFA(r, n):
    """
    FVIFA(i, n)為年金終值利率因子(Future Value Interest Factor of Annuity, FVIFA)
    TEST: FVIFA(10%, 5) = 6.1051
    """
    factor = 0
    for i in range (0, n):
        factor = factor + (1 + r) ** i
    return factor

def MC(r, n):
    """
    貸款之平均攤還因子恰為年金現值因子之倒數，此因子 稱為貸款常數(Loan Constant, LC)
    或不動產抵押貸款常 數(Mortgage Constant, MC)，即在特定的利率及貸款期 限下，目前
    每借1元，未來每期應攤還的貸款支付額。
    """
    return 1/PVIFA(r, n)

# directly use 等比數列公式
# def fv_annuity (pmt, r, n):
#    return pmt / r * ((1 + r) ** n - 1)

def fv_annuity (pmt, r, n):
    """
    TEST: fv_annuity(16000, .1, 5) = 97681.60000000002
    """
    return pmt * FVIFA(r, n)

def pv_annuity(pmt, r, n):
    return pmt * PVIFA (r, n)

def pmt_annuity(pv, r, n):
    """
    假設小陳剛買了一輛賓士轎車，總價300萬元，自備100萬 元，
    向銀行貸款200萬元，年利率12%(即月利率1%)， 分二年(二
    十四個月)每月平均攤還。試問小陳未來二十 四個月內每個月應還多少?

    TEST: pmt_annuity(200*10000, 12/100/12, 2*12) = 94146.94444652944

    """
    return pv / PVIFA (r, n)

def fv_annuity_due (pmt, r, n):
    """
        前置年金，期初支付，到終期比普通年金多左 (1 + r)
    """
    return fv_annuity(pmt, r, n) * (1 + r)

