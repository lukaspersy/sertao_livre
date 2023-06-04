from vendedor import *
vendedores = []
clientes = []

while True:
    print('======== Sertão Livre - Sistema de Vendas ===========')
    print('1 - Menu do Vendedor')
    print('2 - Menu do Cliente')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    while opcao == 1:
        print('======== Sertão Livre - Área do vendedor ===========')
        print('1 - Cadastrar Vendedor')
        print('2 - Fazer Login')
        print('3 - Voltar')
        opcao_vendedor = int(input('Digite a opção desejada: '))
        if opcao_vendedor == 1:
            cadastrar_vendedor(vendedores)
        if opcao_vendedor == 2:
            login_vendedor(vendedores)






