"""01 A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
∆t: variação de tempo (tempo final – tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  
"""
#Entrada de Dados 
delta_s = float(input("Digite a variação de espaço em quilômetros: "))
delta_t = float(input("Digite a variação de tempo em horas: "))

#Processamento
velocidade_media = delta_s / delta_t

# Saida
print("A velocidade média é", velocidade_media, "km/h")


