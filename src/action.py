from tkinter import messagebox
import random

def cek_petak(self):
  self.start_bonus()
  self.pay_tax()
  self.pay_needs()
  self.bansos()

def start_bonus(self):
  if self.move_latch == True:
    if self.which_player_loc == 1:
      get_latch = False
      if get_latch == False:
        total_value = int(self.amount_read_player(self.which_player))
        total_value += 100000
        self.amount_add_player(self.which_player, int(total_value))
        messagebox.showinfo('Bonus Start', f'{self.which_player_name} mendapat bonus sebesar Rp.100.000 saat melewati start')
        self.stats_update()
        get_latch = True

def pay_rent(self):
  player_amount = int(self.amount_read_player(self.which_player)) - 100000
  player_amount_invers = int(self.amount_read_player(self.which_player_invers)) + 100000
  self.amount_add_player(self.which_player, player_amount)
  self.amount_add_player(self.which_player_invers, player_amount_invers)
  messagebox.showinfo('Informasi', f'{self.which_player_name} membayar sewa ke {self.which_player_name_invers} sebesar Rp. 100.000')

def pay_tax(self):
  cekProperti = self.props_read(self.which_player)
  daftar_properti = cekProperti.split(', ')

  base_value = 200000
  if self.which_player_loc == 3:
    total_value = int(self.amount_read_player(self.which_player)) - base_value
    total_value -= ((len(daftar_properti)-1) * (base_value/2))

    if cekProperti != '':
      self.amount_add_player(self.which_player, int(total_value))
      messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{total_value}\nDengan bangunan sejumlah {len(daftar_properti)-1}')
    else:
      messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{total_value}\nTanpa bangunan')

    self.kunci_dadu = False
    self.giliran = not self.giliran
    self.stats_update()

def pay_needs(self):
  cekProperti = self.props_read(self.which_player)
  total_value = int(self.amount_read_player(self.which_player))
  daftar_properti = cekProperti.split(', ')
  total_value -= ((len(daftar_properti)-1) * 50000)

  if self.which_player_loc == 19:
    if cekProperti == '':
      messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan listrik')
    else:
      self.amount_add_player(self.which_player, int(total_value))
      messagebox.showinfo('Pembayaran listrik', f'{self.which_player_name} membayar listrik sebesar Rp.{total_value}\nDengan bangunan sejumlah {len(daftar_properti)-1}')

  if self.which_player_loc == 35:
    if cekProperti == '':
      messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan air')
    else:
      self.amount_add_player(self.which_player, int(total_value))
      messagebox.showinfo('Pembayaran air', f'{self.which_player_name} membayar air sebesar Rp.{total_value}\nDengan bangunan sejumlah {len(daftar_properti)}')

  self.kunci_dadu = False
  self.giliran = not self.giliran
  self.stats_update()

def bansos(self):
  total_value = int(self.amount_read_player(self.which_player))
  total_value += (random.randint(20, 500) * 1000)
  if self.which_player_loc in [24, 36]:
    self.amount_add_player(self.which_player, int(total_value))
    messagebox.showinfo('Dapat Bansos', f'Selamat {self.which_player_name}, kamu mendapat bansos sebesar {total_value}')