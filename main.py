from vendedor import *
from produto import *

vendedores = [{'nome': 'Lucas Pereira', 'login': 'lucas', 'senha': '0000'}, {'nome': 'Júnior', 'login': 'junior', 'senha': '1111'}, {'nome': 'Everton Cândido', 'login': 'everton', 'senha': '2222'}]
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

            while login_vendedor(vendedores, login, senha, produtos) == False:
                print(" Usuário ou senha inválido. Tente novamente")
                login = str(input('Digite o usuário: '))
                senha = str(input('Digite a senha: '))

            menu_produtos = True
            while menu_produtos:
                print('=' * 35)
                opcao_produto = int(input('''   Gerenciamento de Produtos
                1. Cadastrar novo produto
                2. Listar produto
                3. Mostrar gráfico
                4. Buscar produto 
                5. Editar produto
                6. Deletar produto
                7. Atualizar a senha de cadastro
                8. Voltar ao menu principal                
                Digite uma opção: '''))
                print('=' * 35)
                if opcao_produto == 1:
                    cadastrar_produto(produtos,login)
                if opcao_produto == 4:
                    buscar_produto(produtos, login)
                if opcao_produto == 8:
                    menu_produtos = False

        else:
            print('Login e/ou senha inválido.')

        if opcao_vendedor == 3:
            break








