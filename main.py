# -*- coding: utf-8 -*-
from lib.interface import *
from lib.functions import *
from time import sleep


while True:
    resp = menu(['Download Video','Download Playlist Video', 'Download Audio', 'Download Playlist Audio', 'Sair'])
    if resp == 1:
        url = str(input('Digite a url do video: '))
        download_video(url)
    elif resp == 2:
        url = input('Digite a url da playlist: ')
        download_playlist_video(url)
    elif resp == 3:
        url = input('Digite a url do audio: ')
        download_audio(url)
    elif resp == 4:
        url = input('Digite a url da playlist: ')
        download_playlist_audio(url)
    elif resp == 5:
        print('Saindo...')
        sleep(2)
        exit()
        