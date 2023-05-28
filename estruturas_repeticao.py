#Repetição com FOR

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()


#tabuada do 7
for numero in range(0, 71, 7):
    print(numero, end=" ")

#Repetição com WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("Informe uma opção:\n[1] Sacar\t[2] Extrato\t[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    else:
        break
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")