from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

list_town = [2, 5, 6, 7, 8, 10, 12, 13, 15, 18, 20, 22, 24, 27, 29, 30, 32, 34, 35, 37, 39, 40]
list_town1 = list_town[0:3]
list_town2 = list_town[3:6]
list_town3 = list_town[6:9]
list_town4 = list_town[9:11]
list_town5 = list_town[11:14]
list_town6 = list_town[14:17]
list_town7 = list_town[17:20]
list_town8 = list_town[20:23]
town_name = ['Medan', 'Makassar', 'Semarang', 'Bandung', 
             'Surabaya', 'Batam', 'Bekasi', 'Tanggerang', 
             'Depok', 'Jakarta', 'Banten', 'Ternate', 'Ambon', 
             'Padang', 'Palembang', 'Lampung', 'Pontianak', 
             'Banjarmasin', 'Balikpapan', 'Jogja', 'Solo', 'Denpasar']

def bg_image(self, x):
  if x in list_town1:
    return import_image('assets/bg_town1.png', png= 1)
  elif x in list_town2:
    return import_image('assets/bg_town2.png', png= 1)
  elif x in list_town3:
    return import_image('assets/bg_town3.png', png= 1)
  elif x in list_town4:
    return import_image('assets/bg_town4.png', png= 1)
  elif x in list_town5:
    return import_image('assets/bg_town5.png', png= 1)
  elif x in list_town6:
    return import_image('assets/bg_town6.png', png= 1)
  elif x in list_town7:
    return import_image('assets/bg_town7.png', png= 1)
  elif x in list_town8:
    return import_image('assets/bg_town8.png', png= 1)
  
def list_kota(self, x):
  if x in list_town:
    return town_name[list_town.index(x)]
  
def list_harga(self):
  giliran_loc = self.player2_loc if self.giliran else self.player1_loc
  
  self.town_title_bg = self.bg_image(giliran_loc)
  self.town_title = self.list_kota(giliran_loc)

  self.town_title_bg_item = self.canvas.create_image(0, 181, anchor='nw', image=self.town_title_bg)
  self.town_title_item = self.canvas.create_text(138, 184, anchor='nw', text= self.town_title, font=('Poppins', 20), fill= 'white')

def buy1_apar(self):
  pass

def buy2_apar(self):
  pass