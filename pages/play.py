from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def play_screen(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

  self.bar = import_image('assets/bar.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bar)

  self.peta = import_image('assets/peta.png')
  self.canvas.create_image(558, 64, anchor='nw', image=self.peta)

  self.dice1_btn = Button(self.frame, text='1 Dadu', font=('Poppins', 24), command= self.roll_1)
  self.dice1_btn.place(x=43, y=615)

  self.dice2_btn = Button(self.frame, text='2 Dadu', font=('Poppins', 24), command= self.roll_2)
  self.dice2_btn.place(x=230, y=615)

  self.player1_pawn = import_image('assets/player_1.png', rgba= 1)
  self.player1_pawnItem = self.canvas.create_image(1098, 602, anchor='nw', image=self.player1_pawn) 

  self.player2_pawn = import_image('assets/player_2.png', rgba= 1)
  self.player2_pawnItem = self.canvas.create_image(1102, 605, anchor='nw', image=self.player2_pawn)