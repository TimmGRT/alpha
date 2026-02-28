
omega_sectorial = {"tech" : ['AAPL', 'MSFT', 'NVDA', 'AMD', 'ORCL', 'CRM', 'INTC', 'ADP', 'CSCO', 'IBM', 'TXN', 'QCOM', 'AVGO', 'MU', 'HPQ', 'AMAT', 'LRCX', 'SNPS', 'NOW', 'ZS', 'PANW', 'ADBE', 'MSFT', 'SWKS', 'FISV', 'CDNS', 'KLAC', 'ATVI', 'V', 'MA'],
         "health" : ['JNJ', 'PFE', 'MRK', 'UNH', 'ABBV', 'BMY', 'GILD', 'AMGN', 'MDT', 'SYK', 'DHR', 'ISRG', 'ZBH', 'BIIB', 'LLY', 'REGN', 'VRTX', 'HCA', 'TMO', 'ABT'],
         "finance" : ['JPM', 'BAC', 'C', 'GS', 'MS', 'WFC', 'BK', 'SCHW', 'CME', 'ICE', 'SPGI', 'AXP', 'COF', 'USB', 'PNC', 'BLK', 'TFC', 'STT', 'RJF', 'AMP'],
         "disc_cons" : ['AMZN', 'MCD', 'SBUX', 'HD', 'NKE', 'LOW', 'TGT', 'COST', 'TJX', 'MAR', 'ROST', 'YUM', 'DRI', 'LVS', 'WYNN'],
         "basics_cons" : ['KO', 'PG', 'PEP', 'WMT', 'COST', 'CL', 'MDLZ', 'KMB', 'WBA', 'GIS'],
         "industry" : ['BA', 'CAT', 'DE', 'GE', 'HON', 'LMT', 'RTX', 'NOC', 'ITW', 'PH', 'MMM', 'EMR', 'CMI', 'FLS', 'TXT'],
         "energy" : ['XOM', 'CVX', 'COP', 'SLB', 'PSX', 'EOG', 'OXY', 'VLO', 'HAL', 'MPC'],
         "materials" : ['LIN', 'DD', 'NUE', 'FCX', 'APD'],
         "telecom" : ['T', 'VZ', 'TMUS', 'CMCSA', 'DISH'],
         "utilities" : ['NEE', 'DUK', 'SO', 'AEP', 'EXC'],
         "imo" : ['PLD', 'AMT', 'SPG', 'PSA', 'O']
}
omega = [item for sublist in omega_sectorial.values() for item in sublist]
