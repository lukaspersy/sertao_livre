def cadastrar_produto(produtos, login):
    codigo = str(input('Digite o código do produto: '))
    nome = str(input('Digite o nome do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    valor = float(input('Digite o valor do produto: '))
    descricao = str(input('Digite a descrição do produto: '))

    produto = {
        'codigo': codigo,
        'nome': nome,
        'valor': valor,
        'quantidade': quantidade,
        'descricao': descricao,
        'vendedor': login
    }
    produtos.append(produto)
    print('Produto cadastrado.')
    print(produtos)


def buscar_produto(produtos, login):
    busca = input('Digite o nome ou código do produto: ')
    achou = False
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            achou = True
            if produto['vendedor'] == login:
                print(f"Código: {produto['codigo']}")
                print(f"Nome: {produto['nome']}")
                print(f"Valor: {produto['valor']}")
                print(f"Quantidade: {produto['quantidade']}")
                print(f"Descrição: {produto['descricao']}")
    if not achou:
        print('\33[1;31mProduto não encontrado.\33[m')


def editar_produto(produtos, login):
    busca = input('Digite o nome ou o codigo que deseja editar: ')
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            if produto['vendedor'] == login:
                produto['codigo'] = input('Digite o novo código: ')
                produto['nome'] = input('Digite o novo nome: ')
                produto['valor'] = input('Digite o novo valor: ')
                produto['quantidade'] = input('Digite a nova quantidade: ')
                produto['descrição'] = input('Digite a nova descrição: ')
                print('\33[1;33mProduto editado com sucesso.\33[m')
            else:
                print('\33[1;31mProduto não pode ser editado.\33[m')


def atualizar_senha(vendedores, login):
    for vendedor in vendedores:
        if vendedor['login'] == login:
            vendedor['senha'] = input('Digite uma nova senha: ')
            print('\33[1;34mSenha atualizada com sucesso.\33[m')
            break
