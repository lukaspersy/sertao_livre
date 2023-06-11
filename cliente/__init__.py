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
            break
    return validacao_login


def buscar_produto_cliente(produtos):
    busca = input('Digite o nome ou código do produto: ')
    achou = False
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            achou = True
            print('\33[1;33m______Resultado da busca______\33[m')
            mostrar_produto(produto)
    if not achou:
        print('\33[1;31mProduto não encontrado.\33[m')


def compras(produtos, carrinho, comprados):
    # Colocar a função mostrar produtos
    print(f'Tamanho da lista {len(produtos)}')
    for produto in produtos:
        # Esta parte vai ser subsituida pela função mostrar produtos
        print(f"\033[0;34m_____   PRODUTOS EM ESTOQUE   _____\033[m")
        mostrar_produto(produto)

    busca_produto = str(input('Digite o código do produto que deseja comprar: '))
    busca_quant = int(input('Digite a quantidade do produto que deseja comprar: '))

    for produto in produtos:

        if busca_produto == produto['codigo'] and busca_quant <= produto['quantidade']:

            carrinho.append(produto)
            quantidade = produto['quantidade']
            decrementado = quantidade - busca_quant
            # atualiza o dicionario
            produto['quantidade'] = decrementado
            # só exibe nos prints
            nome = produto['nome']
            descricao = produto['descricao']

        else:
            print('Código não encontrado!')

    while True:
        continuar = int(input('''Deseja continuar comprando?
         1. Sim
         2. Não
         >>> '''))
        if continuar == 1:
            compras(produtos, carrinho, comprados)
            break
        elif continuar == 2:
            comprar = int(input('''Deseja confirmar sua compra?
          1. Sim
          2. Não
          >>> '''))
            if comprar == 1:
                # aqui a lista comprados recebe uma cópia dos itens que estavam em carrinho
                comprados.append(carrinho.copy())
                # Aqui o carrinho é esvaziado ao confirmar a compra
                carrinho.clear()

                print(
                    f'Foram comprados {busca_quant} unidades do produto:{nome} - {descricao}, agora só restam {decrementado}')
                if len(carrinho) <= 0:
                    print(f'\033[1;33mSituação do carrinho: VAZIO\033[m')
                    print(f'\033[1;34mNo carrinho restaram os seguintes itens: {carrinho}\033[m')
                print(f'Parabéns! você comprou: \033[1;31m{busca_quant} \033[m unidades de {nome}.')

                print(f"Código: {produto['codigo']}\n",
                      f"\n\033[1;33mNome: {produto['nome']}",
                      f"\nValor: {produto['valor']}",
                      f"\nQuantidade: {produto['quantidade']}",
                      f"Descrição: {produto['descricao']}\033[m")

            elif comprar == 2:
                print('Finalizando as compras...')
                print(f'\033[0;36mVocê selecionou {busca_quant} unidades do produto:{nome}- {descricao}\033[m')
                print(f'\033[1;35mHá alguns itens no carrinho esperando por você: {carrinho}\033[m')
                finalizar = int(input('''Deseja concluir a compra dos itens selecionados?
            1. Sim
            2. Não
            >>> '''))
                if finalizar == 1:
                    return comprar()
                elif finalizar == 2:
                    carrinho.clear()
                    comprados.clear()
                    decrementado = quantidade
                    produto['quantidade'] = decrementado

                    print(
                        f'\033[0;36mVocê optou por não comprar: {busca_quant} unidades do produto:{nome} {descricao}\033[m')
                    if len(carrinho) <= 0:
                        print(f'\033[1;35mSituação do carrinho: VAZIO\033[m')
                    print('Em estoque restaram:')
                    print(f"Código: {produto['codigo']}\n",
                          f"\033[1;33mNome: {produto['nome']}\n",
                          f"Valor: {produto['valor']}\n",
                          f"Quantidade: {produto['quantidade']}\n",
                          f"Descrição: {produto['descricao']}\033[m")

        break


def consultarchatgpt(produto):
    openai.api_key = 'cole sua chave aqui'

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'me diga resumidamente o que você acha do ' + produto + ' ?'
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
