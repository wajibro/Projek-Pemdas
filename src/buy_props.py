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

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]

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

koor_apar = [None] * 41
for i in range(6):
  town_index = list_town[i]
  koor_apar[town_index] = [(1044 + (47*list_town[0])) - (47.02*town_index), 632], [(1044-20 )+ (47*list_town[0]) - (47.02*town_index), 632]
for i in range(6, 11):
  town_index = list_town[i]
  koor_apar[town_index] = [561, (548 + (47*list_town[6])) - (47*town_index)], [561, ((548-22) + (47*list_town[6])) - (47*town_index)]
for i in range(11, 17):
  town_index = list_town[i]
  koor_apar[town_index] = [(645 - (47*list_town[11])) + (47*town_index), 64], [(645+20) - (47*list_town[11]) + (47*town_index), 64]
for i in range(17, len(list_town)):
  town_index = list_town[i]
  koor_apar[town_index] = [1129, 147 - (47*list_town[17]) + (47*town_index)], [1129, (147+22) - (47*list_town[17]) + (47*town_index)]

# Simpan data pembelian properti
def props_add(self, player, prop):
  if player == 'player1':
    with open('src/data_pemain/properti/player1_props.txt', 'w') as file:
      file.write(str(prop))
  elif player == 'player2':
    with open('src/data_pemain/properti/player2_props.txt', 'w') as file:
      file.write(str(prop))

# Periksa data pembelian yang sudah tersimpan
def props_read(self, player): 
  if player == 'player1':
    with open('src/data_pemain/properti/player1_props.txt', 'r') as file:
      return file.read()
  elif player == 'player2':
    with open('src/data_pemain/properti/player2_props.txt', 'r') as file:
      return file.read()

# Fungsi mengembalikan gambar background warna pada informasi harga
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

# Fungsi mengembalikan nama kota
def list_town_name(self, x): 
  if x in list_town:
    return town_name[list_town.index(x)]

def price_level(self):
  match self.which_player_loc:
    case x if x in list_town1:
      return 500000
    case x if x in list_town2:
      return 600000
    case x if x in list_town3:
      return 700000
    case x if x in list_town4:
      return 800000
    case x if x in list_town5:
      return 900000
    case x if x in list_town6:
      return 1000000
    case x if x in list_town7:
      return 1200000
    case x if x in list_town8:
      return 1400000
    case _:
      return 0
    
# Tampilan informasi harga beli dan sewa
def list_harga(self):
  harga = self.price_level()
  sewa1 = harga - (harga /2)
  sewa1 = int(sewa1)
  sewa2 = sewa1 * 2
  sewa2 = int(sewa2)

  self.town_title_bg = self.bg_image(self.which_player_loc)
  self.town_title = self.list_town_name(self.which_player_loc)

  self.canvas.delete(self.show_price_item)
  self.canvas.delete(self.show_rent1_item)
  self.canvas.delete(self.show_rent2_item)
  self.show_price_item = self.canvas.create_text(246, 360, anchor='nw', text= f'Rp {f"{int(harga):,}".replace(",", ".")}', font=('Poppins', 16), fill= 'black')
  self.show_rent1_item = self.canvas.create_text(281, 264, anchor='nw', text= f'Rp {f"{int(sewa1):,}".replace(",", ".")}', font=('Poppins', 16), fill= 'black')
  self.show_rent2_item = self.canvas.create_text(281, 294, anchor='nw', text= f'Rp {f"{int(sewa2):,}".replace(",", ".")}', font=('Poppins', 16), fill= 'black')
  
  if harga == 0:
    self.canvas.delete(self.show_price_item)
    self.canvas.delete(self.show_rent1_item)
    self.canvas.delete(self.show_rent2_item)
  else:
    if hasattr(self, 'card_bg_item'):
      self.canvas.delete(self.card_bg_item)
      self.canvas.delete(self.card_text)

  self.town_title_bg_item = self.canvas.create_image(0, 181, anchor='nw', image=self.town_title_bg)
  self.town_title_item = self.canvas.create_text(138, 184, anchor='nw', text= self.town_title, font=('Poppins', 20), fill= 'white')

# Fungsi untuk membeli 1 apartement
def buy1_apar(self, event=None):
  harga = self.price_level()
  which_apar = self.apar2_img if self.giliran else self.apar1_img

  # Tampilan 
  self.buy1_btn.destroy()
  self.buy2_btn.destroy()
  self.buy1_price.destroy()
  self.buy2_price.destroy()

  # Fungsi
  town_name = self.list_town_name(self.which_player_loc)
  prop_cache = self.props_read(self.which_player)
  player_amount = int(self.amount_read_player(self.which_player)) - harga

  if town_name not in prop_cache:
    self.canvas.create_image(koor_apar[self.which_player_loc][0][0], koor_apar[self.which_player_loc][0][1], anchor='nw', image=which_apar)

    self.props_add(self.which_player, f'{prop_cache}, {town_name}')

    self.amount_add_player(self.which_player, player_amount)
    
  elif prop_cache.count(town_name) >= 2:
    messagebox.showerror('Perhatikan!!', "Anda sudah memiliki properti di kota ini!")
  else:
    self.canvas.create_image(koor_apar[self.which_player_loc][1][0], koor_apar[self.which_player_loc][1][1], anchor='nw', image=which_apar)

    self.props_add(self.which_player, f'{prop_cache}, {town_name}')
    self.amount_add_player(self.which_player, player_amount)

  if hasattr(self, 'gonnaBuy_btn'):
    self.gonnaBuy_btn.destroy()
  if hasattr(self, 'nextPlayer_btn'):
    self.nextPlayer_btn.destroy()
  
  self.nextPlayer()

# Fungsi untuk membeli 2 apartement
def buy2_apar(self, event=None):
  harga = self.price_level()
  which_apar = self.apar2_img if self.giliran else self.apar1_img
  
  # Tampilan 
  self.buy1_btn.destroy()
  self.buy2_btn.destroy()
  self.buy1_price.destroy()
  self.buy2_price.destroy()

  # Fungsi
  town_name = self.list_town_name(self.which_player_loc)
  prop_cache = self.props_read(self.which_player)
  player_amount = int(self.amount_read_player(self.which_player)) - harga

  if town_name not in prop_cache:
    self.canvas.create_image(koor_apar[self.which_player_loc][0][0], koor_apar[self.which_player_loc][0][1], anchor='nw', image=which_apar)
    self.canvas.create_image(koor_apar[self.which_player_loc][1][0], koor_apar[self.which_player_loc][1][1], anchor='nw', image=which_apar)

    self.props_add(self.which_player, f'{prop_cache}, {town_name}, {town_name}')
    self.amount_add_player(self.which_player, player_amount)
    
  else:
    messagebox.showerror('Perhatikan!!', "Anda sudah memiliki properti di kota ini!\nMaksimal 2 properti dalam 1 kota")  

  if hasattr(self, 'gonnaBuy_btn'):
    self.gonnaBuy_btn.destroy()
  if hasattr(self, 'nextPlayer_btn'):
    self.nextPlayer_btn.destroy()
  
  self.nextPlayer()

def show_apar(self):
  self.apar1_img = import_image('assets/apar_1.png', png= 1)
  self.apar2_img = import_image('assets/apar_2.png', png= 1)

  # koor_apar[petak][rumah ke n][0 = x, y = 1]