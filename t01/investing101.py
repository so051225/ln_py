

def npv_f(rate, cashflows):
    """
        r=0.05
        cfs = [-100, 20, 40, 50, 20, 10]
        npv_f(r, cfs) 
        TEST: 22.80998927303707
    """
    total = 0.0
    for i, cf in enumerate(cashflows):
        total += cf / (1+rate) ** i
    return total


def IRR_f(cashflows, interations=100):
    """
        rate_i+1 = rate_i * (1 - k)
        k = npv_f(rate_i) / investment

        所以做了一百次後，由於 rate和npv 負相關，最後有望找到一個rate使 npv==0

        TEST: IRR_f([-100, 20, 40, 50, 20, 10]) =  0.1360125939440155
        npv_f(_, [-100, 20, 40, 50, 20, 10]) = -1.4210854715202004e-14
        
        see -1.4210854715202004e-14 已經好細。

    """
    rate = 1.0
    investment=cashflows[0]
    for i in range(1, interations+1):
        rate *= 1 - npv_f(rate, cashflows) / investment
    return rate


    