#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:20:12 2019

@author: steffens
"""

import sys
import string
import unicodedata

Posi = 0;
saida = ""
letras =  string.ascii_lowercase # Somente as letras minusculas
param = sys.argv[1:]  # entrada de parametros

if len(param)==2:  # Testa se a quantidade de parametros é correta
    arqTextoClaro = param[0]
    chave = param[1]

else:
    print('Quantidade de parametros invalida! \n Passe o diretorio do arquivo txt cifrado e digite a chave.\n')
    print('Exemplo: $ python decifrador.py saidacifrada.txt lucas\n')
    exit()
    
chave = chave.lower()  # Coloca a chave toda em miniscula

    
Alfabeto = [] #Cria o alfabeto removendo o Y
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
    lines = [line.replace(',', '') for line in lines]
    lines = [line.replace('.', '') for line in lines]
    lines = [line.replace('?', '') for line in lines]
    lines = [line.replace('!', '') for line in lines]
    lines = [line.replace('(', '') for line in lines]
    lines = [line.replace(')', '') for line in lines]
    lines = [line.replace('"', '') for line in lines]
    lines = [line.replace('_', '') for line in lines]
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












matriz =  [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # Inicia-se a Matriz de encriptarr




auxlinha=0
auxcoluna=0

for i in chave: # Percorre a matriz adicionando a chave nas primeiras linhas e colunas da esquerda para direita
    if(i in Alfabeto):
        if(auxcoluna>=5):
            auxcoluna = 0
            auxlinha =auxlinha+ 1
        matriz[auxlinha][auxcoluna]=i # Adiciona o caractere na matriz 
        Alfabeto.remove(i)        # Remove do alfabeto para nao repetir
        auxcoluna=auxcoluna+1
        
for i in Alfabeto:  # Percorre o resto do alfabeto adicionando nos locais vagos da matriz o restante do algf
    if(auxcoluna>=5):
            auxcoluna = 0
            auxlinha = auxlinha+ 1
    matriz[auxlinha][auxcoluna]=i
    auxcoluna+=1
    
    



textoseparado=[]


i =0 # Auxilar percorerr a string

while (i < len(textosemespaco)):  # Separa o texto em uma lista
    letra1 = textosemespaco[i]
   
    textoseparado.append(letra1 )
    i=i+1
    
    
def PercorreMatriz(locPrimeiraLetra,locSegundaLetra,saida,aux): # Percorre a matriz e aplica as regras da criptografia
    
    
        if (locPrimeiraLetra[0] == locSegundaLetra[0]): # estao na mesma linha //  troque-as pela letra imediatamente a direita 
            auxcoluna = (locPrimeiraLetra[1]+aux)
           
            if(auxcoluna==5): # Testa a condicao para manter a forma circular
                auxcoluna =0
            
            auxcoluna2 = (locSegundaLetra[1]+aux)
            if(auxcoluna2==5):  # Testa a condicao para manter a forma circular
                auxcoluna2 =0
            
            saida = saida + matriz[locPrimeiraLetra[0]][(auxcoluna)] + matriz[locSegundaLetra[0]][(auxcoluna2)]
            
        
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

while (Posi < len(textoseparado)): # Enquanto nao percorrer todo texto 
        
        
        primeiraLetra = textoseparado[Posi] # Pega a primeira letra e a segunda
        segundaLetra = textoseparado[Posi+1]
     
        for i, x in enumerate(matriz): # Busca a primeira letra na matriz
            if primeiraLetra in x:
                locPrimeiraLetra= [i, x.index(primeiraLetra)]
        for i, x in enumerate(matriz):  # Busca a segunda letra na matriz
            if segundaLetra in x:
               locSegundaLetra= [i, x.index(segundaLetra)]
        
        saida = PercorreMatriz(locPrimeiraLetra,locSegundaLetra,saida,-1)
       
        
        Posi+=2 # Anda duas posições pois o texto é cifrado em duplas de letras
        


a=[]
for letter in saida:  # Manipula o texto para remover os X a mais
            a.append(letter)



    
i=0
while i <len(a)-2:  # remove o x do meio das letras iguais 
    if(a[i]==a[i+2] and a[i+1]=='x'):
        a[i+1] =''
    i+=1
if(a[-1]=='x'):  #remove X adicionado nas palavras impares
    del(a[-1])


with open('saidadecifrada.txt', 'w') as f:
        f.writelines(a)
with open("saidadecifrada.txt", 'r') as f:
        lines = f.readlines()

lines = [print(line) for line in lines]


        

        



