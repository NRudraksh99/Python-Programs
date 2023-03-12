from pytube import YouTube
from os import path
from random import randint
import memes

def download(l):
    yt=YouTube(l)
    v=yt.streams.get_highest_resolution()
    x=randint(0,10000)
    v.download(path.join("Videos",f"Vid{x}"))

l=input("Enter the link of the video to be downloaded, or enter '1' to choose from some Sample Videos: ")
if l=='1':
    print('''------> Sample Memes <-------
          1) Never Gonna Give You Up
          2) Undertale - Megalovania
          3) Wide Putin Meme
          4) Coffin Dance
          ''')
    y=int(input('Enter the Numebr Corresponding to your Choice: '))
    print("Downloading Video, please wait...",end='\r')
    if y==1:
        download(memes.rickroll)
    elif y==2:
        download(memes.u_megalovania)
    elif y==3:
        download(memes.wideP)
    elif y==4:
        download(coffin_dance)
    else:
        print('\n\nInvalid Choice...')
    print("\n\nVideo was Successfully Downloaded!")
else:
    download(l)
    print("\n\nVideo was Successfully Downloaded!")

