# contageme = "fundação"

# def contagem ():
   
#    return contagem

# # print (len(contageme))



# def contagem_letras(texto):
#     dicionario = {}
#     for letra in texto:
#         if letra in dicionario:
#             dicionario[letra] += 1
#         else:
#             dicionario[letra] = 1
#     return dicionario

# contageme = "fundação"
# resultado = contagem_letras(contageme)
# print(resultado)


def contagem_letras (texto):
    dicionario = {}
    for letra in texto:
        if letra in dicionario:
            dicionario[letra] +=1
        else:
            dicionario[letra] = 1
    return dicionario
contageme = "fundação"
resultado = contagem_letras(contageme)
print(resultado)
