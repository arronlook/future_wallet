import modelfactory as mf
from modelpack import ModelType
import pandas as pd
import dbutil

if __name__ == "__main__":
	print('Starting...')
	mfac = mf.ModelFactory()
	engine = dbutil.connect_engine('modeldata')
	print('DB Engine connected...')

	wages = []
	industryCodes = None
	tickers = None
	with engine.connect() as conn:
		industryCodes = pd.read_sql("SELECT DISTINCT IndustryCode FROM CBPIncome WHERE IndustryCode LIKE '%///'", con=conn)
		tickers = pd.read_sql("WITH Tickers AS (SELECT DISTINCT Ticker FROM Stocks) SELECT TOP 5 PERCENT Ticker FROM Tickers ORDER BY newid();", con=conn)

	industryCodes = industryCodes['IndustryCode'].tolist()
	tickers = tickers['Ticker'].tolist()
	print('Industry Codes and Tickers loaded...')


	for i in industryCodes:
		print('Wage model ' + i + ' loaded')
		wages.append(mfac.createModel(ModelType.WAGES, train=True, industryCode=i))
	print('Wages models created...')
	investments = mfac.createModel(ModelType.INVESTS, train=True, tickers=tickers)
	print('Investment models created...')
	assets = mfac.createModel(ModelType.ASSETS, train=True)
	print('Asset models saved...')

	for w in wages:
		w.train(50, 100000)
		wages.save('F:/ServerData/FutureWallet/models/')
	
	print('Wage models saved...')

	investments.train(50, 100000)
	assets.train(50, 100000)

	investments.save('F:/ServerData/FutureWallet/models/')
	print('Investment models saved...')
	assets.save('F:/ServerData/FutureWallet/models/')
	print('Asset models saved...')