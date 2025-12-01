from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def name_init_screen(self):
  self.player1_name= StringVar()
  self.player2_name= StringVar()
  self.modal_amount= StringVar()

  self.canvas.configure(bg='#9BB3CD')

  self.bg= import_image('assets/background.png')
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  
  self.title = import_image('assets/title.png', rgba= 1)
  self.canvas.create_image(442.05, 96, anchor='nw', image=self.title)

  self.player1_bg = import_image('assets/player1_entry.png', rgba= 1)
  self.canvas.create_image(364, 259, anchor= 'nw', image= self.player1_bg)

  self.player2_bg = import_image('assets/player2_entry.png', rgba= 1)
  self.canvas.create_image(364, 352, anchor= 'nw', image= self.player2_bg)

  self.modal_bg = import_image('assets/modal_entry.png', rgba= 1)
  self.canvas.create_image(364, 472, anchor= 'nw', image= self.modal_bg)

  self.btn_bg = import_image('assets/btn_start.png', rgba= 1)
  self.btn_start= Button(self.frame, image= self.btn_bg, command= self.var_init, bg='#9BB3CD')
  self.canvas.create_window(410, 570, anchor= 'nw', window= self.btn_start)

  self.player1_entry = Entry(self.frame, width= 20, font=('Arial', 20), textvariable=self.player1_name, bg='#C3D827')
  self.player1_entry.place(x= 539, y= 270)

  self.player2_entry = Entry(self.frame, width= 20, font=('Arial', 20), textvariable=self.player2_name, bg='#C3D827')
  self.player2_entry.place(x= 539, y= 360)

  self.modal_amount= Entry(self.frame, width= 18, font=('Arial', 20), textvariable=self.modal_amount, bg='#C3D827')
  self.modal_amount.place(x= 609, y= 482)