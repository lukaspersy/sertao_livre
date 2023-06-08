
def cadastrar_vendedor(vendedores):
    nome = input('Digite o nome do vendedor: ')
    login = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    while login == senha:
        print('O login não pode ser igual a senha')
        login = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')

    for vendedor in vendedores:
        if vendedor['login'] == login:
            print('O login já está em uso, por favor escolha outro.')
            login = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')

    vendedor = {
        'nome': nome,
        'login': login,
        'senha': senha
    }
    vendedores.append(vendedor)
    print('Vendedor cadastrado!')
    print(vendedores)


def login_vendedor(vendedores, login, senha, produtos):
    validacao_login = False
    for vendedor in vendedores:
        if vendedor['login'] == login and vendedor['senha'] == senha:
            print('Login realizado com sucesso')
            validacao_login = True
            break
    return validacao_login










