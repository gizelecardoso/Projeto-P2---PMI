#Importando biblioteca
import csv
#Função para gravar entrada de dados em arquivo .csv
def gravCSV (dados):
    arq = open('PMI_2.csv', 'a')
    c = csv.writer(arq, delimiter=';')
    c.writerow(dados)
    arq.close()
#Variáveis
data = input("Data: ")
tempMin = float(input("Digite a temperatura mínima: "))
tempMax = float(input(("Digite a temperatura máxima: ")))

#integrando parâmetro às variáveis
dados = [data,tempMin,tempMax]
#Comando de execução da função
gravCSV(dados)