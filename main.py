saldo = 1000
print("Saldo inicial: {saldo}")
while True:
    print("\nEscolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("4. Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        valor = float(input("Valor a depositar: "))
        saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {saldo}")
    elif opcao == "2":
        valor = float(input("Valor a sacar: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {saldo}")
    elif opcao == "3":
        print(f"Saldo atual: {saldo}")

    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        