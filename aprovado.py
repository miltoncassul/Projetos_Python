nota = [float(input())]
	
media = (nota[i])/3

print ("Informe a primeira nota:\nInforme a segunda nota:\nInforme a terceira nota:")

if media >= 7.0:
	print ("Aprovado com media", media)
if media >= 5.0 and media < 7.0:
	print ("Recuperacao com media", media)
if media < 5.0:
	print ("Reprovado com media", media)

