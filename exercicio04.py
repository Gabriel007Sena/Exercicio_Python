"""
04. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto
"""
# Entrada de Dados 
distancia_total = float(input("Digite a distância total percorrida em km: "))
combustivel_gasto = float(input("Digite o total de combustível gasto em litros: "))

# Processamento
consumo_medio = distancia_total / combustivel_gasto

# Saida de Dados 
print("O consumo médio do automóvel é de {:.2f} km/l".format(consumo_medio))
