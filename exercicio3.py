
numeros = ['1','2','3','4','5','6','7','8','9','10']
nomes = ['alexandre','Ribeiro','quintanilha','dulce']
ano = ['1999','2025']

for numero in numeros :
    print(numero)

soma = 0
for num in range(1, 11):  
    if num % 2 != 0:      
        soma += num       

print("Soma dos números ímpares de 1 a 10:", soma)

for num in range(10, 0, -1):
    print(num)

numero_qualquer = int(input('digite qualquer numero '))
for i in range(1,11):
    resultado = numero_qualquer * i
    print(f'{numero_qualquer}x {i} = {resultado}')

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")