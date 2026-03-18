# Sistema de Cadastro de Usuários

usuarios = []

def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    usuarios.append({"nome": nome, "email": email})
    print(f"Usuário {nome} adicionado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de Usuários:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, Email: {usuario['email']}")

def buscar_usuario():
    nome_busca = input("Digite o nome do usuário que deseja buscar: ")
    encontrados = [u for u in usuarios if nome_busca.lower() in u['nome'].lower()]
    if encontrados:
        print("\nUsuários encontrados:")
        for usuario in encontrados:
            print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")
    else:
        print("Nenhum usuário encontrado com esse nome.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Buscar Usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()