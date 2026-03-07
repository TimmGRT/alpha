import yfinance as yf
import pandas as pd
import duckdb 
from pathlib import Path
from omega_choice import omega
from indicator_choice import indicators
import datetime
from functools import lru_cache
from fredapi import Fred

# Parameters pour le ciblage de la loc du fichier d'installation 
current_file = Path(__file__).resolve()
direction = current_file.parent.parent
#Création du datalake dans le folder, du directory parquet et de la BD dDB
Data_parquet_path = direction/"DATALAKE"/"parquet"
Data_parquet_path.mkdir(parents=True, exist_ok=True)

OHLCV_PATH = direction/"DATALAKE"/"parquet"/"ohlcv"
OHLCV_PATH.mkdir(parents=True, exist_ok=True)

MACRO_PATH = direction/"DATALAKE"/"parquet"/"macro"
MACRO_PATH.mkdir(parents=True, exist_ok=True)

# Connexion à la BD dDB
DUCKDB_PATH = direction/"DATALAKE"/"market.duckdb"
con = duckdb.connect(DUCKDB_PATH)

# Parameters pour downloading
n_years_back = 20
n_years_back_macro = 30
start_date = datetime.date.today() - datetime.timedelta(n_years_back*252)
start_date_macro = datetime.date.today() - datetime.timedelta(n_years_back_macro*252)
end_date = datetime.date.today()
fred = Fred(api_key = '7001389dfc7179ce6bbfe18fd28ad5ac')

# dowwload des datas OHLCV + MACRO
def download_data_ohlcv(ticker):
    df = yf.download(tickers = ticker,
                    start = start_date,
                    end = end_date,
                    auto_adjust=True,
                    progress = False # pour pvr enlever la barre de dwnld
                    )
    
    df.columns = [c[0].lower() if isinstance(c,tuple) else c.lower() for c in df.columns()]
    df['ticker'] = ticker

    return df

def download_data_macro(indicator):
    data = fred.get_series(indicator, 
                         observation_start=start_date,
                         observation_end=end_date)
    df = data.reset_index()
    df.columns = ["date", "value"]
    
    return df

   
# STORING DES DATAS OHLCV + MACRO
def ohlcv_storing(ticker):
    df = download_data_ohlcv(ticker)

    path = OHLCV_PATH / f"ticker={ticker}"
    path.mkdir(parents=True, exist_ok=True)

    file = path/"data.parquet"

    df.to_parquet(file)

def macro_storing(indicator):
    df = download_data_macro(indicator)

    path = MACRO_PATH / f"indicator={indicator}"
    path.mkdir(parents=True, exist_ok=True)

    file = path/"data.parquet"

    df.to_parquet(file)


# CONNECTIONS DES PARQUETS AVEC DUCKDB
def register_tables(ticker):
    con.execute(f"""CREATE VIEW IF NOT EXIST ohlcv AS
                SELECT * FROM read_parquet('{OHLCV_PATH}/**/*.parquet')
                """)
    
    con.execute(f"""CREATE VIEW IF NOT EXIST macro AS
                SELECT * FROM read_parquet('{MACRO_PATH}/**/*.parquet')
                """)

        
def main():
    for a in omega:
        data = ohlcv_storing(a)
    for m in indicators:
        indicator = macro_storing(m)

    register_tables()
    

    
if __name__ == "__main__":
    main()




