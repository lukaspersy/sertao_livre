from vendedor import *
from produto import *
from cliente import *
from menus import *

vendedores = [{'nome': 'Jose Luke', 'login': 'luke', 'senha': '0000'},{'nome': 'Lucas Pereira', 'login': 'lucas', 'senha': '0000'}, {'nome': 'Júnior', 'login': 'junior', 'senha': '1111'}, {'nome': 'Everton Cândido', 'login': 'everton', 'senha': '2222'}]
clientes = [{'nome': 'Jose Luke', 'login': 'luke', 'senha': '0000', 'comprados':[]}, {'nome': 'Júnior', 'login': 'junior', 'senha': '1111', 'comprados':[]}]
produtos = [{'codigo': '01', 'nome': 'cadeira', 'valor': 300.0, 'quantidade': 20, 'descricao': 'Cadeira Gamer Stillus Ergonômica com apoio para os pés (Preto)', 'vendedor': 'luke'}, {'codigo': '02', 'nome': 'Tênis', 'valor': 540.5, 'quantidade': 35, 'descricao': 'Tênis Nike Air Force 1 Flyease Casual', 'vendedor': 'luke'}]
carrinho = []
comprados = []

while True:
    mostrar_menu_principal()
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        mostrar_menu_vendedor()
        opcao_vendedor = int(input('Digite a opção desejada: '))
        if opcao_vendedor == 1:
            cadastrar_vendedor(vendedores)
        elif opcao_vendedor == 2:
            login = str(input('Digite o usuário: '))
            senha = str(input('Digite a senha: '))
            if login_vendedor(vendedores, login, senha, produtos):
                menu_produtos = True
                while menu_produtos:
                    mostrar_menu_produtos()
                    opcao_produto = int(input('Digte a opção desejada: '))
                    if opcao_produto == 1:
                        cadastrar_produto(produtos, login)
                    elif opcao_produto == 2:
                        listar_produto(produtos, login)
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
                print('\33[1;37mUsuário ou senha inválido. Tente novamente\33[m')

        elif opcao_vendedor == 3:
            break

    elif opcao == 2:
        mostrar_menu_cliente()
        opcao_cliente = int(input('Digite a opção desejada: '))
        if opcao_cliente == 1:
            cadastrar_cliente(clientes)
        elif opcao_cliente == 2:
            login = str(input('Digite o usuário: '))
            senha = str(input('Digite a senha: '))
            clienteLogado = login_cliente(clientes, login, senha)
            if clienteLogado is not None:
                menu_compra = True
                while menu_compra:
                    mostrar_menu_compra()
                    opcao_compra = int(input('Digite a opção desejada: '))
                    if opcao_compra == 1:
                        produtoCliente = buscar_produto_cliente(produtos)
                        mostrar_produto(produtoCliente)
                    elif opcao_compra == 2:
                        compras(produtos, carrinho, comprados, clienteLogado)
                    elif opcao_compra == 3:
                        listar_compras(clienteLogado)
                    elif opcao_compra == 4:
                        listar_produtos(produtos)
                        print(consultar_descricao(produtos))
                    elif opcao_compra == 5:
                        menu_compra = False
            else:
                print('\33[1;37mUsuário ou senha inválido. Tente novamente\33[m')


    elif opcao == 3:
        from art import tprint
        print('\033[1;36mPrograma encerrado!\033[m')
        tprint('Volte  Sempre')
        break