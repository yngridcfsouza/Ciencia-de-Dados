from pandas import read_csv
from matplotlib import pyplot

# criando uma figura única que conterá os 3 gráficos
figura = pyplot.figure(figsize = (10, 5))
figura.suptitle('Atividade Prática')

# criando o 1o gráfico
figura.add_subplot(131)
comparativo1 = read_csv(r"C:\Users\Home\Downloads\USD_BRL_hist.csv", header = 0, 
index_col = 0, parse_dates = True, squeeze = True)

comparativo_p1 = comparativo1["01-01-2010":"31-07-2010"]
comparativo_p1.plot(x = ['Data'], y = ['USD_BRL'])

pyplot.show()

# criando o 2o gráfico
figura.add_subplot(132)
comparativo2 = read_csv(r"C:\Users\Home\Downloads\USD_BRL_hist.csv", header = 0, 
index_col = 0, parse_dates = True, squeeze = True)

comparativo_p2 = comparativo2["01-01-2010":"31-07-2011"]
comparativo_p2.plot(x = ['Data'], y = ['USD_BRL'])

pyplot.show()




# criando o 1o gráfico
figura.add_subplot(131)
plt.plot(x, y)

# criando o 2o gráfico
figura.add_subplot(132)
plt.scatter(x, y)

# criando o 3o gráfico
figura.add_subplot(133)
plt.bar(x, y)

plt.show()