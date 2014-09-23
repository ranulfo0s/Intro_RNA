'''
Created on Sep 21, 2014

@author: plutarco
'''

import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt

#Manipulacao dos dados de entrada do arquivo txt
dados_entrada = ""
with open("EntradasG.txt") as file:
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        dados_entrada += line
array_entrada = dados_entrada.rstrip().split("#")
sinais_entrada = np.genfromtxt(StringIO(array_entrada[0]), delimiter=",")

#n representa quantidade de conjunto de sinais de entrada recebidos
n = np.genfromtxt(StringIO(array_entrada[1]), delimiter=",")
pesos = np.genfromtxt(StringIO(array_entrada[2]), delimiter=",")
teta = np.genfromtxt(StringIO(array_entrada[3]), delimiter=",")
g =  np.genfromtxt(StringIO(array_entrada[4]), delimiter=",")

#Multiplicacao de matrizes para adquirir a combinacao linear
combinador_linear = np.dot(sinais_entrada,pesos)

print(combinador_linear)

u = np.subtract(combinador_linear,teta)

print(u)
y = []

#Funcoes para utilizar na funcao de ativacao
def func_degree(u):
    if u >= 0:
        return 1
    else:
        return 0

def func_tang_hiperb(u,b):
    return (1-np.exp(-b*u))/(1+np.exp(-b*u))

def func_logis(u,b):
    return 1/(1+np.exp(-b*u))

#Caso a funcao de ativacao seja a funcao de Degrau
if(g == 0):
    for x in range(n):
        y.append(func_degree(u[x]))


#Caso a funcao de ativacao seja a funcao tangente hiperbolica
if(g == 1):
    beta = 1
    for x in range(n):
        y.append(func_tang_hiperb(u[x], beta))
#Caso a funcao de ativacao seja a funcao logistica        
if(g == 2):
    beta = 1
    for x in range(n):
        y.append(func_logis(u[x], beta))


print(y)

x1 = list(zip(*sinais_entrada)[0])
x2 = list(zip(*sinais_entrada)[1])  

plt.plot(x1, y, "-b")
plt.plot(x2, y, "-r")
plt.xlabel('Sinais de Entrada') 
plt.ylabel('Funcao de Ativacao: g(u)',rotation='vertical')
plt.title("Questao 2 - G")
plt.xlim(0)
plt.ylim(0)

plt.grid(True)
plt.savefig('questaoG.png') 
plt.show()
    

                                                                                
        
