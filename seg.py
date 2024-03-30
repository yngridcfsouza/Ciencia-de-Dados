import pandas as pd
import matplotlib.pyplot as plt

# criando uma figura única que conterá os 3 gráficos
figura = plt.figure(figsize = (15, 20))
figura.suptitle('Atividade Prática\n Comparativo das ações da Tesla por 10 dias')

comparativo = open(r"C:\Users\Home\Downloads\TSLA.csv").readlines()

x = []
y = []

for i in range(len(comparativo)):
    if i > 0 and i < 11:
        linha = comparativo[i].split(",")
        x.append(linha[0])
        y.append(float(linha[3]))

# criando o 1o gráfico
figura.add_subplot(311)
plt.title('Valores mínimos do dia', pad = 0.25)
plt.plot(x, y)

# criando o 2o gráfico

x = []
y = []

for i in range(len(comparativo)):
    if i > 0 and i < 11:
        linha = comparativo[i].split(",")
        x.append(linha[0])
        y.append(float(linha[6]))


figura.add_subplot(312)
plt.bar(x, y)
plt.title('Volumes negociados do dia (volume na escala de 10^7)', pad = 0.25)

# criando o 3o gráfico

x = []
y = []

for i in range(len(comparativo)):
    if i > 0 and i < 11:
        linha = comparativo[i].split(",")
        x.append(linha[0])
        y.append(float(linha[2]))

figura.add_subplot(313)
plt.scatter(x, y)
plt.title('Valores máximos do dia', pad = 0.25)

plt.show()