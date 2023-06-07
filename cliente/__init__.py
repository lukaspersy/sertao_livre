def cadastrar_cliente(clientes):
    nome = input('Digite o nome do cliente: ')
    login = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    while login == senha:
        print('O login não pode ser igual a senha')
        login = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')

    for cliente in clientes:
        if cliente['login'] == login:
            print('O login já está em uso, por favor escolha outro.')
            login = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')

    cliente = {
        'nome': nome,
        'login': login,
        'senha': senha
    }
    clientes.append(cliente)
    print('Cliente cadastrado!')
    print(clientes)

def login_cliente(clientes, login, senha):
        validacao_login = False
        for cliente in clientes:
            if cliente['login'] == login and cliente['senha'] == senha:
                print('Login realizado com sucesso')
                validacao_login = True

        if not validacao_login:
            return False

