from tkinter import *
from PIL import Image, ImageTk
import time
import random

from pages import loadscreen, name_init, play
from src import kordinat, dadu

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

    self.player1_pawn = None
    self.player2_pawn = None  
    self.player1_pawnItem = None
    self.player2_pawnItem = None

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

    self.kordinat = kordinat.kordinat_peta()

    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    self.player1_loc = 1
    self.player2_loc = 1
    
  def pawn_update(self):
    if self.player1_loc >= len(self.kordinat)-1:
      self.player1_loc = 1
    if self.player2_loc >= len(self.kordinat)-1:
      self.player2_loc = 1
    print(len(self.kordinat_x))

    self.canvas.delete(self.player1_pawnItem)
    self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc]+2, self.kordinat_y[self.player1_loc]+2, anchor= 'nw',  image= self.player1_pawn)
    self.canvas.delete(self.player2_pawnItem)
    self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc]-2, self.kordinat_y[self.player2_loc]-2, anchor= 'nw',  image= self.player2_pawn)


  def roll_1(self, event=None):
    self.dadu_num = random.randint(1, 6)
    if self.giliran == True:
      self.player1_loc += self.dadu_num
    elif self.giliran == False:
      self.player2_loc += self.dadu_num

    self.pawn_update()
    self.giliran = not self.giliran

  def roll_2(self, event=None):
    self.dadu1 = dadu.roll_1()
    self.dadu2 = dadu.roll_1()

    if self.giliran == True:
      self.player1_loc += self.dadu1 + self.dadu2
    elif self.giliran == False:
      self.player2_loc += self.dadu1 + self.dadu2

    self.pawn_update()
    self.giliran = not self.giliran

screen4.div = play.play_screen


SCREEN = screen4(window)

window.mainloop()