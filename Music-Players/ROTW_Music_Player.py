#    ___   ___  _____ __      __   |
#   | _ \ / _ \|_   _|\ \    / /   |   Rúben Cavaco
#   |   /| (_) | | |   \ \/\/ /    |   rcavaco@protonmail.ch
#   |_|_\ \___/  |_|    \_/\_/     |   https://github.com/ResOfTheWolph/
#                                  |

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("ROTW Music Player")
music_player.geometry("500x400")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 10 bold", bg='white', fg="black", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play(loops = -1)
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 11 bold", text="-   Tocar Música   -", command=play, bg="#e1d7bf", fg="#3776ab")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 11 bold", text="-   Parar Música   -", command=stop, bg="#e1d7bf", fg="#ba3230")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 11 bold", text="-   Pausar Música   -", command=pause, bg="#e1d7bf", fg="#2F5E55")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 11 bold", text="-   Retirar Pausa   -", command=unpause, bg="#e1d7bf", fg="#2F5E55")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 10 bold", bg='white', fg="black", textvariable=var)

song_title.pack(fill="x", expand="yes")
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="x", expand="yes")
music_player.mainloop()

