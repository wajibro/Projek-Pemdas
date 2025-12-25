from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import time
import random
import ctypes
import os

# Memasukkan file halaman
from pages import loadscreen, name_init, play, opsi_ui

# Memasukkan file src untuk program backend
from src import config

from src import kordinat
from src import bidak, status_pemain
from src import dadu, data_handle, move_option, buy_props, action, ular_tangga

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def load_font(font_path):
    if os.path.exists(font_path):
        FR_PRIVATE = 0x10
        return ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
    return 0

# Load the custom font
font_path = os.path.join(os.path.dirname(__file__), 'assets', 'Poppins-Regular.ttf')
fonts_loaded = load_font(font_path)

#================= SETUP WINDOW ================#
def win_config():
   pass
win_config = config.win_config
window = win_config()
 #=================================================#

#=============== Fungsi Fullscreen ================#
window.attributes('-fullscreen', not window.attributes('-fullscreen'))
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

    self.show()
    self.hide()
    self.div() # Tampilkan UI tiap halaman

  def hide(self): # Fungsi untuk menghapus halaman
    self.frame.pack_forget()

  def show(self): # Fungsi untuk menampilkan halaman
    self.frame.pack(fill = 'both', expand = True)
#======================================#

#============== SCREEN 1 ==============#
class screen1(setup): # Halaman Loading Awal
  def __init__(self, master):
    super().__init__(master)
    # Tampilkan halaman saat program dijalankan
    self.master.after(5000, self.showof)

  def changeTo(self):
    # Sembunyikan halaman saat ini
    self.hide()
    # Tampilkan halaman SCREEN2
    SCREEN2.show()
#======================================#
# Fungsi untuk tampilan
screen1.div = loadscreen.splash1
screen1.showof = loadscreen.showof1
#======================================#
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
screen2.showof = loadscreen.showof2
#======================================#

#============== SCREEN 3 ==============#
class screen3(setup): # Halaman inisialisasi nama pemain
  def __init__(self, master):
    super().__init__(master)

    self.player1_name = ''
    self.player2_name = ''
    self.player_amount = 0

  def screen4(self):
    # Ambil data dari SCREEN3 dan siapkan permainan di SCREEN4
    SCREEN4.setup_game()
    # Tampilkan halaman SCREEN4
    SCREEN4.show()

#======================================#
screen3.div = name_init.name_init_screen
screen3.changeTo = name_init.changeTo
#======================================#

class screen4(setup):
  def __init__(self, master):
    super().__init__(master)

    # Inisiasi pengambilan assets apartement
    self.show_apar()

    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

  def setup_game(self):
    self.player1_name = SCREEN3.player1_name
    self.player2_name = SCREEN3.player2_name

    self.player1_amount = int(SCREEN3.player_amount)
    self.player2_amount = int(SCREEN3.player_amount)

    self.props_player1 = []
    self.props_player2 = []

    # Variabel untuk memeriksa apakah tiap pemain sudah melempar dadu
    self.move_latch = False

    # Inisiasi giliran pemain
    self.giliran = False

    # Inisiasi status pemain (0: normal, 1: penjara, 2: pulau asing)
    self.player_status = [0, 0]

    # Inisiasi posisi pemain
    self.player1_loc = 1
    self.player2_loc = 1

    self.stats_update()


  def game_over(self):
    cek_uang = self.which_player_amount_read(self.which_player)
    cek_uang = int(cek_uang)

    cek_uang_invers = self.which_player_amount_read(self.which_player_invers)

    if cek_uang < 0:
      messagebox.showinfo("Game Over", f"{self.which_player_name} telah bangkrut! {self.which_player_name_invers} memenangkan permainan.")
      self.changeTo()
      self.amount_set(0)
      self.name_add('', '')
      self.giliran = False
    if cek_uang_invers < 0:
      messagebox.showinfo("Game Over", f"{self.which_player_name_invers} telah bangkrut! {self.which_player_name} memenangkan permainan.")
      self.changeTo()
      self.amount_set(0)
      self.name_add('', '')
      self.giliran = False

  def changeTo(self):
    self.hide()
    SCREEN2.show()

screen4.div                = play.play_screen
screen4.tampilan_opsi      = opsi_ui.tampilan_opsi
screen4.tampilan_inginBeli = opsi_ui.tampilan_inginBeli

screen4.cek_petak   = data_handle.cek_petak
screen4.ular_tangga = ular_tangga.ular_tangga

screen4.start_bonus = action.start_bonus
screen4.pay_tax     = action.pay_tax
screen4.pay_needs   = action.pay_needs
screen4.bansos      = action.bansos
screen4.chance_card = action.chance_card
screen4.badluck_card= action.badluck_card
screen4.travelling  = action.travelling
screen4.pulau_asing = action.pulau_asing
screen4.penjara     = action.penjara

screen4.roll_dice     = dadu.roll_dice
screen4.pos_increase  = dadu.pos_increase

screen4.ask            = move_option.ask
screen4.gonnaBuy       = move_option.gonnaBuy
screen4.nextPlayer_cta = move_option.nextPlayer_cta
screen4.pay_rent       = action.pay_rent

screen4.price_level    = buy_props.price_level
screen4.list_town_name = buy_props.list_town_name
screen4.buy1_apar      = buy_props.buy1_apar
screen4.buy2_apar      = buy_props.buy2_apar

screen4.nextPlayer = move_option.nextPlayer

screen4.which_player_props_read  = data_handle.which_player_props_read
screen4.which_player_props_add   = data_handle.which_player_props_add
screen4.which_player_amount_read = data_handle.which_player_amount_read
screen4.which_player_amount_add  = data_handle.which_player_amount_add

screen4.stats_update = status_pemain.update_data
screen4.pawn_update  = bidak.pawn_update
screen4.dadu_update  = dadu.dadu_update
screen4.list_harga   = buy_props.list_harga
screen4.dice_img     = dadu.dice_img
screen4.bg_image     = buy_props.bg_image
screen4.show_apar    = buy_props.show_apar
#===============================================================#
#============================================================================================#

# SCREEN1 = screen1(window)
# SCREEN2 = screen2(window)
SCREEN3 = screen3(window)
SCREEN4 = screen4(window)

def tutup_jendela(event= None):
    if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar dari permainan?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", tutup_jendela)

window.mainloop()