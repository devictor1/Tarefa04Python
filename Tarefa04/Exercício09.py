# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se
# forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.

macasCompradas = int(input("Quantas maçãs você comprou?"))
if macasCompradas < 12:
    custoTotal = macasCompradas * 1.3
    print("O total da compra ficou", custoTotal, "reais")
else:
    custoTotal = macasCompradas
    print("O total da compra ficou", custoTotal, "reais")