#    ___   ___  _____ __      __   |
#   | _ \ / _ \|_   _|\ \    / /   |   Rúben Cavaco
#   |   /| (_) | | |   \ \/\/ /    |   rcavaco@protonmail.ch
#   |_|_\ \___/  |_|    \_/\_/     |   https://github.com/ResOfTheWolph/
#                                  |


#   instalação do tkinter usando o pip
#   tkinter installation using pip
from tkinter import *


#   importação do pyperclip usando o pip
#   pyperclip imports using pip
import pyperclip
import random


#   Secção de código responsável pelo design da janela
#   Section of the code responsible for the design of the window
root = Tk()
root.geometry("700x300")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)


#   Secção do código responsável pela criação da password
#   Section of the code responsible to generate the password
def generate():
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)


#   Secção do código responsável por copiar a password para a área de tansferência
#   Section of the code responsible to copy the password to the clipboard
def copyclipboard():
	random_password = passwrd.get()
	pyperclip.copy(random_password)


#   Secção de código responsável pelo design do programa
#   Section of the coe responsible for the design of the program
Label(root, text="ROTW Password Generator", font="Courier 30 bold").pack()
Label(root, text="by Rúben Cavaco", font="Courier 20 italic").pack()
Label(root, text="Coloque o tamanho de caracteres desejados").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Clique para gerar password", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Clique para copiar a password", command=copyclipboard).pack()
root.mainloop()
