from tkinter import *
from tkinter import messagebox

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]

def ask(self):
  which_player_loc = self.player2_loc if self.giliran else self.player1_loc  
  which_player = 'player2' if self.giliran else 'player1'
  which_player_invers = 'player1' if self.giliran else 'player2'

  is_town = self.list_kota(which_player_loc)
  prop_cache_invers = self.props_read(which_player_invers)

  if which_player_loc in list_town:
    self.gonnaBuy_btn = Button(self.frame, text= 'Beli Properti', command= self.gonnaBuy, font=('Poppins', 18))
    self.nextPlayer_btn = Button(self.frame, text= 'Lanjut', command= self.nextPlayer, font=('Poppins', 18))

    if is_town in prop_cache_invers:
      self.gonnaBuy_btn.destroy()
      self.nextPlayer_btn.destroy()

      player_amount = int(self.amount_read_player(which_player)) - 100000
      player_amount_invers = int(self.amount_read_player(which_player_invers)) + 100000
      self.amount_add_player(which_player, player_amount)
      self.amount_add_player(which_player_invers, player_amount_invers)
      messagebox.showinfo('Informasi', f'{self.player2_name if self.giliran else self.player1_name} membayar sewa ke {self.player1_name if self.giliran else self.player2_name} sebesar Rp. 100.000')
      self.kunci_dadu = False
      self.giliran = not self.giliran
      self.stats_update()
    else:
      self.gonnaBuy_btn.place(x= 41, y= 499)
      self.nextPlayer_btn.place(x= 221, y= 499)

  else:
    if hasattr(self, 'gonnaBuy_btn'):
      self.gonnaBuy_btn.destroy()
    if hasattr(self, 'nextPlayer_btn'):
      self.nextPlayer_btn.destroy()
    self.kunci_dadu = False
    self.giliran = not self.giliran
    self.stats_update()
    # self.action

def gonnaBuy(self):
  self.thisTownPrice = 100000
  self.gonnaBuy_btn.destroy()
  self.nextPlayer_btn.destroy()

  self.buy1_btn = Button(self.frame, text= 'Bangun 1 Apartement', command= self.buy1_apar, font=('Poppins', 12))
  self.buy2_btn = Button(self.frame, text= 'Bangun 2 Apartement', command= self.buy2_apar, font=('Poppins', 12))

  self.buy1_price = Label(self.frame, text= f'-{self.thisTownPrice}', fg= 'red', bg= 'white', font= ('Poppins', 16))
  self.buy2_price = Label(self.frame, text= f'-{int(self.thisTownPrice + (self.thisTownPrice * 1/2))}', fg= 'red', bg= 'white', font= ('Poppins', 16))

  self.buy1_btn.place(x= 53, y= 480)
  self.buy2_btn.place(x= 225, y= 480)

  self.buy1_price.place(x= 68, y= 511)
  self.buy2_price.place(x= 230, y= 511)

def nextPlayer(self):
  self.gonnaBuy_btn.destroy()
  self.nextPlayer_btn.destroy()
  
  self.giliran = not self.giliran
  self.kunci_dadu = False
  self.stats_update()