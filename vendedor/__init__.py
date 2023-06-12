def cadastrar_vendedor(vendedores):
    nome = input('Digite o nome do vendedor: ')
    login = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

    while login == senha:
        print('\33[1;31mO login não pode ser igual a senha\33[m')
        login = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')

    for vendedor in vendedores:
        if vendedor['login'] == login:
            print('\33[1;31mO login já está em uso, por favor escolha outro.\33[m')
            login = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')

    vendedor = {
        'nome': nome,
        'login': login,
        'senha': senha
    }
    vendedores.append(vendedor)
    print('\33[1;32mVendedor cadastrado com sucesso!\33[m')
    print(vendedores)


def login_vendedor(vendedores, login, senha, produtos):
    validacao_login = False
    for vendedor in vendedores:
        if vendedor['login'] == login and vendedor['senha'] == senha:
            print('\33[1;34mLogin realizado com sucesso\33[m')
            validacao_login = True
            break
    return validacao_login


def listar_produto(produtos, login):
    for produto in produtos:
        escreverNoArquivo(produto, login)
    lerarquivo(login)


def escreverNoArquivo(produto, login):
    nome = produto['nome']
    valor = produto['valor']
    qtde = produto['quantidade']

    texto = f'nome do produto: {nome}\n'
    texto = texto + f'valor do produto: {valor}\n'
    texto = texto + f'quantidade do produto: {qtde}\n\n'

    salvarArquivo(texto, login)


def salvarArquivo(texto, login):
    f = open(f'produtos_{login}.txt', 'a')
    f.write(texto)
    f.close()


def lerarquivo(login):
    f = open(f'produtos_{login}.txt', 'r')

    for linha in f.readlines():
        print(linha, end='')

    f.close()