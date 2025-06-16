for numero in [1, 3, 5]:  
    if numero % 2 == 0:  
        print(f"{numero} é par! Loop interrompido.")  
        break  
else:  
    print("Nenhum número par encontrado.")  # Executa se o loop não for interrompido  