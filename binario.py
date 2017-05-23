numero_decimal = int(input("Digite o numero decimal: "))
num_decimal = numero_decimal
binario = []
hexadecimal = []

while (numero_decimal > 1):
	resto = (numero_decimal % 2)
	binario.insert(0, resto)
	numero_decimal = int(numero_decimal / 2)
'''
if (numero_decimal == 0):
	binario.insert(0, 0)

if (numero_decimal == 1):
	binario.insert(0, 1)
'''
# Incluir a parte inteira na lista binaria
binario.insert(0, numero_decimal)

print (binario)

#recuperando o valor original do usuario
numero_decimal = num_decimal

alfabeto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

#computar ovalor em decimal
while (numero_decimal > 15):
	resto = [(numero_decimal % 16)]
	hexadecimal.insert(0, resto)
	numero_decimal = int(numero_decimal/16)

	'''
	if (resto < 10):
		hexadecimal.insert(0, resto)
	elif (resto == 10):
		hexadecimal.insert(0, 'A')
	elif (resto == 11):
		hexadecimal.insert(0, 'B')
	elif (resto == 12):
		hexadecimal.insert(0, 'C')
	elif (resto == 13):
		hexadecimal.insert(0, 'D')
	elif (resto == 14):
		hexadecimal.insert(0, 'E')
	elif (resto == 15):
		hexadecimal.insert(0, 'F')
	'''

hexadecimal.insert(0, alfabeto[numero_decimal])

print (hexadecimal)