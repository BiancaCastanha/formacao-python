#Operadores Aritméticos

#Adição
print(5+2)
#Subtração
print(10-2)
#Multiplicação
print(4*5)
#Divisão
print(13/3)
#Divisão Inteira
print(13//3)
#Módulo (resto da divisão)
print(12%5)
#Exponenciação
print(2**3)
print('\n')

#Operadores de Comparação

saldo = 450
saque = 200

#Igualdade
print(saldo == saque)
#Diferença
print(saldo != saque)
#Maior
print(saldo > saque)
#Maior ou igual
print(saldo >= saque)
#Menor
print(saldo < saque)
#Menor ou igual
print(saldo <= saque)
print('\n')

#Operadores de Atribuição
saldo = 500
saldo += 200
print(saldo)

saldo = 500
saldo -= 100
print(saldo)

saldo = 500
saldo *= 2
print(saldo)

saldo = 500
saldo /= 5
print(saldo)

saldo = 500
saldo //= 5
print(saldo)

saldo = 500
saldo %= 480
print(saldo)

saldo = 80
saldo **= 2
print(saldo)
print('\n')

#Operadores Lógicos

saldo = 1000
saque = 200
limite = 100
contatos_emergencia = []
#Operador E (AND)
print("\n")
print(saldo >= saque and saque <= limite)
#Operador OU (OR)
print("\n")
print(saldo >= saque or saque <= limite)
#Operador NOT
print("\n")
print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500")
print(not "")

#Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True
print("\n")
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
print("\n")

#Operadores de Identidade
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)
print("\n")

#Operadores de Associação
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 1000]

print("Python" in curso)
print("de" in curso)
print("maçã" not in frutas)
print(200 in saques)