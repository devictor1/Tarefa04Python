# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual
# ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Bem-vindo! Digite a nota da sua primeira avaliação."))
nota2 = float(input("Obrigado! Agora, digite a nota da sua segunda avaliação."))

media = (nota1+nota2)/2

print("Parabéns! Você foi aprovado com uma média de", media) if media >= 6 else print("Infelizmente você foi reprovado com uma média de",media)