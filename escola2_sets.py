#!/usr/bin/env python3
"""
Exibe relatorio de criancas por atividade.

Imprimir a lista de criancas agrupada por sala que frequentada cada uma das atividades
"""

__version__ = "0.1.1"
__author__ = "Kaio"

# Dados
sala1 = ["Tony", "Kaio", "Madara", "Kaguya", "Maik", "Sanzu", "Killua"]
sala2 = ["Vitim", "Alucard", "Sasuke", "Flacko", "Kazy", "Kazutora", "Marreco"]

aula_ingles = ["Kaio", "Killua", "Sanzu", "Flacko", "Vitim", "Marreco"]
aula_russo = ["Madara", "Alucard", "Tony", "Maik", "Flacko"]
aula_roblox = ["Madara", "Kaguya", "Sasuke", "Kazutora", "Kazy"]

print("{:^18}".format(f"Alunos das sala"))
print("-" *40)
print()
print("sala1", sala1)
print("sala2", sala2)


atividades = [
    ("ingles", aula_ingles),
    ("russo", aula_russo),
    ("roblox", aula_roblox),
]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    print()
    
    print(f"Alunos da atividade {nome_atividade}\n")
    #print("" * 40)

    #sala1 que tem interseção com a atividade


    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))
    
    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    
    print()
    print("-" * 40)
    