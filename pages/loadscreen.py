from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def splash1(self):
  self.bg= import_image('assets/background.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

  self.logoM = import_image('assets/logo_M.png', png= True)
  self.canvas.create_image(361, 107, anchor='nw', image=self.logoM)
  
def splash2(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

def showof(self):
    self.logo= import_image('assets/monopoly_guy.png', png= 1)
    self.canvas.create_image(0, 417, anchor='nw', image=self.logo)

    self.title= import_image('assets/title_sub.png', png= 1)
    self.canvas.create_image(370, 164, anchor='nw', image=self.title)

    self.btn_bg= import_image('assets/btn_start.png', png= 1)
    self.btn_start= Button(self.frame, image= self.btn_bg, command= self.changeTo, bg='#9BB3CD', bd= 0, highlightthickness= 0)
    self.canvas.create_window(423, 559, anchor= 'nw', window= self.btn_start)