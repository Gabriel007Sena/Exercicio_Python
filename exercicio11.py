"""
11. Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.
"""
# Entrada de Dados 
valor_depositado = float(input("Digite o valor depositado: "))
# Processamento
taxa_juros = 0.007 # 0,70% a.m.
valor_rendimento = valor_depositado * (1 + taxa_juros)
# Saida de Dados 
print(f"O valor com rendimento após um mês é: R${valor_rendimento:.2f}")
