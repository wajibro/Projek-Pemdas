from tkinter import *
from PIL import Image, ImageTk
import time

from pages import loadscreen, name_init

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

class screen3(setup):
  def __init__(self, master):
    super().__init__(master)
    self.show()

    self.player1_name= StringVar()
    self.player2_name= StringVar()
    self.modal_amount= StringVar()

  def div(self):
    pass

  def var_init(self):
    with open('src/player1_name.txt', 'w') as file:
      file.write(self.player1_name.get())

    with open('src/player2_name.txt', 'w') as file:
      file.write(self.player2_name.get())

    with open('src/modal_amount.txt', 'w') as file:
      file.write(self.modal_amount.get())

screen3.div = name_init.name_init_screen

SCREEN = screen3(window)

window.mainloop()