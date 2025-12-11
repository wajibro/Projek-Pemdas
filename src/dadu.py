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
  if self.kunci_dadu == False:
    self.dadu_num = random.randint(1,6)
    self.pos_increase()
    self.giliran = not self.giliran

    self.cek_petak()
    self.stats_update()
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
      if self.player1_loc >= len(self.kordinat_x)-1:
        self.player1_loc += self.dadu_num - len(self.kordinat_x)-1
    
    elif self.giliran == True:
      self.player2_loc += self.dadu_num
      if self.player2_loc >= len(self.kordinat_x)-1:
        self.player2_loc += self.dadu_num - len(self.kordinat_x)-1

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