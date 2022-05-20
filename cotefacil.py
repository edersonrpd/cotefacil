import os

arquivos = os.listdir()

excecao = ['cotefacil.py', '.git', '.gitignore', 'resultados.txt']

try:
    for exc in excecao:

        if exc in excecao:
            arquivos.remove(exc)
        else:
            None

except exc as error:
    print(error)


def cotefacil(file: str):
    cnpj_cliente = ''
    uf = ''
    data_encerramento = ''
    cod_cotacao = ''
    cod_cliente = ''
    data_inicial_val_preco = ''
    data_final_val_preco = ''
    cod_cond_pgto = ''
    cnpj_fornecedor = ''
    produtos = list()
    qtde_produto = list()
    tot_produto = ''

    with open(file, mode='r', encoding='utf-8') as fp:
        linha = fp.readline()
        while linha:

            if linha.startswith('1'):
                dados = linha.split(';')
                # print(dados)
                cnpj_cliente = dados[1]
                uf = dados[2]
                data_encerramento = dados[3]
                pedido = dados[4]
                data_inicial_val_preco = dados[6]
                cod_cond_pgto = dados[8]
                cnpj_fornecedor = dados[9]
            if linha.startswith('2'):
                prod = linha.split(';')
                produto = prod[1]
                produtos.append(produto)
                qtde_produto.append(prod[2])
            if linha.startswith('9'):
                dados = linha.split(';')
                tot_produto = dados[1]

            linha = fp.readline()

    print('-' * 48)
    print(f'|Pedido: {pedido} | Arquivo: {file}|')
    print('-' * 48)
    print(f'CNPJ Cli: {cnpj_cliente} ')
    print(f'CNPJ For: {cnpj_fornecedor}')
    print(f'Condição: {cod_cond_pgto}')
    print(f'Total Produtos: {tot_produto}')
    print('-' * 48 )
    
    for produto, qtde in zip(produtos, qtde_produto):
        print(f'EAN: {produto} Qtd: {qtde}')
    print('')
    return cnpj_cliente


for arquivo in arquivos:
    cotefacil(arquivo)

print(f'{len(arquivos)} arquivos')
