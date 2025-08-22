# import calculadora
# calculadora.subtrair
# resultado=calculadora.subtrair(100,45)
# print("o resultado da subtração é :", resultado)
       #------------------------------------------------

# from textos import gritar

# frases= gritar("eu amo programar")

# print(frases)

#       -------------------------------------------------
# import universo

# nome= universo.NOME_PLANETA
# lua= universo.NUMERO_DE_LUAS

# print("Nóes viemos da", nome,"e lá tem", lua, "lua(s)")

              # -------------------------------------
# import ferramentas_de_geometria_analitica as geo

# y= geo.calcular_distancia(0,0,1,1)

# print(y)



# -----------------------------------



import validador



emails= [

    "joao@example.com",
    "maria123@site.com.br",
    "semarroba.com",
    "carla@.com",
    "lucas@dominio",
    "ana_silva@gmail.com",
    "@gmail.com",
    "pedro@hotmail",
    "teste@site.com",
    "invalido",
    "paulo@empresa.net",
    "roberta@web."
]


for email in emails:
     if validador.email_e_valido(email):
        print("o email", email, "é valido")

     else:
         print("o email", email,"é invalido")