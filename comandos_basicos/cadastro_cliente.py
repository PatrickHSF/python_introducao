clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if clientes:
        for cliente in clientes:
            print("Nome:", cliente['nome'])
            print("Email:", cliente['email'])
            print("Telefone:", cliente['telefone'])
            print("---------------------------")
    else:
        print("Não há clientes cadastrados.")

def main():
    while True:
        print("------ CADASTRO DE CLIENTES ------")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()