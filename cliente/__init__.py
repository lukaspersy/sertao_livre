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


def compras(produtos, carrinho, comprados):
    # Colocar a função mostrar produtos
    for produto in produtos:
        # Esta parte vai ser subsituida pela função mostrar produtos
        print(f"\033[0;34m             === PRODUTOS EM ESTOQUE ===\033[m")
        print(f"Código: {produto['codigo']}\n",
              f"\033[1;33mNome: {produto['nome']}\n",
              f"Valor: {produto['valor']}\n",
              f"Quantidade: {produto['quantidade']}\n",
              f"Descrição: {produto['descricao']}\033[m")

        print("=" * 35)

    busca_produto = str(input('Digite o código do produto que deseja comprar: '))
    busca_quant = int(input('Digite a quantidade do produto que deseja comprar: '))

    for produto in produtos:

        if busca_produto == produto['codigo']:
            if busca_quant <= produto['quantidade']:
                carrinho.append(produto)
                quantidade = produto['quantidade']
                decrementado = quantidade - busca_quant
                # atualiza o dicionario
                produto['quantidade'] = decrementado
                # só exibe nos prints
                nome = produto['nome']
                descricao = produto['descricao']

            else:
                print('Você ultrapassou a quantidade para este produto')
                return
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
                comprados.append(carrinho[:])
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
                    return comprar
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
