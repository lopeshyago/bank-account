menu = """
\n========================================================================
============================= Bank Account =============================
========================================================================
Escolha uma das opções abaixo:
\n[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
\n========================================================================
========================================================================
========================================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n========================================================================")
            print(f"Depósito de R$ {valor:.2f} concluído com sucesso! Retornando ao Menu.")
            print("========================================================================")

        else:
            print("\n================================= Erro =================================")
            print("Falha na Operação! O valor informado é inválido.")
            print("Retornando ao Menu.")
            print("========================================================================")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n================================= Erro =================================")
            print("Falha na Operação! Saldo Insuficiente.")
            print("Retornando ao Menu.")
            print("========================================================================")

        elif excedeu_limite:
            print("\n================================= Erro =================================")
            print("Falha na Operação! O valor de saque excede o limite.")
            print("Retornando ao Menu.")
            print("========================================================================")

        elif excedeu_saques:
            print("\n================================= Erro =================================")
            print("Falha na Operação! Número máximo de saques excedido.")
            print("Retornando ao Menu.")
            print("========================================================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n========================================================================")
            print(f"Saque de R$ {valor:.2f} concluído com sucesso! Retornando ao Menu.")
            print("========================================================================")

        else:
            print("\n================================= Erro =================================")
            print("Falha na Operação! O valor informado é inválido.")
            print("Retornando ao Menu.")
            print("========================================================================")

    elif opcao == "e":
        print("\n=============================== EXTRATO ================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================================================")

    elif opcao == "q":
        break

    else:
        print("\n================================= Erro =================================")
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("Retornando ao Menu.")
        print("========================================================================")