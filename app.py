import os

restaurantes = ['piza', 'sushi']

def exibir_nome_do_programa():  
    print('sabor express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu \n')
    main()

def opcao_invalida():
    print('opção invalida! \n')
    voltar_ao_menu_principal()
    

def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes ')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar ')
    restaurantes.append(nome_do_restaurante)
    print(f'o Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('listando os restaurantes ')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opção_escolhida = int(input('escolha uma opção: '))
        #print(f'voce escolheu a opção{opção_escolhida}')
        #opção_escolhida = int(opção_escolhida)

        if opção_escolhida == 1:
             cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            print('ativar restaurante')
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()