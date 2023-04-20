"""
03. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
"""
# Entrada de De Dados 
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# Processamento
percentagem_distribuidor = 0.28
impostos = 0.45
custo_consumidor = custo_fabrica + (percentagem_distribuidor * custo_fabrica) + (impostos * custo_fabrica)

# Saida de Dados 
print("O custo ao consumidor do carro é R$ {:.2f}".format(custo_consumidor))
