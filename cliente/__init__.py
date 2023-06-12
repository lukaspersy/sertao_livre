from sertao_livre.menus import *
from sertao_livre import produto
import openai
from sertao_livre.produto import *


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
        'senha': senha,
        'comprados':[]
    }
    clientes.append(cliente)
    print('Cliente cadastrado!')


def login_cliente(clientes, login, senha):
    cliente_logado = None
    for cliente in clientes:
        if cliente['login'] == login and cliente['senha'] == senha:
            cliente_logado = cliente
            print('Login realizado com sucesso')
            break
    return cliente_logado


def buscar_produto_cliente(produtos):
    busca = input('Digite o nome ou código do produto: ')
    achou = None
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            achou = produto
            print('\33[1;33m__Resultado da busca__\33[m')

    if achou is None:
        print('\33[1;31mProduto não encontrado.\33[m')
    return achou


def compras(produtos, carrinho, comprados, usuarioLogado):
    menuContinuarComprando = True
    menuCompras = True
    global nome, descricao, quantidade, valor
    listar_produtos(produtos)

    while menuCompras:

        busca_produto = str(input('Digite o código do produto que deseja comprar: '))
        busca_quant = int(input('Digite a quantidade do produto que deseja comprar: '))
        encontrado = False
        for produto in produtos:

            if busca_produto == produto['codigo'] and busca_quant <= produto['quantidade']:
                produtoSelecionado = produto.copy()
                produtoSelecionado['quantidade'] = busca_quant
                carrinho.append(produtoSelecionado)
                quantidade = produto['quantidade']
                decrementado = quantidade - busca_quant
                produto['quantidade'] = decrementado
                nome = produto['nome']
                descricao = produto['descricao']
                valor = produto['valor']
                encontrado = True
                break

        if not encontrado:
            print("\033[0;31mProduto não encontrado ou quantidade insuficiente.\033[m")
            break

        while menuContinuarComprando:
            print('Deseja continuar comprando?')
            print("1. Continuar comprando")
            print("2. Não")
            opcao = input("Digite o número da opção desejada: ")
            if opcao == '1':
                print("\033[1;36mContinuando compra...\033[m ")
                break
            elif opcao == '2':
                menuContinuarComprando = False
                print('\033[1;36mEncerrando...\033[m')
                print("Deseja fechar suas compras?")
                print("\033[1;33m1. Sim")
                print("2. Não\033[m")
                comprar = input("Digite o número da opção desejada para Fechar sua compra: ")
                if comprar == '1':
                    menuCompras = False
                    comprados = carrinho.copy()
                    usuarioLogado['comprados'].append(comprados)
                    carrinho.clear()
                    for produto in comprados:
                        print(f"Foram comprados {produto['quantidade']} unidades do produto:")
                        print("\033[0;33mCódigo:", produto['codigo'])
                        print("Nome:", produto['nome'])
                        print("Valor:", produto['valor'])
                        print("Quantidade:", produto['quantidade'])
                        print("Descrição:", produto['descricao'])
                        print(f"Totalizando R$:{produto['valor'] * produto['quantidade']}\033[m")
                        print("--------------------")
                elif comprar == '2':
                    print(f'\033[1;35mHá alguns itens no carrinho esperando por você:\033[m')
                    for item in carrinho:
                        print("\033[0;33mCódigo:", item['codigo'])
                        print("Nome:", item['nome'])
                        print(f"Quantidade: {item['quantidade']}")
                        print("Descrição:", item['descricao'])
                        total = item['quantidade'] * item['valor']
                        print(f"Valor:", item['valor'])
                        print(f'Totalizando R$:{total}\033[m')
                        print("--------------------")
                    print(f'Tem certeza que deseja \033[1;31mNÃO CONTINUAR\033[m com a compra destes itens?')
                    print("\033[1;33m1. Sim, tenho certeza!")
                    print("2. Não, Acho que vou comprar!\033[m")
                    confirmacao = input("Digite o número da opção desejada: ")
                    if confirmacao == '1':
                        for item in carrinho:
                            for produtoEstoque in produtos:
                                if (item['codigo'] == produtoEstoque['codigo']):
                                    print(
                                        f"\033[0;36mVocê optou por não comprar: {item['quantidade']} unidades do produto: {item['descricao']}\033[m")
                                    produtoEstoque['quantidade'] = produtoEstoque['quantidade'] + item['quantidade']
                        carrinho.clear()
                        if len(carrinho) <= 0:
                            print(f'\033[1;35mSituação do carrinho: VAZIO\033[m')
                    elif confirmacao == '2':
                        return opcao == 2
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        break


def listar_produtos(produtos):
    for produto in produtos:
        mostrar_produto(produto)


def consultar_descricao(produtos):
    produtoCliente = buscar_produto_cliente(produtos)
    openai.api_key = 'minha chave'

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'me diga resumidamente o que você acha do ' + produtoCliente['descricao'] + ' ?'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text


def listar_compras(clienteLogado):
    print(f'\033[1;35mMinhas Compras:\033[m')
    if len(clienteLogado['comprados']) > 0:
        for compra in clienteLogado['comprados']:
            listar_produtos(compra)
    else:
        print(f'\033[1;35mNenhum registro encontrado.\033[m')