# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) ela possui.

frase = input("Digite uma frase!")
vogais = "aeiou"
contador = 0

for letra in frase.lower():
    if letra in vogais:
        contador += 1

print("A quantidade de vogais é",contador)