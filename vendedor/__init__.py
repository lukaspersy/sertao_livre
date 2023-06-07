import matplotlib.pyplot as plt
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

    if not validacao_login:
        return False

def mostrar_grafico(produto):
    # creating the dataset
    courses = list(produto.keys())
    values = list(produto.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(courses, values, color='red',
            width=0.4)

    plt.xlabel(['nome'])
    plt.ylabel(['quantidade'])
    plt.title("Sertao Livre")
    plt.show()









