id = int(input('ID: '))
nomeProduto = (input('Nome: '))
qtd = int(input('Estoque: '))
valor = float(input('Valor: '))

print('ID: {}, Nome: {}, Estoque: {}, Valor: {}'.format(id, nomeProduto, qtd, valor))

qtd += 1

print('Aumentando o item no estoque: {}'.format(qtd))

qtd -= 1

print('Removendo item no estoque: {}'.format(qtd))

