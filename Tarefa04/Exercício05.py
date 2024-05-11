# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

numero = float(input("Digite um valor qualquer!"))
if numero < 0:
    print("O seu número é negativo!")
elif numero == 0:
    print("O seu número é zero!")
else:
    print("O seu número é positivo!")