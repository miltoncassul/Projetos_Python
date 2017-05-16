"""
algoritmo
soma_peares <- 0 soma_primos <- 0
para i <- 1 ate 10
	leia numero
	se (numero%2)=0 entao
		soma_pares <- soma_pares + numero
	primo <- 1
	para j <- 2 ate numero -1 faca passo 1
		se (numero%j)=0 entao
			primo <- 0
	se primo = 1 entao
		soma_primos <- soma_primos + numeros
	soma_pares, soma_primos

"""
soma_pares = 0
soma_primos = 0

for i <= 10:
	n=input("Digite a sequencia: ")
	if n%2==0:
		soma_pares = soma_pares + n
	primo = 1
	for j = numero - 1
