import yfinance as yf
import pandas as pd

# Config et param
MAX_RETRIES = 3
prop_of_nan_treshold = 0.7

### FOCNTIONS INIT DES DATAS
def init_data(omega):
    data = raw_data_dowloader(omega)
    market_df = data_setter(data)
    data_clean, n_asset_pre_drop, n_assets_post_drop, assets_to_drop = caract_data(market_df)

    return data_clean, n_asset_pre_drop, n_assets_post_drop, assets_to_drop




class datapreparation:
    
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



    def data_setter(data):

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
        return market_df


    def caract_data(data):
        # Nan par assets
        missing_per_asset = data.groupby('asset').apply(lambda x: x.isna().sum())
        non_missing_per_asset = data.groupby('asset').apply(lambda x: x.notna().sum())
        prop_missing_per_asset = missing_per_asset/non_missing_per_asset

        assets_to_drop = prop_missing_per_asset[prop_missing_per_asset['close']> drop_prop_treshold].index.tolist()
        print("Assets to drop:", assets_to_drop)

        data_clean = data[~market_df['asset'].isin(assets_to_drop)].copy()

        n_asset_pre_drop = data['asset'].nunique()
        n_assets_post_drop = data_clean['asset'].nunique()

        return data_clean, n_asset_pre_drop, n_assets_post_drop, assets_to_drop
    
    ### INSTALLATION DANS LA BASE DE DONNÉES DUCKDB

