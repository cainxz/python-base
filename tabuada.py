#!usr/bin/env python
#"""imprime a tabuada do 1 ao 10."""


__version__ = "0.1.00"
__author__ = "Kaio"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

#print  (numeros)



#iterable (percorriveis)

#para cada numeroo em numeros: 

for numero in numeros:
        print("tabuada do:", numeros)
        for outro_numero in numeros: 
            print(numero * outro_numero)
        print ("-------------")
        
