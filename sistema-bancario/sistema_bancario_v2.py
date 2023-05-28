import textwrap

def menu():
    menu = """\n
    ====================MENU====================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    print("Depósito")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação Falhou! Valor inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedidos = numero_saques >= limite_saques

    print("Saque")

    if saldo_excedido:
        print("Operação Falhou! Valor requisitado para saque maior que saldo disponível.")

    elif limite_excedido:
        print("Operação Falhou! Valor requisitado para saque maior que limite disponível.")

    elif saques_excedidos:
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

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n########## Extrato ##########")
    if not extrato:
        print("\nNenhuma movimentação realizada")
    else:
        print(f"\n{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n#############################")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtro_usuarios(cpf,usuarios)

    if usuario:
        print("Usuário existente com CPF providenciado!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de Nascimento (dd-mm-aaa): ")
    endereco = input("Endereço: (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("==================== Usuário criado com sucesso! ====================")

def filtro_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n==================== Conta criada com sucesso! ====================")
        return {"agencia":agencia, "numero_cota":numero_conta, "usuario":usuario}
    
    print("\nUsuário não encontrado, criação de conta encerrado!")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor desejado para depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input("Informe o valor desejado para saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == '3':
            extrato(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == '5':
            lista_contas(contas)

        elif opcao == '6':
            novo_usuario(usuarios)

        elif opcao == '0':
            break
        
        else:
            print("Operação Inválida, por favor selecione novamente a operação desejada.")

main()