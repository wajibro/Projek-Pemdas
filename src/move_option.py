from tkinter import *
from tkinter import messagebox

'''
tampilan_opsi = opsi_ui.tampilan_opsi
tampilan_inginBeli = opsi_ui.tampilan_inginBeli
'''

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]

def ask(self):
  self.canvas.delete(self.dice_btn_item)
  properti_lawan = self.which_player_props_read(self.which_player_invers)
  if self.which_player_loc in properti_lawan:
    self.pay_rent()
    self.nextPlayer()
  else:
    self.tampilan_opsi()

def gonnaBuy(self, event=None):  
  self.tampilan_inginBeli()

def nextPlayer_cta(self):
  self.canvas.delete(self.gonnaBuy_item)
  self.canvas.delete(self.nextPlayer_item)
  self.nextPlayer()

def nextPlayer(self):
  self.game_over()
  self.giliran = not self.giliran
  self.pawn_update()
  self.stats_update()
  self.dice_btn_item = self.canvas.create_window(29, 644, anchor='nw', window=self.dice_btn)