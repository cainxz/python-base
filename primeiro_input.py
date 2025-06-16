numero = int(input("Digite um número: "))
if numero %2 ==0: 
    print("É par e múltiplo de 4!" if numero % 4 == 0 else "é par!")
else:
    print("É ímpar!")
