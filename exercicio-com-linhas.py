from pandas import read_csv
from matplotlib import pyplot

origemDosDados = read_csv(r"C:\Users\Home\Downloads\USD_BRL_hist.csv", header = 0, 
index_col = 0, parse_dates = True, squeeze = True)

periodo = origemDosDados["01-01-2010":"31-12-2019"]
periodo.plot()

pyplot.show()