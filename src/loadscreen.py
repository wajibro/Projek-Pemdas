from tkinter import *
from PIL import Image, ImageTk

def splash1(self):
  self.bg_src = Image.open('assets/background-start.png')
  self.bg= ImageTk.PhotoImage(self.bg_src)

  self.logoM_src = Image.open('assets/logo-M.png').convert('RGBA')
  self.logoM = ImageTk.PhotoImage(self.logoM_src)

  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(361, 164, anchor='nw', image=self.logoM)

def splash2(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg_src = Image.open('assets/background-start.png')
  self.bg= ImageTk.PhotoImage(self.bg_src)

  self.logo_src = Image.open('assets/monopoli-guy.png').convert('RGBA')
  self.logo= ImageTk.PhotoImage(self.logo_src)

  self.title_src = Image.open('assets/title-sub.png').convert('RGBA')
  self.title= ImageTk.PhotoImage(self.title_src)

  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(0, 579, anchor='nw', image=self.logo)
  self.canvas.create_image(361, 339, anchor='nw', image=self.title)
