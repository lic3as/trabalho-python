nome = input("NOME DO ALUNO:\n")
np = input("INFORME A NOTA DA PROVA\n")
nt = input("INFORME A NOTA DO TRABALHO\n")
nq =input("INFORME A NOTA DA QUALITATIVA\n")

media = (float(np)*6+float(nt)*3+float(nq))/10

if media >= 6:
    print ("APROVADO")
else:
    print ("REPROVADO")

print("A MEDIA DO ALUNO", nome, "E", media)