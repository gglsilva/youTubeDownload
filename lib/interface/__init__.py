# -*- coding: utf-8 -*-

def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
			continue
		except (KeyboardInterrupt):
			print('\033[31mUsario preferiu não digitar esse valor.\033[m')
			return 0
		else:
			return n


def linha(tam=42):
	return '-' * tam


def cabeçalho(tx):
    print('='*30)
    print('{:^30}'.format(tx))
    print('='*30)


def menu(lista):
    cabeçalho('YouTube Downloader V.1.2')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
