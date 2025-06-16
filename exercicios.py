lista = [10, 2.5, 'texto', [1, 2], 7, '3.14']

soma = 0
for item in lista:
    if isinstance(item, (int, float)):
        soma += item

print(soma)
