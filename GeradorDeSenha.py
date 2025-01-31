#Hard Form
import random

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['!', '#','&','$']

print('Bem vindo ao Gerador de Senhas')
nr_letras = int(input('Quantas letras gostaria de ter em sua senha:\n'))
nr_numeros = int(input(f'Quantos simbolos voce gostaria:\n'))
nr_simbolos = int(input(f'Quantos numeros gostaria:\n'))

senha_list = []

for letra in range(0, nr_letras):
    senha_list.append(random.choice(letras))
    
for numero in range(0, nr_numeros):
    senha_list.append(random.choice(numeros))
     
for simbolo in range(0, nr_simbolos):
    senha_list.append(random.choice(simbolos))
    

random.shuffle(senha_list)

senha = ''
for char in senha_list:
    senha += char

print(f'Sua senha é: {senha}')