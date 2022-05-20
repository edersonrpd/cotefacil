import os


arquivos = os.listdir()
cotacoes = []
if ('sample_data' and '.config') in arquivos:
  arquivos.remove('sample_data')
  arquivos.remove('.config')


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

  with open(file, mode='r', encoding='utf-8') as fp:
    linha = fp.readline()
    while linha:

      if linha.startswith('1'):
        dados = linha.split(';')
        #print(dados)
        cnpj_cliente = dados[1]
        uf = dados[2]
        data_encerramento = dados[3]
        cod_cotacao = dados[4]
        data_inicial_val_preco = dados[6]
        cod_cond_pgto = dados[8]
        cnpj_fornecedor = dados[9]
      if linha.startswith('2'):
        prod = linha.split(';')
        produto = prod[1]
        produtos.append(produto)
        qtde_produto.append(prod[2])
      linha = fp.readline()

      
  
  print(f'Pedido: {cod_cotacao}')
  print(f'CNPJ: {cnpj_cliente}')
  print(f'Condição: {cod_cond_pgto}')
  print(f'CNPJ Fornecedor: {cnpj_fornecedor}')
  print('-' * 32 )
  for produto, qtde in zip(produtos, qtde_produto):
    print(f'EAN: {produto} Qtd: {qtde}')
  return cnpj_cliente

def imprimir():
  for arquivo in arquivos:
    print('-' * 32 )
    print(arquivo)
    print(cotefacil(arquivo))