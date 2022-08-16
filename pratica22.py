fruits=[('apple', 4), ('banana', 5), ('grape', 6), ('watermelon', 7)]

tabela={fruta:valor for fruta,valor in fruits}

print(tabela)

adicionar={'orange': 8, 'pear': 10}

print(tabela.get('apple'))

print(tabela.__reversed__())

tabela.popitem()

print(tabela)
