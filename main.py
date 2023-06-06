from vendedor import *
from produto import *

vendedores = []
clientes = []
produtos = []

while True:
    print('======== Sertão Livre - Sistema de Vendas ===========')
    print('1 - Menu do Vendedor')
    print('2 - Menu do Cliente')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    while opcao == 1:
        print('======== Sertão Livre - Área do vendedor ===========')
        print('1 - Cadastrar Vendedor')
        print('2 - Fazer Login')
        print('3 - Voltar')
        opcao_vendedor = int(input('Digite a opção desejada: '))
        if opcao_vendedor == 1:
            cadastrar_vendedor(vendedores)
        if opcao_vendedor == 2:
            login = str(input('Digite o usuário: '))
            senha = str(input('Digite a senha: '))
            login_vendedor(vendedores, login, senha, produtos)

            if login_vendedor(vendedores, login, senha, produtos) == True:
                print('Login realizado com sucesso')
                menu_produtos = True
                while menu_produtos:
                    print('=' * 35)
                    opcao_produto = int(input('''   Gerenciamento de Produtos
                    1. Cadastrar novo produto
                    2. Pesquisar 
                    3. Editar
                    4. Deletar
                    5. Atualizar a senha de cadastro
                    6. Voltar ao menu principal                
                    Digite uma opção: '''))
                    print('=' * 35)
                    if opcao_produto == 1:
                        cadastrar_produto(produtos)
                    if opcao_produto == 6:
                        menu_produtos = False
            else:
                print('Login o/ou senha errados nessa porra')

        if opcao_vendedor == 3:
            break








