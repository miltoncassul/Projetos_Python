soma_pares = 0
soma_primos = 0
i = 0

print "Digite 10 numeros"

while i < 10:
	numero = input()
	if numero % 2 == 0:
		soma_pares = soma_pares + numero
	primo = 1
	j = 2
	
	while j< numero and primo == 1:
		if numero % j == 0:
			primo = 0
		j = j + 1
	if primo == 1:
		soma_primos = soma_primos + numero
	i = i + 1
	
print "Soma Pares : ", soma_pares
print "Soma Primos: ", soma_primos
