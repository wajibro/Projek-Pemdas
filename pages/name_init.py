from tkinter import *
from PIL import Image, ImageTk

def name_init_screen(self):
  self.canvas.configure(bg='#9BB3CD')

  self.bg_src = Image.open('assets/background_start.png')
  self.bg= ImageTk.PhotoImage(self.bg_src)

  self.title_src = Image.open('assets/title.png').convert('RGBA')
  self.title= ImageTk.PhotoImage(self.title_src)

  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(428, 40, anchor='nw', image=self.title)