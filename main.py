import pandas as pd

def getTickerData(ticker):
    df = pd.read_csv(f'stockData/{ticker}.csv')
    return df

if __name__ == '__main__':
    data=getTickerData('HDFC')[['Date','Close']]
    print(data.iloc['2020-09-11'])