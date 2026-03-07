macro = {
    "inflation": ["CPIAUCSL","CPILFESL","PCEPI","PCEPILFE","CUSR0000SA0L2","GDPDEF","PPIACO"],
    "growth": ["GDPC1","A939RX0Q048SBEA","GPDIC1","GCEC1","PCEPI","A001RD3A048NBEA"],
    "labor": ["UNRATE","PAYEMS","CIVPART","ICSA","CES0500000003","UEMPMEAN","LNS13023610"],
    "rates_yield_curve": ["FEDFUNDS","DGS1MO","DGS3MO","DGS6MO","DGS1","DGS2","DGS5","DGS10","DGS30","T10Y2Y","T10Y3M"],
    "credit": ["BAA","AAA","BAMLH0A0HYM2","H0A0FDRPPPPPT","BAMLC0A4CBBBEY","VIXCLS"],
    "money_supply": ["M1SL","M2SL","M2V","TOTRESNS","WSHOM2NS"],
    "consumption": ["PCEC96","DPCERA3M086SBEA","PCEDG","PSAVERT"],
    "production": ["INDPRO","TCU","IPFPNSS","NAPMPI"],
    "housing": ["HOUST","PERMIT","CSUSHPINSA","URMITT01USA","RECPROUSM156N"],
    "trade": ["EXPGS","IMPGS","NETEXP","BOTSLAKWN"],
    "sentiment_confidence": ["UMCSENT","CONCCONF","NFIBCONF","USSLIND"],
    "leading_indicators": ["USSLIND","NAPM","LEI","CES0600000007"],
    "global_markets": ["DTWEXB","DEXCHUS","DEXJPUS","DEXUSAL"],
    "financial_conditions": ["KCFSI","STLFSI","TEDRATE"],
    "recession_flags": ["USREC","USRECPRO","NBERRECP"]
}

indicators = [item for sublist in macro.values() for item in sublist]


if __name__ == "__main__":
    print(f"the indicator list is : {indicators}")