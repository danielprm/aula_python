print('sabor express\n')


print('1. cadastrar restaurante')
print('2. listar restaurante')
print('3. ativar restaurante')
print('4. sair\n')

opção_escolhida = int(input('escolha uma opção: '))
#print(f'voce escolheu a opção{opção_escolhida}')
#opção_escolhida = int(opção_escolhida)

if opção_escolhida == 1:
    print('cadastrar restaurante')
elif opção_escolhida == 2:
    print('listar restaurantes')
elif opção_escolhida == 3:
    print('ativar restaurante')
else:
    print('encerrando o programa.')