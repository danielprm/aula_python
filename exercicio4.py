pessoa = {f'nome':'daniel','idade':'25','cidade':'Rio de Janeiro'}
pessoa['idade'] = 31
pessoa['profissao'] = 'engenheiro'
del pessoa['cidade']

numeros_quadrados = {x: x**2 for x in range(1,6)}
print(numeros_quadrados)

if 'nome' in pessoa:
    print("a chave 'nome' existe no dicionario. ")
else:
    print("A chave 'nome' não existe no dicionario. ") 

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)