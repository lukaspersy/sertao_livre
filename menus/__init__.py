def mostrar_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Valor: {produto['valor']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Descrição: {produto['descricao']}")
    print('\33[1;33m_________________________________\33[m')


def mostrar_menu_vendedor():
    print('\33[1;35m======== Sertão Livre - Área do vendedor ===========\33[m')
    print('1 - Cadastrar Vendedor')
    print('2 - Fazer Login')
    print('3 - Voltar')
    print('\33[1;35m_____________________________________________________\33[m')


def mostrar_menu_principal():
    print('\33[1;35m======== Sertão Livre - Sistema de Vendas ==========\33[m')
    print('1 - Menu do Vendedor')
    print('2 - Menu do Cliente')
    print('3 - Sair')
    print('\33[1;35m====================================================\33[m')


def mostrar_menu_produtos():
    print('\33[1;32m======  Gerenciamento de Produtos  ======\33[m')
    print('''
    1. Cadastrar novo produto
    2. Listar produto
    3. Mostrar gráfico
    4. Buscar produto 
    5. Editar produto
    6. Deletar produto
    7. Atualizar a senha de cadastro
    8. Voltar ao menu principal''')
    print('\33[1;32m=========================================\33[m')


def mostrar_menu_cliente():
    print('\33[1;35m======== Sertão Livre - Área do cliente ===========\33[m')
    print('1 - Cadastrar cliente')
    print('2 - Fazer Login')
    print('3 - Voltar')
    print('\33[1;35m===================================================\33[m')


def mostrar_menu_compra():
    print('\33[1;33m===========   Menu de Compras   ===========\33[m')
    print('''
    1. Buscar produto
    2. Comprar produto
    3. Listar compras
    4. Consultar descrição do produto
    5. Sair''')
    print('\33[1;33m===========================================\33[m')
