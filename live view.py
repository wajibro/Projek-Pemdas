from tkinter import *
from PIL import Image, ImageTk
import time
import random

from pages import loadscreen, name_init, play

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

window = Tk()
window.title('Monopoly')
window.iconbitmap('assets/icon.ico')
window.geometry('1280x720')

class setup:
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)

    self.canvas = Canvas(self.frame, width=1280, height=720, highlightthickness=0)
    self.canvas.pack(fill= 'both', expand= True)

    self.div()

  def hide(self):
    self.frame.pack_forget()

  def show(self):
    self.frame.pack(fill = 'both', expand = True)

class screen4(setup):
  def __init__(self, master):
    super().__init__(master)
    self.show()

    self.giliran = True

    self.kordinat = [[0,0]]
    for i in range(0, 9): # Garis Bawah Peta
      self.kordinat.append([1036-(48*i), 813])

    for i in range(1, 9): # Garis Kiri Peta
      self.kordinat.append([1036-(48*8), 813-(76*i)])

    for i in range(1, 9): # Garis Atas Peta
      self.kordinat.append([(1036-(48*8))+(76*i), 813-(76*8)])

    for i in range(1, 8): # Garis Kanan Peta
      self.kordinat.append([1036, 813-(48*8)+(76*i)])

    self.kordinat_x = [x[0] for x in self.kordinat]
    self.kordinat_y = [x[1] for x in self.kordinat]

    self.player1_loc = 1
    self.player2_loc = 1
    
  def pawn_update(self):
    self.canvas.delete(self.player1_pawnItem)
    self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc], self.kordinat_y[self.player1_loc], anchor= 'nw',  image= self.player1_pawn)
    self.canvas.delete(self.player2_pawnItem)
    self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc], self.kordinat_y[self.player2_loc], anchor= 'nw',  image= self.player2_pawn)

  def roll_1(self, event=None):
    if self.giliran == True:
      self.player1_loc += random.randint(1, 6)
    elif self.giliran == False:
      self.player2_loc += random.randint(1, 6)

    self.pawn_update()
    self.giliran = not self.giliran

  def roll_2(self, event=None):
    if self.giliran == True:
      self.player1_loc += random.randint(1, 6) + random.randint(1, 6)
    elif self.giliran == False:
      self.player2_loc += random.randint(1, 6) + random.randint(1, 6)

    self.pawn_update()
    self.giliran = not self.giliran

screen4.div = play.play_screen


SCREEN = screen4(window)

window.mainloop()