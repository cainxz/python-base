#!/usr/bin/env python3
"""
Exibe relatorio de criancas por atividade.

Imprimir a lista de criancas agrupada por sala que frequentada cada uma das atividades
"""

__version__ = "0.1.0"
__author__ = "Kaio"

# Dados
sala1 = ["Tony", "Kaio", "Madara", "Kaguya", "Maik", "Sanzu", "Killua"]
sala2 = ["Vitim", "Alucard", "Sasuke", "Flacko", "Kazy", "Kazutora", "Marreco"]

aula_ingles = ["Kaio", "Killua", "Sanzu", "Flacko", "Vitim", "Marreco"]
aula_russo = ["Madara", "Alucard", "Tony", "Maik", "Flacko"]
aula_roblox = ["Madara", "Kaguya", "Sasuke", "Kazutora", "Kazy"]

atividades = [
    ("ingles", aula_ingles),
    ("russo", aula_russo),
    ("roblox", aula_roblox),
]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print("#" * 40)
