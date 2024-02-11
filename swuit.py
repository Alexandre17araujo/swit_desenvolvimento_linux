#!/usr/bin/python3

import os
import socket


while True:
    print('''\n\033[1;32m  ####### OPÇÕES #######
1 - Mostrar todas as PORTAS abertas
2 - Mostrar todos os diretorios no local atual
3 - Realizar um scanner de PORTAS e BANNER no site PMZ
4 - SAIR\033[m''')

    usuario_escolher = int(input('\nInforme o número da ação que deseja executar: '))

    if (usuario_escolher == 1):
        print('\033[1;33m')
        os.system('netstat -nltp')
        print('\033[m')

    elif usuario_escolher == 2:
        print('\033[1;33m')
        os.system('ls -all')
        print('\033[m')

    elif (usuario_escolher == 3):
        ip = input('Informe o IP do SITE: ')
        for portas in range(1, 65535):
            meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            meusocket.settimeout(1)
            try:
                meusocket.connect((ip, portas))
                banner = meusocket.recv(1024)
                print("Porta {} Aberta - BANNER: {}".format(portas, banner.decode('utf-8')))
            except (socket.timeout, ConnectionRefusedError):
                print('Porta {} Fechada'.format(portas))
            finally:
                meusocket.close()

            
    elif (usuario_escolher == 4):
        print('Saindo')
        break

