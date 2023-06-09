from vendedor import *
from produto import *
from cliente import *

vendedores = [{'nome': 'Jose Luke', 'login': 'luke', 'senha': '0000'},{'nome': 'Lucas Pereira', 'login': 'lucas', 'senha': '0000'}, {'nome': 'Júnior', 'login': 'junior', 'senha': '1111'}, {'nome': 'Everton Cândido', 'login': 'everton', 'senha': '2222'}]
clientes = [{'nome': 'Jose Luke', 'login': 'luke', 'senha': '0000'}, {'nome': 'Júnior', 'login': 'junior', 'senha': '1111'}]
produtos = [{'codigo': '01', 'nome': 'cadeira', 'valor': 300.0, 'quantidade': 20, 'descricao': 'Cadeira Gamer Stillus Ergonômica com apoio para os pés (Preto)', 'vendedor': 'luke'}, {'codigo': '02', 'nome': 'Tênis', 'valor': 540.5, 'quantidade': 35, 'descricao': 'Tênis Nike Air Force 1 Flyease Casual', 'vendedor': 'luke'}]
carrinho=[]
comprados=[]

while True:
    print('======== Sertão Livre - Sistema de Vendas ===========')
    print('1 - Menu do Vendedor')
    print('2 - Menu do Cliente')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('======== Sertão Livre - Área do vendedor ===========')
        print('1 - Cadastrar Vendedor')
        print('2 - Fazer Login')
        print('3 - Voltar')
        opcao_vendedor = int(input('Digite a opção desejada: '))
        if opcao_vendedor == 1:
            cadastrar_vendedor(vendedores)
        elif opcao_vendedor == 2:
            login = str(input('Digite o usuário: '))
            senha = str(input('Digite a senha: '))
            if login_vendedor(vendedores, login, senha, produtos):
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
                        cadastrar_produto(produtos, login)
                    elif opcao_produto == 3:
                        mostrar_grafico(produtos, login)
                    elif opcao_produto == 4:
                        buscar_produto(produtos, login)
                    elif opcao_produto == 5:
                        editar_produto(produtos, login)
                    elif opcao_produto == 6:
                        deletar_produto(produtos, login)
                    elif opcao_produto == 7:
                        atualizar_senha(vendedores, login)
                    elif opcao_produto == 8:
                        menu_produtos = False
            else:
                print('Usuário ou senha inválido. Tente novamente')

        elif opcao_vendedor == 3:
            break

    elif opcao == 2:
        print('======== Sertão Livre - Área do cliente ===========')
        print('1 - Cadastrar cliente')
        print('2 - Fazer Login')
        print('3 - Voltar')
        opcao_cliente = int(input('Digite a opção desejada: '))

        if opcao_cliente == 1:
            cadastrar_cliente(clientes)

        elif opcao_cliente == 2:
            login = str(input('Digite o usuário: '))
            senha = str(input('Digite a senha: '))

            if login_cliente(clientes, login, senha):
                menu_compra = True
                while menu_compra:
                    print('=' * 35)
                    opcao_compra = int(input('''   Menu de Compras
                                1. Buscar produto
                                2. Comprar produto
                                3. Listar compras
                                4. Consultar descrição do produto
                                5. Sair              
                                Digite uma opção: '''))
                    print('=' * 35)
                    if opcao_compra == 2:
                        compras(produtos, carrinho, comprados)
                    if opcao_compra == 5:
                        menu_compra = False

            else:
                print('Usuário ou senha inválido. Tente novamente')

    elif opcao == 3:
        from art import tprint
        tprint('Volte    Sempre')
        break







