import quandl

gold_price = quandl.get("WGC/GOLD_DAILY_USD", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
gold_futures = quandl.get("CHRIS/CME_GC1", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
silver_futures = quandl.get("CHRIS/CME_SI1", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
copper_futures = quandl.get("CHRIS/CME_HG2", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
crude_oil_futures = quandl.get("EIA/PET_RCLC1_D", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
dollar_index = quandl.get("FRED/DTWEXB", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
EUR_USD = quandl.get("BOE/XUDLERD", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
USD_GBP = quandl.get("BOE/XUDLUSS", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
USD_CNY = quandl.get("CUR/CNY", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
SNP_TSX = quandl.get("YAHOO/INDEX_GSPTSE", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
hang_seng = quandl.get("YAHOO/INDEX_HSI", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")
nikkei_225 = quandl.get("YAHOO/INDEX_N225", authtoken="tbTSHmzg4fvb5zRiCGdU", start_date="1980-01-01", end_date="2017-01-01")

gold_price.to_csv('gold_price.csv')
gold_futures.to_csv('gold_futures.csv')
silver_futures.to_csv('silver_futures.csv')
copper_futures.to_csv('copper_futures.csv')
crude_oil_futures.to_csv('crude_oil_futures.csv')
dollar_index.to_csv('dollar_index.csv')
EUR_USD.to_csv('EUR_USD.csv')
USD_GBP.to_csv('USD_GBP.csv')
USD_CNY.to_csv('USD_CNY.csv')
SNP_TSX.to_csv('SNP_TSX.csv')
hang_seng.to_csv('hang_seng.csv')
nikkei_225.to_csv('nikkei_225.csv')

print('done!')