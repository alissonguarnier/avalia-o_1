def menu():
    while True:

        print('''
        ==== Caixa Eletrônico ===

        Escolha o número no menu:
        [1] - Depositar
        [2] - Saldo
        [3] - Sacar
        [4] - Sair

        ''')

        opcao = int(input("Digite o número da opção desejada: "))
        return opcao

def consultar_saldo(sld):
    print(f"Seu saldo é de: R${sld:.2f}")

def fazer_saque(sld, saque):
    saldo = sld - saque
    return saldo

def fazer_deposito(sld, deposito):
    saldo = sld + deposito
    return saldo

def main():
    print("=== Bem-vindo ao Banco ===")
    saldo = 200.00

    while True:

        op = menu()

        match op:
            case 4:
                print("Sistema finalizado...")
                break
            
            case 1:
                print("Opção de depósito selecionada.")
                valorDeposito = float(input("Digite o valor do depósito: R$"))
                if valorDeposito > 0:
                    saldo = fazer_deposito(saldo, valorDeposito)
                else:
                    print("Valor deve ser positivo.")

            case 2:
                consultar_saldo(saldo)
    
            case 3:
                print("Opção de saque selecionada.")
                valorSaque = float(input("Digite o valor do saque: R$"))
                if valorSaque <= saldo:
                    saldo = fazer_saque(saldo, valorSaque)
                else:
                    print("Saldo insuficiente")
    
            case _: 
                print("Opção inválida")

if __name__ == "__main__":
    main()
