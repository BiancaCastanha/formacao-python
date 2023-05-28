saldo = 2000.0
opcao = int(input("Informe uma opção:\n[1] Sacar\t[2] Extrato\n"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    if saldo >= valor:
        print("Realizando Saque!")
    else:
        print("Saldo Insuficiente!")
    #IF TERNÁRIO
    #status = "Sucesso" if saldo >= saque else "Falha"
    #print(f"{status} na operação")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")
  
'''
MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")
'''

