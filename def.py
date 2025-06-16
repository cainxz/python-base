# def calcular_media(nota1, nota2, nota3):
#     soma = nota1 + nota2 + nota3
#     media = soma /3
#     return media

# # # Chamando a função
# # resultado = calcular_media(8, 7, 9)
# # print(f"A média é: {resultado}")  # Saída: A média é: 8.0


# # def calcula_imc(peso, altura):
# #     imc = peso / (altura ** 2)
# #     if imc < 18.5:
# #         return "Abaixo do peso"
# #     elif imc < 25:
# #         return "Peso normal"
# #     else:
# #         return "Sobrepeso"

# # classificacao = calcula_imc(70, 1.10)
# # print(classificacao)  # Saída: "Peso normal"



# pessoas = [("Ana", 25), ("João", 18), ("Maria", 30)]
# pessoas.sort(key=lambda pessoa: pessoa[1])  # Ordena pela idade
# print(pessoas)  # Saída: [('João', 18), ('Ana', 25), ('Maria', 30)]]





# def calculando_tudo(a, b,):
#      soma = f"soma da exatamente",  {a + b}
#      menos = f"a subtração exata é", {a - b}
#      multiplicacao= f"a multiplicação exata é", {a * b}
#      divisao = f"a divisão exata é", { a/b}
#      return soma,    menos, multiplicacao, divisao

# resultados= calculando_tudo (10, 5)

# print("calculando tudo da:\n", resultados) 



# chat gpt corrigiu o codigo axcima com o de baixo 
# def calculando_tudo(a, b):
#     soma = f"soma é {a + b}"
#     menos = f"subtração é {a - b}"
#     multiplicacao = f"multiplicação é {a * b}"
#     divisao = f"divisão é {a / b}"
#     return soma, menos, multiplicacao, divisao

# resultados = calculando_tudo(10, 5)
# print("calculando tudo dá:\n", resultados)


# def numeros_agora(a, b):
#     soma= a +b
#     return soma
    
# resultado = numeros_agora (10, 5)
# print(resultado)


# pessoas_ordenadas = sorted(pessoas_ordenadas, key=lambda pessoa: pessoa[1])



def bomdia (pessoa):
    def montarbomdia():
        return f"bom dia, {pessoa}!"
    return montarbomdia()

print(bomdia ("kaio"))