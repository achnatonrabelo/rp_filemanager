""" 
Script didático que tem por objetivo explicar o comportamento
de alguns recursos do Python, tais como:
1) Tuples
2) Laços de repetição
3) Tratamento de Exceções com Try..Except
4) Manutenção de arquivos com a função open() 

AUTOR: Achnaton Pessoa Rabelo
"""   

import os as cm

from rich.console import Console

console = Console()

cm.system('cls')

MENU = '''
[bold green][1][/bold green]: -> Criar Arquivo
[bold green][2][/bold green]: -> Ler Arquivo
[bold green][3][/bold green]: -> Editar arquivo
[bold green][4][/bold green]: -> Deletar Arquivo
[bold green][5][/bold green]: -> Limpar tela
[bold green][6][/bold green]: -> Listar diretório
[bold green][7][/bold green]: -> Mudar diretório
[bold green][8][/bold green]: -> Localização atual
[bold green][0][/bold green]: -> Encerrar programa
'''

OP = ''

opcoes_menu = ('1', '2', '3', '4', '5', '6', '7', '8', '0')

while OP != '0':
    try:
        console.print(MENU)
        OP = console.input('Informe a opção desejada: ')
        if OP in opcoes_menu:
            #  op = int(op_s)
            if OP == '1':
                cm.system('cls')
                console.print('########### CRIANDO ARQUIVOS ###########')
                fname = console.input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                with open(file_name, 'x', encoding='utf-8') as f1:
                    console.print(f'Arquivo {file_name.upper()} criado com sucesso')
            elif OP == '2':
                cm.system('cls')
                console.print('########### LENDO ARQUIVOS ###########')
                fname = console.input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                with open(file_name, 'r', encoding='utf-8') as f1:
                    console.print(f1.read())
            elif OP == '3':
                cm.system('cls')
                console.print('########### EDITANDO ARQUIVOS ###########')
                fname = console.input('Informe o nome do arquivo: ')
                file_name = f"{fname}.txt"

                texto = console.input('Digite abaixo:\n')
                with open(file_name, 'a', encoding='utf-8') as f1:
                    f1.write(texto + '\n')
            elif OP == '4':
                cm.system('cls')
                console.print('########### DELETANDO ARQUIVOS ###########')
                fname = console.input('Informe o arquivo a deletar: ')
                fname = f'{fname}.txt'

                if cm.path.exists(fname):
                    cm.remove(fname)
                    console.print('Arquivo deletado com sucesso!')
                else:
                    console.print('O nome de arquivo informado não existe!')
            elif OP == '5':
                cm.system('cls')
            elif OP == '6':
                cm.system('cls')
                dir_atual = cm.getcwd()
                console.print(f'[blue]PASTA ATUAL:[/blue] [underline]{dir_atual}[/underline]')
                dir_atual = cm.listdir()
                for i in dir_atual:
                    console.print(i)
            elif OP == '7':
                cm.system('cls')
                console.print('########### ALTERANDO PASTA ATUAL ###########')
                destino = cm.chdir(console.input('Mudar para: '))
                console.print('PASTA ATUAL:', cm.getcwd())
            elif OP == '8': # Localização atual
                cm.system('cls')
                corrente = cm.getcwd()
                console.print(f'[blue]DIRETÓRIO CORRENTE:[/blue] [underline]{corrente}[/underline]')
        else:
            cm.system('cls')
            console.print('[bold red]Opção inválida, tente novamente![bold red]')
    except FileExistsError:
        console.print('Arquivo já existe!')
    except FileNotFoundError:
        console.print('Arquivo não encontrado')

cm.system('cls')
