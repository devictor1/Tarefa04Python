# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um programa que peça ao usuário para digitar três números e retorne o maior deles.

numero1 = float(input("Insira abaixo um número qualquer"))
numero2 = float(input("Agora, insira um segundo número"))
numero3 = float(input("Por último, insira mais um número"))

if numero1 > numero2:
    if numero2 > numero3:
        print("O maior dos números é o", numero1)
    elif numero3 > numero1:
         print("O maior dos números é o", numero3)
elif numero2 > numero3:
    if numero3 > numero1:
        print("O maior dos números é o", numero2)
    elif numero1 > numero2:
        print("O maior dos números é o", numero1)
elif numero3 > numero1:
    if numero1 > numero2:
        print("O maior dos números é o", numero3)
    elif numero2 > numero3:
        print("O maior dos números é o", numero2)
    
