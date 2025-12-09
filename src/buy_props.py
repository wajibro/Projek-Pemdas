from tkinter import *
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40, 50]

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
             'Irian','Padang', 'Palembang', 'Lampung', 
             'Pontianak','Banjarmasin', 'Balikpapan', 'Jogja', 
             'Solo', 'Denpasar']

koor_apar = [None] * max(list_town)
for i in range(6):
  town_index = list_town[i]
  koor_apar[town_index] = [(1044 + (47*list_town[0])) - (47.02*town_index), 632], [(1044-20 )+ (47*list_town[0]) - (47.02*town_index), 632]
for i in range(6, 11):
  town_index = list_town[i]
  koor_apar[town_index] = [561, (548 + (47*list_town[6])) - (47*town_index)], [561, ((548-22) + (47*list_town[6])) - (47*town_index)]
for i in range(11, 17):
  town_index = list_town[i]
  koor_apar[town_index] = [(645 - (47*list_town[11])) + (47*town_index), 64], [(645+20) - (47*list_town[11]) + (47*town_index), 64]
for i in range(17, len(list_town)-1):
  town_index = list_town[i]
  koor_apar[town_index] = [1129, 147 - (47*list_town[17]) + (47*town_index)], [1129, (147+22) - (47*list_town[17]) + (47*town_index)]

def props_add(self, player, prop): # Menambahkan nama pemain ke file teks
  if player == 'player1':
    with open('src/data_pemain/properti/player1_props.txt', 'w') as file:
      file.write(str(prop))
  elif player == 'player2':
    with open('src/data_pemain/properti/player2_props.txt', 'w') as file:
      file.write(str(prop))
  
def props_read(self, player): # Menambahkan nama pemain ke file teks
  if player == 'player1':
    with open('src/data_pemain/properti/player1_props.txt', 'r') as file:
      return file.read()
  elif player == 'player2':
    with open('src/data_pemain/properti/player2_props.txt', 'r') as file:
      return file.read()

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
  which_player_loc = self.player2_loc if self.giliran else self.player1_loc  

  self.town_title_bg = self.bg_image(which_player_loc)
  self.town_title = self.list_kota(which_player_loc)

  self.town_title_bg_item = self.canvas.create_image(0, 181, anchor='nw', image=self.town_title_bg)
  self.town_title_item = self.canvas.create_text(138, 184, anchor='nw', text= self.town_title, font=('Poppins', 20), fill= 'white')

def buy1_apar(self):
  which_player = 'player2' if self.giliran else 'player1'
  which_player_loc = self.player2_loc if self.giliran else self.player1_loc
  which_apar = self.apar2_img if self.giliran else self.apar1_img
  # Tampilan 
  self.buy1_btn.destroy()
  self.buy2_btn.destroy()
  self.buy1_price.destroy()
  self.buy2_price.destroy()

  # Fungsi
  town_name = self.list_kota(which_player_loc)
  prop_cache = self.props_read(which_player)
  player_amount = int(self.amount_read_player(which_player)) - 100000

  if prop_cache == '':
    self.canvas.create_image(koor_apar[which_player_loc][0][0], koor_apar[which_player_loc][0][1], anchor='nw', image=which_apar)

    self.props_add(which_player, town_name)

    self.amount_add_player(which_player, player_amount)
    
  elif prop_cache.count(town_name) >= 2:
    messagebox.showerror('Perhatikan!!', "Anda sudah memiliki properti di kota ini!")
  else:
    self.canvas.create_image(koor_apar[which_player_loc][1][0], koor_apar[which_player_loc][1][1], anchor='nw', image=which_apar)

    self.props_add(which_player, f'{prop_cache}, {town_name}')
    self.amount_add_player(which_player, player_amount)

  self.giliran = not self.giliran
  self.kunci_dadu = False
  self.stats_update()

def buy2_apar(self):
  which_player = 'player2' if self.giliran else 'player1'
  which_player_loc = self.player2_loc if self.giliran else self.player1_loc
  which_apar = self.apar2_img if self.giliran else self.apar1_img
  # Tampilan 
  self.buy1_btn.destroy()
  self.buy2_btn.destroy()
  self.buy1_price.destroy()
  self.buy2_price.destroy()

  # Fungsi
  town_name = self.list_kota(which_player_loc)
  prop_cache = self.props_read(which_player)
  player_amount = int(self.amount_read_player(which_player)) - 100000

  if prop_cache == '':
    self.canvas.create_image(koor_apar[which_player_loc][0][0], koor_apar[which_player_loc][0][1], anchor='nw', image=which_apar)
    self.canvas.create_image(koor_apar[which_player_loc][1][0], koor_apar[which_player_loc][1][1], anchor='nw', image=which_apar)

    self.props_add(which_player, f'{town_name}, {town_name}')
    self.amount_add_player(which_player, player_amount)
    
  elif prop_cache.count(town_name) >= 1:
    messagebox.showerror('Perhatikan!!', "Anda sudah memiliki properti di kota ini!\nMaksimal 2 properti dalam 1 kota")  

  self.giliran = not self.giliran
  self.kunci_dadu = False
  self.stats_update()

def show_apar(self):
  self.apar1_img = import_image('assets/apar_1.png', png= 1)
  self.apar2_img = import_image('assets/apar_2.png', png= 1)

  # koor_apar[petak][rumah ke n][0 = x, y = 1]