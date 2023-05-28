menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")
        valor = float(input("Informe o valor desejado para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou! Valor inválido.")

    elif opcao == 2:
        print("Saque")
        valor = float(input("Informe o valor desejado para saque: "))
        if valor > saldo:
            print("Operação Falhou! Valor requisitado para saque maior que saldo disponível.")
        elif valor > limite:
            print("Operação Falhou! Valor requisitado para saque maior que limite disponível.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação Falhou! Número máximo de saques diários alcançado.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"{numero_saques}º do dia")
            if numero_saques == 3:
                print("Número máximo de saques diários alcançado.\nPróximo saque disponível apenas amanhã")
        else:
            print("Operação Falhou! Valor requisitado inválido.")
    
    elif opcao == 3:
        print("\n########## Extrato ##########")
        if not extrato:
            print("\nNenhuma movimentação realizada")
        else:
            print(f"\n{extrato}")
            print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n#############################")
    elif opcao == 0:
        break
    
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")