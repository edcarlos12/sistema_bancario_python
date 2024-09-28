def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito não pode ser negativo!")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, valor, limite_saques_diarios, limite_saque):
    if valor <= 0:
        print("Valor de saque deve ser maior que zero!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite_saque:
        print(f"Você não pode sacar mais de R${limite_saque:.2f} por vez!")
    elif numero_saques >= limite_saques_diarios:
        print("Limite de saques diários atingido!")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R${saldo:.2f}")
    print("----------------")

# Função para exibir o menu e interagir com o usuário
def exibir_menu():
    saldo = 0.0
    extrato = []
    numero_saques = 0
    limite_saques_diarios = 3
    limite_saque = 500.0

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Extrato")
        print("4. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$"))
            saldo, extrato = depositar(saldo, extrato, valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$"))
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, valor, limite_saques_diarios, limite_saque)
        elif opcao == '3':
            exibir_extrato(saldo, extrato)
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
exibir_menu()
