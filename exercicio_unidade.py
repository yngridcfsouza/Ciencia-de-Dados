import pandas as pd
import matplotlib.pyplot as plt

# criando uma figura única que conterá os 3 gráficos
figura = plt.figure(figsize = (20, 5))
figura.suptitle('Atividade Prática')

comparativo = open(r"C:\Users\Home\Downloads\USD_BRL_hist.csv").readlines()

x = []
y = []

for i in range(len(comparativo)):
    if i > 0 and i < 500:
        linha = []
        linha = comparativo[i].split(",")
        x.append(linha[0])
        y.append(linha[1])

# criando o 1o gráfico
figura.add_subplot(131)
plt.plot(x, y)

plt.show()
