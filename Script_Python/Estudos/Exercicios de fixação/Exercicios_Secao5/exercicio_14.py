lab = float(input("Digite sua nota: "))
sem = float(input("Digite sua nota: "))
fin = float(input("Digite sua nota: "))

notas_atividades = (lab * 2) + (sem * 3) + (fin * 5)
peso_atividades = 2 + 3 + 5
media_ponderada = notas_atividades / peso_atividades

if media_ponderada >= 5:
    print("Aprovada")

elif media_ponderada >= 3:
    print("Recuperação")

else:
    print("Reprovada")
