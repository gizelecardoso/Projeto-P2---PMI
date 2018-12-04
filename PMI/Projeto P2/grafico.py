'''
Crie um script python que leia um arquivo CSV gerado acima
e extraia as seguintes informações e formato de graficos usando a biblioteca: matplotlib (4,0)
grafico de linhas da amplitude termica dia a dia
grafico de linha das com eixo para maiores temperaturas e eixo para as menores temperaturas dia a dia
Faça a media de temperaturas dos dias e agrupe os valores na seguinte distribuição, criando um grafico de pizza
0 a 15,99
16 a 19,99
20,00 a 25,99
26 a 29,99
30 a 35,99
36 a 40,99
Acima de 41
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

# Criando uma funcao para obter a amplitude termica de informacoes do arquivo csv
def amplitude():
    arq = open('teste5.csv', 'r')
    lines = csv.reader(arq, delimiter=';')
    amplitude = []
    dia = []
    # Lendo linha a linha do arquivo com o laco for, e calculando a amplitude
    #jogando nas variaveis do grafico
    for line in lines:
        data = line[0]
        tempMax = float(line[1])
        tempMin = float(line[2])
        amplitude.append(tempMax - tempMin)
        dia.append(data)

    # Criando grafico de linhas com as inforacoes adquiridas no for anterior
    plt.plot(dia, amplitude)
    plt.ylabel('Amplitude Termica')
    plt.xlabel('Data')
    plt.title("Amplitude Termica por Dia")
    plt.show()

    arq.close()
amplitude()

# Criando uma funcao para obter a varicao de temperatura do dia
def variacao():
    arq = open('teste5.csv', 'r')
    lines = csv.reader(arq, delimiter=';')
    tempMax = []
    tempMin = []
    data = []
    # Lendo linha a linha do arquivo com o laco for, e calculando a amplitude
    #jogando nas variaveis do grafico
    for line in lines:
        dia = line[0]
        tempMax1 = float(line[1])
        tempMin1 = float(line[2])
        tempMax.append(tempMax1)
        tempMin.append(tempMin1)
        data.append(dia)

    plt.plot(tempMin, tempMax, data)
    plt.ylabel('Variacao de Temperatura do Dia')
    plt.xlabel('Data')
    plt.title("Temperaturas Maximas e Minimas do Dia")
    plt.show()

    arq.close()
variacao()

#Criando uma funcao que com dados do csv calcula a media de temperaturas e coloca em um grafico de pizza
def media():
    arq = open('teste5.csv', 'r')
    lines = csv.reader(arq, delimiter=';')
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    total = 0
    # Lendo linha a linha do arquivo com o laco for, e calculando a amplitude
    #jogando nas variaveis do grafico
    for line in lines:
        tempMax = float(line[1])
        tempMin = float(line[2])
        media = (tempMax + tempMin) / 2
        total = total + 1
        #Criando uma condicao como solicitado para separacao em grupos que sera colocado no grafico
        if media >= 0 and media <= 15.99:
            cont1 = cont1 + 1
        elif media >= 16.00 and media <= 19.99:
            cont2 = cont2 + 1
        elif media >= 20.00 and media <= 25.99:
            cont3 = cont3 + 1
        elif media >= 26.00 and media <= 29.99:
            cont4 = cont4 + 1
        elif media >= 30.00 and media <= 35.99:
            cont5 = cont5 + 1
        elif media >= 36.00 and media <= 40.99:
            cont6 = cont6 + 1
        elif media >= 41.00:
            cont7 = cont7 + 1
        else:
            print("Media errada")
    #Calculando a porcentagem dos grupos separados no elif anterior para colocar no grafico
    porc1 = (cont1 / total)*100
    porc2 = (cont2 / total)*100
    porc3 = (cont3 / total)*100
    porc4 = (cont4 / total)*100
    porc5 = (cont5 / total)*100
    porc6 = (cont6 / total)*100
    porc7 = (cont7 / total)*100

    #Comecando a criar o grafico de pizza
    labels = "0 a 15,99", "16 a 19,99", "20,00 a 25,99", "26 a 29,99", "30 a 35,99", "36 a 40,99", "Acima de 41"
    sizes = [porc1, porc2, porc3, porc4, porc5, porc6, porc7]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that is drawn as a circle.
    plt.title("Temperaturas Medias Diarias")

    plt.show()

    arq.close()
media()
