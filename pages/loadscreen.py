from tkinter import *
from PIL import Image, ImageTk

def import_image(src):
  x = Image.open(src)
  return ImageTk.PhotoImage(x)

def import_imageRGBA(src):
  x = Image.open(src).convert('RGBA')
  return ImageTk.PhotoImage(x)


def splash1(self):
  self.bg= import_image('assets/background-start.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

  self.logoM = import_imageRGBA('assets/logo-M.png')
  self.canvas.create_image(361, 164, anchor='nw', image=self.logoM)
  
def splash2(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background-start.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

  self.logo= import_imageRGBA('assets/monopoli-guy.png')
  self.canvas.create_image(0, 579, anchor='nw', image=self.logo)

  self.title= import_imageRGBA('assets/title-sub.png')
  self.canvas.create_image(361, 339, anchor='nw', image=self.title)