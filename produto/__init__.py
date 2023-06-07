import matplotlib.pyplot as plt
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

def mostrar_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Valor: {produto['valor']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Descrição: {produto['descricao']}")
    print('\33[1;33m_________________________________\33[m')

def buscar_produto(produtos, login):
    busca = input('Digite o nome ou código do produto: ')
    achou = False
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            achou = True
            if produto['vendedor'] == login:
                print('\33[1;33m______Resultado da busca______\33[m')
                mostrar_produto(produto)
    if not achou:
        print('\33[1;31mProduto não encontrado.\33[m')


def editar_produto(produtos, login):
    busca = input('Digite o nome ou o codigo que deseja editar: ')
    for produto in produtos:
        if busca in produto['nome'] or busca in produto['codigo']:
            if produto['vendedor'] == login:
                print('\33[1;33m______Produto que será editado______\33[m')
                mostrar_produto(produto)
                produto['codigo'] = input('Digite o novo código: ')
                produto['nome'] = input('Digite o novo nome: ')
                produto['valor'] = input('Digite o novo valor: ')
                produto['quantidade'] = input('Digite a nova quantidade: ')
                produto['descricao'] = input('Digite a nova descrição: ')
                print('\33[1;33mProduto editado com sucesso.\33[m')
                print(produto)
        else:
            print('\33[1;31mProduto não pode ser editado.\33[m')


def atualizar_senha(vendedores, login):
    for vendedor in vendedores:
        if vendedor['login'] == login:
            vendedor['senha'] = input('Digite uma nova senha: ')
            print('\33[1;34mSenha atualizada com sucesso.\33[m')
            break

# def mostrar_grafico(produto):
#     # creating the dataset
#     data = {'Mesa': 20, 'Cadeira': 15, 'Corda': 30,
#             'COrtina': 35}
#     courses = list(data.keys())
#     values = list(data.values())
#
#     fig = plt.figure(figsize=(10, 5))
#
#     # creating the bar plot
#     plt.bar(courses, values, color='maroon',
#             width=0.4)
#
#     plt.xlabel("Produtos")
#     plt.ylabel("Quantidade")
#     plt.title("Sertao Livre")
#     plt.show()

def deletar_produto(produtos, login):
    for produto in produtos:
        if produto['vendedor'] == login:
            print(f'{produtos.index(produto)} =' + f" Código: {produto['codigo']} " + f"| Nome: {produto['nome']} " +
                  f'| Valor: {produto["valor"]:.2f} ' + f"| Quantidade: {produto['quantidade']} " + f"| Descrição: {produto['descricao']}")
    busca = int(input('Informe o índice do produto que deseja remover: '))
    produtos.pop(busca)
    print('\33[1;37mProduto excluído com sucesso.\33[m')
