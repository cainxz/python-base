#!usr/bin/env python

__version__= "0.1.0"
__author__= "Kaio"


numeros = list(range(1, 11))


for n1 in numeros:
    print("{:^18}".format(f"tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format (f"{n1} x {n2} = {resultado}"))

    print("-" * 18)
