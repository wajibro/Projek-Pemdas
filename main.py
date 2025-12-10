from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random

# Memasukkan file halaman
from pages import loadscreen, name_init, play 

# Memasukkan file src untuk program backend
from src import config, crud_player, kordinat, dadu, bidak, status_pemain, move_option, buy_props, action

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

#================= SETUP WINDOW ================#
def win_config():
   pass
win_config = config.win_config
window = win_config()
 #=================================================#

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

#============== SETUP CLASS ==============#
class setup: # Setup untuk semua halaman
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)

    # Merubah master menjadi self.canvas
    self.canvas = Canvas(self.frame, width=1280, height=720, highlightthickness=0) 
    self.canvas.pack(fill= 'both', expand= True)

    self.show() # Tampilkan semua halaman saat dijalankan
    self.hide() # Sembunyikan halaman saat dijalankan
    self.div() # Tampilkan UI tiap halaman

  def hide(self): # Fungsi untuk menghapus halaman
    self.frame.pack_forget()

  def show(self): # Fungsi untuk menampilkan halaman
    self.frame.pack(fill = 'both', expand = True)
#======================================#
# Fungsi untuk menambahkan nama pemain
setup.name_add = crud_player.name_add

# Fungsi untuk membaca nama pemain
setup.name_read_player = crud_player.name_read_player

# Fungsi untuk menambahkan jumlah uang pemain
setup.amount_read_player = crud_player.amount_read_player
#======================================#

#============== SCREEN 1 ==============#
class screen1(setup): # Halaman Loading Awal
  def __init__(self, master):
    super().__init__(master)
    # self.show() # Tampilkan halaman saat program dijalankan

    # Tunggu 3 detik kemudian jalankan self.changeTo
    self.master.after(3000, self.changeTo) 

  def changeTo(self):
    # Sembunyikan halaman saat ini
    self.hide()
    # Tampilkan halaman SCREEN2
    SCREEN2.show()
#======================================#
# Fungsi untuk tampilan
screen1.div = loadscreen.splash1
#======================================#

#============== SCREEN 2 ==============#
class screen2(setup): # Halaman awal
  def __init__(self, master):
    super().__init__(master)

    # Tunggu 3 detik kemudian jalankan self.showof
    self.master.after(3000, self.showof)

  def changeTo(self, event=None):
    # Sembunyikan halaman saat ini
    self.hide()
    # Tampilkan halaman SCREEN3
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
    # Tampilkan halaman SCREEN4
    SCREEN4.show()
    # Refresh tampilan data pemain
    SCREEN4.stats_update()
    
#======================================#
screen3.div = name_init.name_init_screen
screen3.changeTo = name_init.changeTo
screen3.amount_set = crud_player.amount_set
#======================================#
      
#============== SCREEN 4 ==============#
class screen4(setup): # Halaman permainan utama
  def __init__(self, master):
    super().__init__(master)
    self.show()

    # Inisiasi pengambilan assets apartement
    self.show_apar()

    # Inisiasi giliran pemain
    self.giliran = False

    # Inisiasi sistem kunci dadu
    self.kunci_dadu = False

    # Inisiasi posisi pemain
    self.player1_loc = 1
    self.player2_loc = 1

    # Mengkosongkan data properti pemain
    self.props_add('player1', '')
    self.props_add('player2', '')

    # Refresh tampilan data pemain
    self.stats_update()

    # Pengelompokan kordinat ke dalam x dan y
    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    # Inisiasi tampilan dadu
    self.list_dadu = import_image('assets/dadu_0.png', png=1)
    self.dadu_img_item = self.canvas.create_image(252, 637, anchor='nw', image=self.list_dadu)
#===============================================================================================#
# Tampilan Peta
screen4.div = play.play_screen

#================= Update Tampilan Status Pemain ==================#
screen4.stats_update = status_pemain.update_data
screen4.amount_add_player = crud_player.amount_add_player
screen4.amount_read_player = crud_player.amount_read_player
#==================================================================#

#================= Sistem Dadu ==================#
screen4.roll_dice = dadu.roll_dice
screen4.pos_increase = dadu.pos_increase
#===============================================#

#================= Update Tampilan Dadu ==================#
screen4.dice_img = dadu.dice_img
screen4.dadu_update = dadu.dadu_update
#=========================================================#

#================== Update Tampilan Bidak ==================#
screen4.pawn_update = bidak.x
#===========================================================#

#================== Opsi Beli Properti atau Lanjut ==================#
screen4.ask = move_option.ask
screen4.gonnaBuy = move_option.gonnaBuy
screen4.nextPlayer = move_option.nextPlayer
#====================================================================#

#================== Sistem Pembelian Properti ==================#
#======= UI Pembelian Properti =======#
# Fungsi mengembalikan gambar
screen4.bg_image = buy_props.bg_image
# Tampilan daftar harga dan sewa
screen4.list_harga = buy_props.list_harga
# Inisiasi Pengambilas asset apartement
screen4.show_apar = buy_props.show_apar
#=====================================#

# Fungsi mengembalikan nama kota
screen4.list_kota = buy_props.list_kota

#======== Fungsi Pembelian Properti =======#
# Menambahkan data pembelian properti
screen4.props_add = buy_props.props_add
# Periksa data pembelian yang sudah tersimpan
screen4.props_read = buy_props.props_read
# Sistem bayar pemain ketika berada di kota lawan
screen4.pay_props = action.pay_props
# Sistem beli properti pemain
screen4.buy1_apar = buy_props.buy1_apar
screen4.buy2_apar = buy_props.buy2_apar
#==========================================#

#===============================================================#
#============================================================================================#

SCREEN1 = screen1(window)
SCREEN2 = screen2(window)
SCREEN3 = screen3(window)
SCREEN4 = screen4(window)

window.mainloop()