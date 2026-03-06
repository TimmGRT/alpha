import yfinance as yf
import pandas as pd
import duckdb 
from pathlib import Path
from omega_choice import omega
import datetime
from IPython.display import display

# Parameters pour le ciblage de la loc du fichier d'installation 
current_file = Path(__file__).resolve()
direction = current_file.parent.parent
#Création du datalake dans le folder, du directory parquet et de la BD dDB
Data_parquet_path = direction/"DATALAKE"/"parquet"
Data_parquet_path.mkdir(parents=True, exist_ok=True)
# Création de la BD dDB
Data_duckDB_path = direction/"DATALAKE"/"market.duckdb"
con = duckdb.connect(Data_duckDB_path)


# Parameters pour downloading
n_years_back = 20
start_date = datetime.date.today() - datetime.timedelta(n_years_back*252)
end_date = datetime.date.today()

# dowwload des datas 

def download_data_asset(omega):
    data = yf.download(tickers = omega,
                       start = start_date,
                       end = end_date,
                       auto_adjust=True,
                       progress = False # pour enlever la barre de dwnld
                       )
    
    return(data)

#data = download_data_asset(omega)
#display(data)


# %%
