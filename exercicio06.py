"""
06. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

"""
# Entrada de Dados 
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processamento
media = (nota1 + nota2 + nota3) / 3

# Saida de Dados 
print("O aluno {} obteve média {:.2f}".format(nome, media))
