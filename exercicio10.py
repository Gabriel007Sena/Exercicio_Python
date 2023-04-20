"""
10.Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.
"""
# Entrada de Dados 
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor: "))

# Processamento
comissao = 0.15 * total_vendas

salario_final = salario_fixo + comissao

# Saida de Dados 
print("Nome do vendedor:", nome)
print("Salário fixo: R$ {:.2f}".format(salario_fixo))
print("Salário final: R$ {:.2f}".format(salario_final))
