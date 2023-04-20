"""
09. Um motorista deseja colocar no tanque do seu carro X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
"""
# Entrada de Dados 
preco_gasolina = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

# Processamento
litros_gasolina = valor_pagamento / preco_gasolina

# Saida de Dados 
print("Com R$ {:.2f}, é possível colocar {:.2f} litros de gasolina no tanque.".format(valor_pagamento, litros_gasolina))
