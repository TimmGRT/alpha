
#%%
import yfinance as yf
import pandas as pd

#%%
omega_sectorial = {"tech" : ['AAPL', 'MSFT', 'NVDA', 'AMD', 'ORCL', 'CRM', 'INTC', 'ADP', 'CSCO', 'IBM', 'TXN', 'QCOM', 'AVGO', 'MU', 'HPQ', 'AMAT', 'LRCX', 'SNPS', 'NOW', 'ZS', 'PANW', 'ADBE', 'MSFT', 'SWKS', 'FISV', 'CDNS', 'KLAC', 'ATVI', 'V', 'MA'],
         #"health" : ['JNJ', 'PFE', 'MRK', 'UNH', 'ABBV', 'BMY', 'GILD', 'AMGN', 'MDT', 'SYK', 'DHR', 'ISRG', 'ZBH', 'BIIB', 'LLY', 'REGN', 'VRTX', 'HCA', 'TMO', 'ABT'],
         #"finance" : ['JPM', 'BAC', 'C', 'GS', 'MS', 'WFC', 'BK', 'SCHW', 'CME', 'ICE', 'SPGI', 'AXP', 'COF', 'USB', 'PNC', 'BLK', 'TFC', 'STT', 'RJF', 'AMP'],
         #"disc_cons" : ['AMZN', 'MCD', 'SBUX', 'HD', 'NKE', 'LOW', 'TGT', 'COST', 'TJX', 'MAR', 'ROST', 'YUM', 'DRI', 'LVS', 'WYNN'],
         #"basics_cons" : ['KO', 'PG', 'PEP', 'WMT', 'COST', 'CL', 'MDLZ', 'KMB', 'WBA', 'GIS'],
         #"industry" : ['BA', 'CAT', 'DE', 'GE', 'HON', 'LMT', 'RTX', 'NOC', 'ITW', 'PH', 'MMM', 'EMR', 'CMI', 'FLS', 'TXT'],
         "energy" : ['XOM', 'CVX', 'COP', 'SLB', 'PSX', 'EOG', 'OXY', 'VLO', 'HAL', 'MPC'],
         "materials" : ['LIN', 'DD', 'NUE', 'FCX', 'APD'],
         "telecom" : ['T', 'VZ', 'TMUS', 'CMCSA', 'DISH'],
         "utilities" : ['NEE', 'DUK', 'SO', 'AEP', 'EXC'],
         "imo" : ['PLD', 'AMT', 'SPG', 'PSA', 'O']
}
#%%
n_assets = len(omega_sectorial["tech"])+len(omega_sectorial["energy"])+len(omega_sectorial["materials"])+len(omega_sectorial["telecom"])+len(omega_sectorial["utilities"])+len(omega_sectorial["imo"])
print(n_assets)
#%%
# CONFIG & PARAM
omega = [item for sublist in omega_sectorial.values() for item in sublist]
MAX_RETRIES = 3

def raw_data_dowloader(omega):
    for attempt in range(MAX_RETRIES):
        tickers = omega 
        try:
            data = yf.download(
                tickers,
                start="2000-01-01",
                interval="1d",
                group_by="ticker",
                auto_adjust=True,
                threads=True)
            return data
    
        except Exception as e:
            print('retrying datas downloading')
            time.sleep(2)
        return None

data = raw_data_dowloader(omega)


#%%
all_frames = []

for ticker in omega:

    if ticker not in data:
        #print("Missing ticker:", ticker)
        continue

    df = data[ticker].copy()
    df["asset"] = ticker
    df["timestamp"] = df.index

    df = df.rename(columns={
        "Open":"open",
        "High":"high",
        "Low":"low",
        "Close":"close",
        "Volume":"volume"
    })

    df = df[[
        "timestamp",
        "asset",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]]

    all_frames.append(df)

market_df = pd.concat(all_frames).sort_values(["asset","timestamp"]).reset_index(drop=True)



