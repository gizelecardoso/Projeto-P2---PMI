'''
Crie um script em python que faça a entradas de 3 valores:

Data
Temperatura minima
Temperatura máxima
Armazene estes valore em arquivo CSV, 
cada valor vai ocupar uma coluna e o 
arquivo deve ser atualizado a cada execução do script (3,0)

'''

#Importando csv para pegar informa�oes
import csv

#Criando funcao para gravar em um vetor as informacoes que serao armazenadas no arquivo csv
def gravarCSV(vetor):
    #Abrindo arquivo csv
    arq = open('teste5.csv','a')
    #delimitando as informacoes desse arquivo com ; - padrao do csv e excel
    c = csv.writer(arq, delimiter=';')
    #Colocando na variavel anterior as informacoes escritas logo apos.
    c.writerow(vetor)
    #fechando a funcao
    arq.close()

#pegando informacoes digitadas pelo usuario e guardando nas variaveis
data = (input("Informe a Data:"))
tempMax = float(input("Informe a Temperatura Maxima:"))
tempMin = float(input("Informe a Temperatura Minima: \n"))

#Colocando os valores armazenados nas variaveis na variavel gerada na funcao(vetor) para o arquivo csv
vetor = [data, tempMax, tempMin]

#Chamando a funcao para execucao
gravarCSV(vetor)

