from tkinter import *
from PIL import Image, ImageTk
import time
import random

from pages import loadscreen, name_init, play # Memasukkan file halaman
from src import kordinat

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

 #======================================#
window = Tk()
window.title('Monopoly')
window.iconbitmap('assets/icon.ico') # Customize icon pojok window
window.geometry('1280x720') # Mengatur resolusi window
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

  def name_add(self, name1, name2): # Menambahkan nama pemain ke file teks
    try:
        with open('src/player1_name.txt', 'w') as file:
            file.write(str(name1))
        with open('src/player2_name.txt', 'w') as file:
            file.write(str(name2))
    except:
        print("Fungsi name_add error")

  def name_read_player(self, x): # Membaca nama pemain dari file teks
    if x == 'player1':
        with open('src/player1_name.txt', 'r') as file:
          p1_name = file.read()
        return p1_name
    elif x == 'player2':
        with open('src/player2_name.txt', 'r') as file:
          p2_name = file.read()
        return p2_name

  def amount_read_player(self, x): # Membaca jumlah uang pemain dari file teks
    if x == 'player1':
        with open('src/player1_amount.txt', 'r') as file:
          p1 = file.read()
        return p1
    elif x == 'player2':
        with open('src/player2_amount.txt', 'r') as file:
          p2 = file.read()
        return p2

class screen1(setup): # Halaman splash screen awal
  def __init__(self, master):
    super().__init__(master)
    self.show() # Tampilkan halaman saat program dijalankan
    self.master.after(3000, self.changeTo) # Tunggu 3 detik kemudian jalankan self.changeTo

  def changeTo(self): # Menyembunyikan halaman saat ini kemudian tampilkan halaman SCREEN2
    self.hide()
    SCREEN2.show()

class screen2(setup): # Halaman awal
  def __init__(self, master):
    super().__init__(master)
    self.master.after(3000, self.showof)

    window.bind('<Return>', self.changeTo) # Tekan 'Enter' kemudian jalankan self.changeTo

  def changeTo(self, event=None): # Menyembunyikan halaman saat ini kemudian tampilkan halaman SCREEN3
    self.hide()
    SCREEN3.show()

class screen3(setup): # Halaman inisialisasi nama pemain
  def __init__(self, master):
    super().__init__(master)

  def amount_set(self, x): # Mengatur ulang jumlah uang pemain ke file teks (awal permainan)
    try:
        with open('src/player1_amount.txt', 'w') as file:
            file.write(x)
        with open('src/player2_amount.txt', 'w') as file:
            file.write(x)
    except:
        print("Fungsi amount_set error")

  def changeTo(self):
    self.name_add(self.player1_name.get(), self.player2_name.get())
    self.amount_set(str(self.modal_amount.get()))

    self.cekNama1 = self.name_read_player('player1')
    self.cekNama2 = self.name_read_player('player2')
    if self.cekNama1 == '' or self.cekNama2 == '':
      print("Nama pemain tidak boleh kosong!")
    else:
      self.hide()
      SCREEN4.show()
      SCREEN4.stats_update()

class screen4(setup): # Halaman permainan utama
  def __init__(self, master):
    super().__init__(master)
    self.giliran = True

    self.kordinat = kordinat.kordinat_peta()
    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    self.player1_loc = 1
    self.player2_loc = 1

  def pawn_update(self):
    if self.player1_loc >= len(self.kordinat)-1:
      self.player1_loc = 1
    if self.player2_loc >= len(self.kordinat)-1:
      self.player2_loc = 1

    self.canvas.delete(self.player1_pawnItem)
    self.canvas.delete(self.player2_pawnItem)
    self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc]+2, self.kordinat_y[self.player1_loc]+2, anchor= 'nw',  image= self.player1_pawn)
    self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc]-2, self.kordinat_y[self.player2_loc]-2, anchor= 'nw',  image= self.player2_pawn)

  def stats_update(self):
    self.player1_name = self.name_read_player('player1')
    self.player2_name = self.name_read_player('player2')
    self.player1_amount = self.amount_read_player('player1')
    self.player2_amount = self.amount_read_player('player2')
    
    self.player1_name_label = Label(self.frame, text=f'Player 1 - {self.player1_name}', font=('Poppins', 24), bg='white')
    self.player1_amount_label = Label(self.frame, text=f'Rp. {self.player1_amount}', font=('Poppins', 24))

    self.player2_name_label = Label(self.frame, text=f'Player 2 - {self.player2_name}', font=('Poppins', 24), bg='white')
    self.player2_amount_label = Label(self.frame, text=f'Rp. {self.player2_amount}', font=('Poppins', 24))

    self.player1_name_label.place(x=9, y=7)
    self.player1_amount_label.place(x=9, y=40)
    self.player2_name_label.place(x=9, y=84)
    self.player2_amount_label.place(x=9, y=120)

  def roll_1(self, event=None):
    self.dadu_num = random.randint(1, 6)
    if self.giliran == True:
      self.player1_loc += self.dadu_num
    elif self.giliran == False:
      self.player2_loc += self.dadu_num

    self.pawn_update()
    self.giliran = not self.giliran

screen1.div = loadscreen.splash1

screen2.div = loadscreen.splash2
screen2.showof = loadscreen.showof

screen3.div = name_init.name_init_screen

screen4.div = play.play_screen
  
SCREEN1 = screen1(window)
SCREEN2 = screen2(window)
SCREEN3 = screen3(window)
SCREEN4 = screen4(window)

window.mainloop()