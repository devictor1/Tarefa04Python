# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Faça um programa que receba um número inteiro e retorne se é primo ou não.

numero = int(input("Por favor, insira um número inteiro: "))
if numero <= 1:
    print("Seu número não é primo!")
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        print("O seu número não é primo!")
        break
else:
    print("Seu número é primo!")