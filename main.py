from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random

from pages import loadscreen, name_init, play # Memasukkan file halaman
from src import config, crud_player, kordinat, dadu, bidak, status_pemain

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

 #======================================#
def win_config():
   pass
win_config = config.win_config
window = win_config()
 #======================================#

#=============== Fungsi Fullscreen ================#
# window.attributes('-fullscreen', not window.attributes('-fullscreen'))
def toggle_fullscreen(event=None):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))
    return "break"

def exit_fullscreen(event=None):
    window.attributes('-fullscreen', False)
    return "break"

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', exit_fullscreen)
#==================================================#

class setup:
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)

    self.canvas = Canvas(self.frame, width=1280, height=720, highlightthickness=0) # Merubah master menjadi self.canvas
    self.canvas.pack(fill= 'both', expand= True)

    self.div()

  def hide(self): # Fungsi untuk menghapus halaman
    self.frame.pack_forget()

  def show(self): # Fungsi untuk menampilkan halaman
    self.frame.pack(fill = 'both', expand = True)
#======================================#
setup.name_add = crud_player.name_add
setup.name_read_player = crud_player.name_read_player
setup.amount_read_player = crud_player.amount_read_player
#======================================#

#============== SCREEN 1 ==============#
class screen1(setup):
  def __init__(self, master):
    super().__init__(master)
    self.show() # Tampilkan halaman saat program dijalankan
    self.master.after(3000, self.changeTo) # Tunggu 3 detik kemudian jalankan self.changeTo

  def changeTo(self): # Menyembunyikan halaman saat ini kemudian tampilkan halaman SCREEN2
    self.hide()
    SCREEN2.show()
#======================================#
screen1.div = loadscreen.splash1
#======================================#

#============== SCREEN 2 ==============#
class screen2(setup): # Halaman awal
  def __init__(self, master):
    super().__init__(master)
    self.master.after(3000, self.showof)

    window.bind('<Return>', self.changeTo) # Tekan 'Enter' kemudian jalankan self.changeTo

  def changeTo(self, event=None): # Menyembunyikan halaman saat ini kemudian tampilkan halaman SCREEN3
    self.hide()
    SCREEN3.show()
#======================================#
screen2.div = loadscreen.splash2
screen2.showof = loadscreen.showof
#======================================#

#============== SCREEN 3 ==============#
class screen3(setup): # Halaman inisialisasi nama pemain
  def __init__(self, master):
    super().__init__(master)

  def screen4(self):
    SCREEN4.show()
    SCREEN4.stats_update()
#======================================#
screen3.div = name_init.name_init_screen
screen3.amount_set = name_init.amount_set
screen3.changeTo = name_init.changeTo
#======================================#
      
#============== SCREEN 4 ==============#
class screen4(setup): # Halaman permainan utama
  def __init__(self, master):
    super().__init__(master)
    self.giliran = True

    self.kordinat = kordinat.kordinat_peta()
    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    self.player1_loc = 1
    self.player2_loc = 1
#======================================#
screen4.div = play.play_screen
screen4.pawn_update = bidak.x
screen4.stats_update = status_pemain.x
screen4.roll_dice = dadu.x
#======================================#

SCREEN1 = screen1(window)
SCREEN2 = screen2(window)
SCREEN3 = screen3(window)
SCREEN4 = screen4(window)

window.mainloop()