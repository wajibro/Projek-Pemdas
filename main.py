from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import time
import random
import ctypes
import os

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

def load_font(font_path):
    if os.path.exists(font_path):
        FR_PRIVATE = 0x10
        return ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
    return 0

# Load the custom font
font_path = os.path.join(os.path.dirname(__file__), 'assets', 'Poppins-Regular.ttf')
fonts_loaded = load_font(font_path)
if fonts_loaded == 0:
    print(f"Warning: Could not load font at {font_path}")


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
    # Tampilkan halaman saat program dijalankan
    self.show()
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
#=====================================
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
    
    # Variabel untuk memeriksa apakah tiap pemain sudah melempar dadu
    self.move_latch = False
    # Inisiasi pengambilan assets apartement
    self.show_apar()

    # Inisiasi giliran pemain
    self.giliran = False

    # Inisiasi sistem kunci dadu
    self.kunci_dadu = False

    # Inisiasi status pemain (0: normal, 1: penjara, 2: pulau asing)
    self.player_status = [0, 0]

    # Inisiasi posisi pemain
    self.player1_loc = 1
    self.player2_loc = 1

    # Mengkosongkan data properti pemain
    self.props_add('player1', '')
    self.props_add('player2', '')

    # Refresh tampilan data pemain
    self.stats_update()
    self.list_harga()

    # Pengelompokan kordinat ke dalam x dan y
    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    # Inisiasi tampilan dadu
    self.list_dadu = import_image('assets/dadu_0.png', png=1)
    self.dadu_img_item = self.canvas.create_image(252, 637, anchor='nw', image=self.list_dadu)

  def game_over(self, event= None):
    messagebox.showinfo("Game Over", f"{self.which_player_name} telah bangkrut! {self.which_player_name_invers} memenangkan permainan.")
    self.amount_set(None)
    self.name_add('', '')
    self.hide()
    SCREEN2.show()
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
# Inisiasi Pengambilan asset apartement
screen4.show_apar = buy_props.show_apar
#=====================================#

# Fungsi mengembalikan nama kota
screen4.list_town_name = buy_props.list_town_name

#======== Fungsi Pembelian Properti =======#
# Menambahkan data pembelian properti
screen4.props_add = buy_props.props_add
# Periksa data pembelian yang sudah tersimpan
screen4.props_read = buy_props.props_read
# Sistem beli properti pemain
screen4.buy1_apar = buy_props.buy1_apar
screen4.buy2_apar = buy_props.buy2_apar
# Fungsi pemain lawan bayar sewa saat melewati kota yang memiliki properti
screen4.pay_rent = action.pay_rent

screen4.price_level = buy_props.price_level
#==========================================#

#======== Fungsi Untuk Memeriksa Setiap Petak yang Dilewati =======#
# Semua fungsi dihubungkan kesini
screen4.cek_petak = action.cek_petak

# Dapat bonus saat melewati petak start
screen4.start_bonus = action.start_bonus
# Saat berhenti pada petak ini bayar pajak sesuai jumlah bangunan
screen4.pay_tax = action.pay_tax
# Saat berhenti pada petak ini bayar air atau listrik sejumlah bangunan yang dimiliki
screen4.pay_needs = action.pay_needs
# Saat berhenti pada petak ini dapat uang dengan nominal Rp20.000 - Rp50.000
screen4.bansos = action.bansos
# Saat berhenti pada petak ini pilih mendarat di petak nomor mana pun
screen4.travelling = action.travelling
# Saat berhenti pada petak ini mendapat kartu kesempatan yang beragam
screen4.chance_card = action.chance_card
# Saat berhenti pada petak ini mendapat kejadian sial yang beragam
screen4.badluck_card = action.badluck_card
# Saat berhenti pada petak ini tidak bisa bergerak kemanapun, lempar dadu 6 untuk bergerak atau uang berkurang Rp100.000
screen4.pulau_asing = action.pulau_asing
# Saat berhenti pada petak ini tidak bisa bergerak pada giliran selanjutnya sekali
screen4.penjara = action.penjara
#=================================================================#

#===============================================================#
#============================================================================================#

SCREEN1 = screen1(window)
SCREEN2 = screen2(window)
SCREEN3 = screen3(window)
SCREEN4 = screen4(window)

def tutup_jendela(event= None):
    if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar dari permainan?"):
        SCREEN3.amount_set(None)
        SCREEN3.name_add('', '')
        SCREEN4.props_add('player1', '')
        SCREEN4.props_add('player2', '')
        window.destroy()

window.protocol("WM_DELETE_WINDOW", tutup_jendela)

window.mainloop()