from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

#========================== desain halaman inisialisasi nama pemain #==========================#
def name_init_screen(self):
  #==============================# Inisialisasi Variabel #==============================#
  self.player1_name= StringVar()
  self.player2_name= StringVar()
  self.modal_amount= StringVar()
  #==============================# End Inisialisasi Variabel #==============================#

  self.canvas.configure(bg='#9BB3CD') # Warna latar belakang halaman

  #==============================# Src Gambar #===============================#
  self.bg= import_image('assets/background.png')
  self.title = import_image('assets/title.png', png= 1)
  self.player1_bg = import_image('assets/player1_entry.png', png= 1)
  self.player2_bg = import_image('assets/player2_entry.png', png= 1)
  self.modal_bg = import_image('assets/modal_entry.png', png= 1)
  self.btn_bg = import_image('assets/btn_start.png', png= 1)
  #==============================# End Src Gambar #===============================#

  #==============================# Inisiasi Entry & Button #===============================#
  self.player1_entry = Entry(self.frame, width= 20, font=('Arial', 20), textvariable=self.player1_name, bg='#C3D827')
  self.player2_entry = Entry(self.frame, width= 20, font=('Arial', 20), textvariable=self.player2_name, bg='#C3D827')
  self.modal_amount= Entry(self.frame, width= 18, font=('Arial', 20), textvariable=self.modal_amount, bg='#C3D827')
  self.btn_start= Button(self.frame, image= self.btn_bg, command= self.changeTo, bg='#9BB3CD', bd=0, highlightthickness= 0 )
  #==============================# End Inisiasi Entry & Button #===============================#
  
  #==============================# Menempatkan Gambar, Entry, & Button #===============================#
  self.canvas.create_image(0, 0, anchor='nw', image=self.bg)
  self.canvas.create_image(442.05, 96, anchor='nw', image=self.title)
  self.canvas.create_image(364, 259, anchor= 'nw', image= self.player1_bg)
  self.canvas.create_image(364, 352, anchor= 'nw', image= self.player2_bg)
  self.canvas.create_image(364, 472, anchor= 'nw', image= self.modal_bg)
  self.player1_entry.place(x= 539, y= 270)
  self.player2_entry.place(x= 539, y= 360)
  self.modal_amount.place(x= 609, y= 482)
  self.canvas.create_window(410, 570, anchor= 'nw', window= self.btn_start)
  #===============================# End Menempatkan Gambar, Entry, & Button #===============================#
#========================== End desain halaman inisialisasi nama pemain ==========================#


def amount_set(self, x): # Mengatur ulang jumlah uang pemain ke file teks (awal permainan)
    try:
        with open('src/data_pemain/player1_amount.txt', 'w') as file:
            file.write(x)
        with open('src/data_pemain/player2_amount.txt', 'w') as file:
            file.write(x)
    except:
        print("Fungsi amount_set error")

def changeTo(self):
  self.name_add(self.player1_name.get(), self.player2_name.get())
  self.amount_set(str(self.modal_amount.get()))

  self.cekNama1 = self.name_read_player('player1')
  self.cekNama2 = self.name_read_player('player2')
  if self.cekNama1 == '' or self.cekNama2 == '':
    messagebox.showerror("Nama pemain tidak boleh kosong!")
  else:
    self.hide()
    self.screen4()