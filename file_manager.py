""" 
Script didático que tem por objetivo explicar o comportamento
de alguns recursos do Python, tais como:
1) Tuples
2) Laços de repetição
3) Tratamento de Exceções com Try..Except
4) Manutenção de arquivos com a função open() 

AUTOR: Achnaton Pessoa Rabelo
"""   

import os as comando

comando.system('cls')

MENU = '''
1: -> Criar Arquivo
2: -> Ler Arquivo
3: -> Editar arquivo
4: -> Deletar Arquivo
5: -> Limpar tela
6: -> Listar diretório
7: -> Mudar diretório
8: -> Localização atual
0: -> Encerrar programa
'''

OP = '-195376'

opcoes_menu = ('1', '2', '3', '4', '5', '6', '7', '8', '0')

while OP != '0':
    try:
        print(MENU)
        OP = input('Informe a opção desejada: ')
        if OP in opcoes_menu:
            #  op = int(op_s)
            if OP == '1':
                comando.system('cls')
                print('########### CRIANDO ARQUIVOS ###########')
                fname = input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                with open(file_name, 'x', encoding='utf-8') as f1:
                    print(f'Arquivo {file_name.upper()} criado com sucesso')
            elif OP == '2':
                comando.system('cls')
                print('########### LENDO ARQUIVOS ###########')
                fname = input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                with open(file_name, 'r', encoding='utf-8') as f1:
                    print(f1.read())
            elif OP == '3':
                comando.system('cls')
                print('########### EDITANDO ARQUIVOS ###########')
                fname = input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                texto = input('Digite abaixo:\n')
                with open(file_name, 'a', encoding='utf-8') as f1:
                    f1.write(texto + '\n')
            elif OP == '4':
                comando.system('cls')
                print('########### DELETANDO ARQUIVOS ###########')
                fname = input('Informe o arquivo a deletar: ')
                fname = f'{fname}.txt'

                if comando.path.exists(fname):
                    comando.remove(fname)
                    print('Arquivo deletado com sucesso!')
                else:
                    print('O nome de arquivo informado não existe!')
            elif OP == '5':
                comando.system('cls')
            elif OP == '6':
                comando.system('cls')
                dir_atual = comando.getcwd()
                print('PASTA ATUAL:', dir_atual)
                dir_atual = comando.listdir()
                for i in dir_atual:
                    print(i)
            elif OP == '7':
                comando.system('cls')
                print('########### ALTERANDO PASTA ATUAL ###########')
                destino = comando.chdir(input('Mudar para: '))
                print('PASTA ATUAL:', comando.getcwd())
            elif OP == '8':
                comando.system('cls')
                corrente = comando.getcwd()
                print('DIRETÓRIO CORRENTE:', corrente)
        else:
            print('Opção inválida, tente novamente!')
    except FileExistsError:
        print('Arquivo já existe!')
    except FileNotFoundError:
        print('Arquivo não encontrado')

comando.system('cls')
