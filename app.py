import os

def exibir_nome_do_programa():  
    print('sabor express\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')

def finalizar_app():
    os.system('cls')
    print('finalizando o app\n')

def escolher_opcao():
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
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()