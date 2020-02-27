# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string
import unicodedata

Posi = 0;
saida = ""
letras =  string.ascii_lowercase # Somente as letras minusculas
param = sys.argv[1:]  # entrada de parametros

if len(param)==3:  # Testa se a quantidade de parametros é correta
    arqTextoClaro = param[0]
    chave = param[1]
    nomesaida= param[2]

else:
    print('Quantidade de parametros invalida! \n Passe o diretorio do arquivo txt , digite a chave e o nome do arquivo de saida.\n')
    print('Exemplo: $ python cifrador.py teste.txt lucas saidacifrada.txt\n')
    exit()
    
chave = chave.lower()  # Coloca a chave toda em miniscula

chave = [line.replace(' ', '') for line in chave]
chave = [line.replace('y', '') for line in chave]

    
Alfabeto = [] # Cria o alfabeto sem a letra Y
for i in letras:
    Alfabeto.append(i)
Alfabeto.remove('y')
   




   #Abrir o arquivo
with open(arqTextoClaro, 'r') as f:
    lines = f.readlines()

    ##remove os espaços em branco e caracteres especiais
    lines = [line.replace(' ', '') for line in lines]
    lines = [line.replace('#', '') for line in lines]
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.replace('\t', '') for line in lines]
    lines = [line.replace('\r', '') for line in lines]
    lines = [line.replace('~', '') for line in lines]
    
    lines = [line.replace(',', '') for line in lines]
    lines = [line.replace('.', '') for line in lines]
    lines = [line.replace('?', '') for line in lines]
    lines = [line.replace('!', '') for line in lines]
    lines = [line.replace('(', '') for line in lines]
    lines = [line.replace(')', '') for line in lines]
    lines = [line.replace('"', '') for line in lines]
    lines = [line.replace('_', '') for line in lines]
    lines = [line.replace('y', '') for line in lines]
    lines = [line.replace('^', '') for line in lines]
    lines = [line.replace(',', '') for line in lines]
    lines = [line.replace('.', '') for line in lines]
    lines = [line.replace('•', '') for line in lines]
    lines = [line.replace('5', '') for line in lines]
    lines = [line.replace('4', '') for line in lines]
    lines = [line.replace('3', '') for line in lines]
    lines = [line.replace('2', '') for line in lines]
    lines = [line.replace('1', '') for line in lines]
    lines = [line.replace('6', '') for line in lines]
    lines = [line.replace('7', '') for line in lines]
    lines = [line.replace('8', '') for line in lines]
    lines = [line.replace('9', '') for line in lines]
    lines = [line.replace('0', '') for line in lines]
    lines = [line.lower() for line in lines]
    
   

    #Escreve um novo arquivo sem espaços // Atualiza o arquivo
with open(arqTextoClaro, 'w') as f:
    f.writelines(lines)



textosemespaco = open(arqTextoClaro,'r') # Abre e le o texto sem espaço atualizado
textosemespaco =textosemespaco.read()

textosemespaco = ''.join(ch for ch in unicodedata.normalize('NFKD', textosemespaco)if not unicodedata.combining(ch)) # tira os acentos
print(textosemespaco)



textoseparado=[]
i =0 # Auxilar percorerr a string

while (i < len(textosemespaco)-1):  # Enquanto o auxiliar for menor que a quantidade de caracteres, junta os caracteres em pares e adiciona X se casso as letras se repetirem ou seja quantiadde impar
    
    letra1 = textosemespaco[i]
    letra2 = textosemespaco[i+1]
    if(letra1 == letra2):  # Se o par de caracteres selecionado forem iguais adiciona um x seguido do primeiro caractere
        textoseparado.append(letra1 )
        textoseparado.append("x")
        i = i+1
    elif(letra1 != letra2):  # Se forem diferentes apenas separa em pares numa lista
        textoseparado.append(letra1)
        textoseparado.append(letra2)
        i = i+2

if(i<len(textosemespaco)):  # Caso seja impar o numero de caracteres o ultimo faz par com um X
    textoseparado.append(textosemespaco[i])
    textoseparado.append("x")



#print(textoseparado)
matriz =  [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # Inicia-se a Matriz de encriptarr




auxlinha=0
auxcoluna=0

for i in chave: # Percorre a matriz adicionando a chave nas primeiras linhas e colunas da esquerda para direita
    if(i in Alfabeto):
        if(auxcoluna>=5):
            auxcoluna = 0
            auxlinha += 1
        matriz[auxlinha][auxcoluna]=i # Adiciona o caractere na matriz 
        Alfabeto.remove(i)        # Remove do alfabeto para nao repetir
        auxcoluna+=1
        
for i in Alfabeto:  # Percorre o resto do alfabeto adicionando nos locais vagos da matriz o restante do algf
    if(auxcoluna>=5):
            auxcoluna = 0
            auxlinha += 1
    matriz[auxlinha][auxcoluna]=i
    auxcoluna+=1
    
    

print(matriz)
print(chave)


def PercorreMatriz(locPrimeiraLetra,locSegundaLetra,saida, aux):
     
        if (locPrimeiraLetra[0] == locSegundaLetra[0]): # estao na mesma linha //  troque-as pela letra imediatamente a direita 
            auxcoluna = (locPrimeiraLetra[1]+aux)
           
            if(auxcoluna==5): # Testa a condicao para manter a forma circular
                auxcoluna =0
            
            auxcoluna2 = (locSegundaLetra[1]+aux)
            if(auxcoluna2==5):  # Testa a condicao para manter a forma circular
                auxcoluna2 =0
            
            saida =saida + matriz[locPrimeiraLetra[0]][(auxcoluna)] + matriz[locSegundaLetra[0]][(auxcoluna2)]
            
        
        elif (locPrimeiraLetra[1] == locSegundaLetra[1]): # estao na mesma coluna troque-as pela letra imediatamente abaixo
            auxlinha =locPrimeiraLetra[0]+aux
            if(auxlinha==5):  # Testa a condicao para manter a forma circular
                auxlinha=0
            auxlinha2 = locSegundaLetra[0]+aux
            if(auxlinha2==5):  # Testa a condicao para manter a forma circular
                auxlinha2=0
            saida = saida + matriz[auxlinha][locPrimeiraLetra[1]] + matriz[auxlinha2][locSegundaLetra[1]]
    
        elif ( locPrimeiraLetra[1] != locSegundaLetra[1] and locPrimeiraLetra[0] != locSegundaLetra[0]): # estao em linhas e colunas diferentes // a é trocada pela letra que esta em sua linha e
#que está na mesma coluna de seu par
            saida =saida+ matriz[locPrimeiraLetra[0]][locSegundaLetra[1]] + matriz[locSegundaLetra[0]][locPrimeiraLetra[1]]

        return saida




while (Posi < len(textoseparado)): # Enquanto nao percorrer todo texto claro
        
        
        primeiraLetra = textoseparado[Posi] # Pega a primeira letra e a segunda
        segundaLetra = textoseparado[Posi+1]
     
        for i, x in enumerate(matriz): # Busca a primeira letra na matriz
            if primeiraLetra in x:
               locPrimeiraLetra= [i, x.index(primeiraLetra)]
        for i, x in enumerate(matriz):  # Busca a segunda letra na matriz
            if segundaLetra in x:
                locSegundaLetra= [i, x.index(segundaLetra)]
        
        
       
        saida = PercorreMatriz(locPrimeiraLetra,locSegundaLetra,saida,1)
        
        Posi+=2 # Anda duas posições pois o texto é cifrado em duplas de letras
        
 



        
print (saida)
f = open(nomesaida, "w")
f.write(saida)
f.close()

