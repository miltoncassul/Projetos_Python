soma = 0 
cont = 0
idade = 0
continua = True

print "Digite as idades"

while continua:
	idade = input()
	if idade != 0:
		soma = soma + idade
		cont = cont + 1
	else:
		continua = False
if cont == 0:
	print "Nenhum numero foi digitado!!"
else:
	print "Media das idade eh", soma/cont
