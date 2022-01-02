# -*- coding: utf-8 -*-
from pytube import YouTube, Playlist
from time import sleep

SAVE_PATH = '/home/gabriel-ativ/Vídeos/'

def download_video(url):
    try:
        yt = YouTube(url)
    except:
        print('Erro na conecção com o YouTube')
    try:
        video = yt.streams.get_highest_resolution().download(SAVE_PATH)
    except:
        print('Erro ao baixar o video')
    print('Video baixado com sucesso!')
    sleep(2)


def download_playlist_video(url):
    for video in Playlist(url):
        try:
            yt = YouTube(video)
        except:
            print('Erro na conecção com o YouTube')
        try:
            p_video = yt.streams.get_highest_resolution().download(SAVE_PATH)
        except:
            print('Erro ao baixar o video')
        print(f'Video URL:{video} baixado com sucesso!')
    sleep(2)
        

def download_audio(url):
    sucess = False
    try:
        yt = YouTube(url)
    except:
        print('Erro na conecção com o YouTube')
    try:
        audio = yt.streams.filter(only_audio=True)[0]
        audio.download(SAVE_PATH)
        sucess = True
    except:
        print('Erro ao baixar o audio')
    print('Video baixado com sucesso!')
    sleep(2)



def download_playlist_audio(url):
    for video in Playlist(url):
        print(f'Video URL:{video}')
        try:
            yt = YouTube(video)
        except:
            print('Erro na conecção com o YouTube')
        try:
            audio = yt.streams.filter(only_audio=True)[0]
            audio.download(SAVE_PATH)
        except:
            print('Erro ao baixar o audio')
        print(f'Audio URL:{video} baixado com sucesso!')
    sleep(2)