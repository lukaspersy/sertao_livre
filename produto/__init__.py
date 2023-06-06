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
    buscar_produto(produtos, login)

