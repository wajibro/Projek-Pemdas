from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

with open('src/player1_name.txt', 'r') as file:
  player1_name = file.read()
with open('src/player1_amount.txt', 'r') as file:
  player1_amount = file.read()

with open('src/player2_name.txt', 'r') as file:
  player2_name = file.read()
with open('src/player2_amount.txt', 'r') as file:
  player2_amount = file.read()

def play_screen(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

  self.bar = import_image('assets/bar.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bar)

  self.peta = import_image('assets/peta.png')
  self.canvas.create_image(558, 64, anchor='nw', image=self.peta)

  self.player1_name = Label(self.frame, text=f'Player 1 - {player1_name}', font=('Poppins', 24), bg='white')
  self.player1_amount = Label(self.frame, text=f'Rp. {player1_amount}', font=('Poppins', 24))
  self.player1_name.place(x=9, y=7)
  self.player1_amount.place(x=9, y=40)
  
  self.player2_name = Label(self.frame, text=f'Player 2 - {player2_name}', font=('Poppins', 24), bg='white')
  self.player2_amount = Label(self.frame, text=f'Rp. {player2_amount}', font=('Poppins', 24))
  self.player2_name.place(x=9, y=84)
  self.player2_amount.place(x=9, y=120)

  self.dice1_btn = Button(self.frame, text='1 Dadu', font=('Poppins', 24), command= self.roll_1)
  self.dice1_btn.place(x=43, y=615)

  self.dice2_btn = Button(self.frame, text='2 Dadu', font=('Poppins', 24), command= self.roll_2)
  self.dice2_btn.place(x=230, y=615)

  self.player1_pawn = import_image('assets/player_1.png', rgba= 1)
  self.player1_pawnItem = self.canvas.create_image(1036, 596, anchor='nw', image=self.player1_pawn) 

  self.player2_pawn = import_image('assets/player_2.png', rgba= 1)
  self.player2_pawnItem = self.canvas.create_image(1066, 596, anchor='nw', image=self.player2_pawn)