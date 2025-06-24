import os

restaurantes = [{'nome': 'praça', 'categoria': 'Japonesa', 'ativo':False}, {'nome':'Pizza', 'categoria':'Pizza', 'ativo':True},
{'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():  
    print('sabor express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. alternar estado do restaurante')
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
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('cadastro de novos restaurantes ')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar ')
    categoria = input(f'digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    restaurantes.append(nome_do_restaurante)
    print(f'o Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('listando os restaurantes ')
    print(f'{'Nome do restaurante'.ljust(22)} | {f'Categoria'.ljust(20)} | status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if  restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('alternando o estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante foi {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontado:
        print('o restaurante não foi encontrado ')

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
            alternar_estado_do_restaurante()
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