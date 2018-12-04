import csv
import matplotlib.pyplot as plt

# Função que lê dados de um arquivo csv e calcula a amplitude térmica
def amplitudeT():
    arq = open('PMI_2.csv', 'r')
    lines = csv.reader(arq,
                       delimiter=';')
    m = []
    n = []
    # Estrutura de repetição que lê linha a linha do arquivo
    for line in lines:
        p0 = line[0]
        p1 = float(
            line[1])
        p2 = float(
            line[2])
        m.append(
            p2 - p1)
        n.append(p0)

    # Identificando quais serão os vértices do gráfico, sendo n o vértice x e m o vértice y e o nome dos labels
    plt.plot(n, m)
    plt.ylabel('Amplitude Térmica')
    plt.xlabel('Data')
    plt.title("Amplitude Térmica Dia a Dia")
    plt.show()

    arq.close()
amplitudeT()

# Função que lê dados de um arquivo csv e calcula a variação de temperatura por dia
def variacaoDia():
    arq = open('PMI_2.csv', 'r')
    lines = csv.reader(arq, delimiter=';')
    m = []
    n = []
    o = []
    # Estrutura de repetição que lê linha a linha do arquivo
    for line in lines:
        p0 = line[0]
        p1 = float(line[1])
        p2 = float(line[2])
        m.append(p1)
        o.append(p2)
        n.append(p0)

    plt.plot(n, m, o)
    plt.ylabel('Variação Diária')
    plt.xlabel('Data')
    plt.title("Temp Mín e Máx Dia a Dia")
    plt.show()

    arq.close()
variacaoDia()

# Função que lê dados de um arquivo csv e calcula a média em um gráfico de pizza
def mediaT():
    arq = open('PMI_2.csv', 'r')
    lines = csv.reader(arq, delimiter=';')
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cTot = 0
    # Estrutura de repetição que lê linha a linha do arquivo
    for line in lines:
        p1 = float(line[1])
        p2 = float(line[2])
        i = (p1 + p2) / 2
        cTot = 0
        cTot = cTot + 1
        #Condicional que segrega os setores do gráfico
        if i >= 0 and i <= 15.99:
            cont1 = cont1 + 1
        elif i >= 16.00 and i <= 19.99:
            cont2 = cont2 + 1
        elif i >= 20.00 and i <= 25.99:
            cont3 = cont3 + 1
        elif i >= 26.00 and i <= 29.99:
            cont4 = cont4 + 1
        elif i >= 30.00 and i <= 35.99:
            cont5 = cont5 + 1
        elif i >= 36.00 and i <= 40.99:
            cont6 = cont6 + 1
        elif i >= 41.00:
            cont7 = cont7 + 1
        else:
            print("Média errada")
    #calculo da porcentagem ceda setor
    porc1 = cont1 / cTot
    porc2 = cont2 / cTot
    porc3 = cont3 / cTot
    porc4 = cont4 / cTot
    porc5 = cont5 / cTot
    porc6 = cont6 / cTot
    porc7 = cont7 / cTot

    labels = "0 a 15,99", "16 a 19,99", "20,00 a 25,99", "26 a 29,99", "30 a 35,99", "36 a 40,99", "Acima de 41"
    sizes = [porc1, porc2, porc3, porc4, porc5, porc6, porc7]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that is drawn as a circle.
    plt.title("Rank de Temperaturas Médias Diarias")

    plt.show()

    arq.close()
mediaT()


