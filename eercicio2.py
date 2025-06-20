# Entrada de número
numero = int(input('Insira um número: '))

# Função para verificar se é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

# Exibe se o número é par ou ímpar
print(f'O número {numero} é {par_ou_impar(numero)}.')

# Entrada de idade
idade = int(input('Digite sua idade: '))

# Função para classificar a idade
def classificar_idade(idade):
    if idade <= 12:
        return 'Criança'
    elif 13 >= idade < 19:
        return 'Adolescente'
    else:
        return 'Adulto'

# Exibe a classificação da idade
print(classificar_idade(idade))

# Validação de login
usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

if usuario == 'daniel' and senha == 'admin123':
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorretos.')

x = int(input('digite as cordenadas de x'))
y = int(input('digite as cordenadas de y'))

if x and y > 0:
    print('primeiro quadrante')
elif x < 0 and y >0:
    print('segundo quadrante')
elif x and y <0:
    print('terceiro quadrante')
elif x >0 and y <0:
    print('quarto quadrante')
else:
    print('o ponto está localizado no eixo ou origem.')

