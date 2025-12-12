from tkinter import *
from tkinter import messagebox

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]

def ask(self):
  self.stats_update()
  is_town = self.list_town_name(self.which_player_loc)
  prop_cache_invers = self.props_read(self.which_player_invers)

  if self.which_player_loc in list_town:
    self.gonnaBuy_btn = Button(self.frame, text= 'Beli Properti', command= self.gonnaBuy, font=('Poppins', 18))
    self.nextPlayer_btn = Button(self.frame, text= 'Lanjut', command= self.nextPlayer, font=('Poppins', 18))

    self.gonnaBuy_btn.place(x= 41, y= 499)
    self.nextPlayer_btn.place(x= 221, y= 499)
  else:
    if hasattr(self, 'gonnaBuy_btn'):
      self.gonnaBuy_btn.destroy()
    if hasattr(self, 'nextPlayer_btn'):
      self.nextPlayer_btn.destroy()

    self.kunci_dadu = False
    self.stats_update()
  
  if prop_cache_invers == None:
    pass
  elif is_town == None:
    pass
  elif is_town in prop_cache_invers:
    self.gonnaBuy_btn.destroy()
    self.nextPlayer_btn.destroy()
    
    self.pay_rent()
    self.kunci_dadu = False
    if hasattr(self, 'gonnaBuy_btn'):
      self.gonnaBuy_btn.destroy()
    if hasattr(self, 'nextPlayer_btn'):
      self.nextPlayer_btn.destroy()
    
    self.giliran = not self.giliran
    self.stats_update()

def gonnaBuy(self, event=None):
  harga = self.price_level()
  
  self.gonnaBuy_btn.destroy()
  self.nextPlayer_btn.destroy()

  self.buy1_btn = Button(self.frame, text= 'Bangun 1 Apartement', command= self.buy1_apar, font=('Poppins', 12))
  self.buy2_btn = Button(self.frame, text= 'Bangun 2 Apartement', command= self.buy2_apar, font=('Poppins', 12))

  self.buy1_price = Label(self.frame, text= f'-{int(harga)}', fg= 'red', bg= 'white', font= ('Poppins', 16))
  self.buy2_price = Label(self.frame, text= f'-{int(harga + (harga/2))}', fg= 'red', bg= 'white', font= ('Poppins', 16))

  self.buy1_btn.place(x= 53, y= 480)
  self.buy2_btn.place(x= 225, y= 480)

  self.buy1_price.place(x= 68, y= 511)
  self.buy2_price.place(x= 230, y= 511)

def nextPlayer(self, event=None):
  if hasattr(self, 'gonnaBuy_btn'):
    self.gonnaBuy_btn.destroy()
  if hasattr(self, 'nextPlayer_btn'):
    self.nextPlayer_btn.destroy()
  
  self.giliran = not self.giliran
  self.kunci_dadu = False
  self.stats_update()