from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

move_point = 0

def roll_dice(self, event= None):
  global move_point
  # Cek status pemain saat ini
  player_index = int(self.giliran)
  current_player_status = self.player_status[player_index]

  # Logika untuk status 2: Terjebak di Pulau Asing
  if current_player_status == 2:
    self.dadu_num = random.randint(1, 6)
    self.dadu_update()

    if self.dadu_num == 6:
      self.player_status[player_index] = 0
      
      messagebox.showinfo('Selamat!', f'{self.which_player_name} berhasil keluar dari pulau asing!')
      self.pos_increase()
      turn_handled = self.cek_petak()
      self.stats_update()
      if not turn_handled:
        self.ask()
    else:
      messagebox.showwarning('Gagal', f'Maaf {self.which_player_name}, anda butuh dadu 6 untuk keluar.\nAnda didenda Rp 100.000')
      total_value = int(self.amount_read_player(self.which_player)) - 100000
      self.amount_add_player(self.which_player, total_value)
      self.stats_update()
      self.nextPlayer()
    return

  # Logika untuk status 1: Di Penjara
  elif current_player_status == 1:
    self.player_status[player_index] = 0
    
    messagebox.showinfo('Penjara', f'{self.which_player_name} telah bebas setelah skip 1 putaran.')
    self.nextPlayer()
    return

  # Logika giliran normal (status 0)
  elif self.kunci_dadu == False:
    self.dadu_num = random.randint(1,6)
    self.pos_increase()
    self.action_allow = True
    self.btn_allow = True
    
    turn_handled = self.cek_petak()
    self.stats_update()
    if not turn_handled:
      self.ask()

    if self.move_latch == False and move_point < 2:
      move_point += 1
    if move_point >= 2:
      self.move_latch = True
    return self.dadu_num
  else:
    messagebox.showwarning('Perhatikan', "Giliran anda sudah selesai\nPilih opsi 'Beli Properti' atau 'Lanjut'")

def pos_increase(self):
    if self.giliran == False:
      self.player1_loc += self.dadu_num
      if self.player1_loc > 40:
        self.player1_loc = self.player1_loc - 40
    
    elif self.giliran == True:
      self.player2_loc += self.dadu_num
      if self.player2_loc > 40:
        self.player2_loc = self.player2_loc - 40

    match self.player1_loc:
      case 4: # Tangga 1
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player1_name}, Anda tidak sengaja menemukan tangga')
        self.player1_loc = 38
      case 18: # Tangga 2
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player1_name}, Anda tidak sengaja menemukan tangga')
        self.player1_loc = 24
      case 14: # Ular 1
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player1_name}, Anda telah dimakan sang ular')
        self.player1_loc = 7
      case 27: # Ular 2
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player1_name}, Anda telah dimakan sang ular')
        self.player1_loc = 35

    match self.player2_loc:
      case 4: # Tangga 1
        self.pawn_update()
        messagebox.showinfo(f'{self.player2_name} - Telah Berubah Posisi', f'{self.player2_name}, Anda tidak sengaja menemukan tangga')
        self.player2_loc = 38
      case 18: # Tangga 2         
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player2_name}, Anda tidak sengaja menemukan tangga')
        self.player2_loc = 24
      case 14: # Ular 1
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player2_name}, Anda telah dimakan sang ular')
        self.player2_loc = 7
      case 27: # Ular 2
        self.pawn_update()
        messagebox.showinfo(f'{self.player1_name} - Telah Berubah Posisi', f'{self.player2_name}, Anda telah dimakan sang ular')
        self.player2_loc = 35
      
    self.pawn_update()
    self.stats_update()
    self.dadu_update()
    self.kunci_dadu = True
    
def dadu_update(self):
  self.list_dadu = self.dice_img(self.dadu_num)
  self.canvas.delete(self.dadu_img_item)
  self.dadu_img_item = self.canvas.create_image(252, 637, anchor='nw', image=self.list_dadu)

def dice_img(self, x):
  match x:
    case 0:
      return import_image('assets/dadu_0.png', png= 1)
    case 1:
      return import_image('assets/dadu_1.png', png= 1)
    case 2:
      return import_image('assets/dadu_2.png', png= 1)
    case 3:
      return import_image('assets/dadu_3.png', png= 1)
    case 4:
      return import_image('assets/dadu_4.png', png= 1)
    case 5:
      return import_image('assets/dadu_5.png', png= 1)
    case 6:
      return import_image('assets/dadu_6.png', png= 1)