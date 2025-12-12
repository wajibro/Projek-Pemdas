from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def play_screen(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background.png')
  self.bar = import_image('assets/bar.png')
  self.peta = import_image('assets/peta.png')  
  self.player1_pawn = import_image('assets/player_1.png', png= 1)
  self.player2_pawn = import_image('assets/player_2.png', png= 1)

  self.dice_btn = Button(self.frame, text='Lempar', font=('Poppins', 24), command= self.roll_dice, pady= 2, padx = 1)
  
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(0, 0, anchor='nw', image=self.bar)
  self.canvas.create_image(9, 16, anchor='nw', image=self.player1_pawn)
  self.canvas.create_image(9, 92, anchor='nw', image=self.player2_pawn)
  self.canvas.create_image(558, 64, anchor='nw', image=self.peta)
  self.player1_pawnItem = self.canvas.create_image(1098, 602, anchor='nw', image=self.player1_pawn) 
  self.player2_pawnItem = self.canvas.create_image(1102, 605, anchor='nw', image=self.player2_pawn)
  self.dice_btn.place(x=29, y=644)

  self.show_price_item = self.canvas.create_text(246, 360, anchor='nw', text= '0', font=('Poppins', 16), fill= 'black')
  self.show_rent1_item = self.canvas.create_text(281, 264, anchor='nw', text= '0', font=('Poppins', 16), fill= 'black')
  self.show_rent2_item = self.canvas.create_text(281, 294, anchor='nw', text= '0', font=('Poppins', 16), fill= 'black')