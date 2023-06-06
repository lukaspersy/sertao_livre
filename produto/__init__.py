def cadastrar_produto(produtos):
    codigo = int(input('Digite o código do produto: '))
    nome = str(input('Digite o nome do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    valor = float(input('Digite o valor do produto: '))

    produto = {
        'codigo': codigo,
        'nome': nome,
        'valor': valor,
        'quantidade': quantidade
    }
    produtos.append(produto)


