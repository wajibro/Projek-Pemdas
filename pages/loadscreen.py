from tkinter import *
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)
#========================== SCREEN 1 ==========================#
def splash1(self):
  # Alamat assets
  self.team_name = import_image('assets/team-screen.png')

  # Penempatan assets
  self.team_nameItem = self.canvas.create_image(0, 0, anchor='nw', image=self.team_name)
  
def showof1(self):
  self.canvas.delete(self.team_nameItem)

  # Alamat assets
  self.bg= import_image('assets/background.png')
  self.logoM = import_image('assets/logo_M.png', png= True)

  # Penempatan assets
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(361, 107, anchor='nw', image=self.logoM)

  # Tunggu 3 detik kemudian jalankan self.changeTo
  self.master.after(3000, self.changeTo) 
#==============================================================#

#========================== SCREEN 2 ==========================#
def splash2(self):
  # Warna background
  self.canvas.configure(bg='#9BB3CD')

  # Alamat assets
  self.bg= import_image('assets/background.png')

  # Penempatan assets
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)

def showof2(self):
  # Alamat assets
  self.logo= import_image('assets/monopoly_guy.png', png= 1)
  self.title= import_image('assets/title_sub.png', png= 1)
  self.btn_bg= import_image('assets/btn_start.png', png= 1)

  # Inisiasi button
  self.btn_start= Button(self.frame, image= self.btn_bg, command= self.changeTo, bg='#9BB3CD', bd= 0, highlightthickness= 0)
  
  # Penempatan assets
  self.canvas.create_image(0, 417, anchor='nw', image=self.logo)
  self.canvas.create_image(370, 164, anchor='nw', image=self.title)
  self.canvas.create_window(423, 559, anchor= 'nw', window= self.btn_start)
  #==============================================================#