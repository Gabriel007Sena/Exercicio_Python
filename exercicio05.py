"""
05. Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.
"""
# Entrada de Dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Processamento
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

# Saida de Dados
print("Soma: {:.2f}".format(soma))
print("Subtração: {:.2f}".format(subtracao))
print("Multiplicação: {:.2f}".format(multiplicacao))
print("Divisão: {:.2f}".format(divisao))
