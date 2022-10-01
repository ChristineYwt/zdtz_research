import pandas as pd
import tushare as ts


def get_qfq(code: str, target_date: str, start_date=None, end_date='30221011') -> float:
    target_date = target_date.replace('-', '')
    start_date = str(start_date) if start_date else str(target_date)
    end_date = str(end_date)

    df = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_date, end_date=end_date)
    res = df.loc[df['trade_date'] == target_date, ['ts_code', 'trade_date', 'close']]

    return res.values.close[0]


def get_hs300(target_date: str, start_date=None, end_date='30221011') -> float:
    hs300 = ts.get_hist_data('hs300', start='20190101', end=end_date)
    return hs300.loc[target_date].close[0]


if __name__ == "__main__":
    pass

