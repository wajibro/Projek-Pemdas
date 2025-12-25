from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import random

list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def start_bonus(self):
  if self.move_latch == True:
    get_latch = False
    if get_latch == False:
      bonus_amount = 100000
      total_value = self.which_player_amount_read(self.which_player)
      total_value += bonus_amount
      self.which_player_amount_add(self.which_player, total_value)
      messagebox.showinfo('Bonus Start', f'{self.which_player_name} mendapat bonus sebesar Rp.{bonus_amount:,.0f}'.replace(',', '.'))
      get_latch = True
      if hasattr(self, 'gonnaBuy_btn'):
        self.gonnaBuy_btn.destroy()
      if hasattr(self, 'nextPlayer_btn'):
        self.nextPlayer_btn.destroy()
      if self.which_player_loc == 1:
        self.nextPlayer()

def pay_rent(self):
  prop_cache = self.which_player_props_read(self.which_player)

  # Hitung harga sewa dasar
  base_rent = self.price_level()  # Tanpa parameter, atau dengan parameter yang sesuai
  base_rent -= base_rent/2
  rent_amount = base_rent * 2 if prop_cache.count(self.which_player_loc) >= 2 else base_rent

  player_amount              = self.which_player_amount_read(self.which_player) - rent_amount
  player_amount_invers       = self.which_player_amount_read(self.which_player_invers) + rent_amount
  self.which_player_amount_add(self.which_player, player_amount)
  self.which_player_amount_add(self.which_player_invers, player_amount_invers)

  # Tampilkan pesan dengan jumlah yang sesuai
  messagebox.showinfo('Informasi', f'{self.which_player_name} membayar sewa ke {self.which_player_name_invers} sebesar Rp. {f"{rent_amount:,}".replace(",", ".")}')

def pay_tax(self):
  cek_properti    = self.which_player_props_read(self.which_player)
  jumlah_properti = len(cek_properti)

  base_value = 200000
  total_tax = base_value + (jumlah_properti * (base_value/2))
  total_value  = self.which_player_amount_read(self.which_player)
  total_value -= total_tax
  total_value  = total_value

  self.which_player_amount_add(self.which_player, total_value)

  match jumlah_properti:
    case x if x > 0:
      messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{f"{int(total_tax):,}".replace(",", ".")}\nDengan bangunan sejumlah {jumlah_properti}')
    case _:
      messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{f"{int(total_tax):,}".replace(",", ".")}\nTanpa bangunan')

  self.nextPlayer()

def pay_needs(self):
  cek_properti    = self.which_player_props_read(self.which_player)
  jumlah_properti = len(cek_properti)

  total_pay  = (jumlah_properti * 50000)
  total_value  = self.which_player_amount_read(self.which_player)
  total_value -= total_pay
  total_value  = int(total_value)

  match self.which_player_loc:
    case 19:
      match jumlah_properti:
        case x if x > 0:
          self.which_player_amount_add(self.which_player, total_value)
          messagebox.showinfo('Pembayaran listrik', f'{self.which_player_name} membayar listrik sebesar Rp.{f"{int(total_pay):,}".replace(",", ".")}\nDengan bangunan sejumlah {jumlah_properti}')
        case _:
          messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan listrik')
    case 35:
      match jumlah_properti:
        case x if x > 0:
          self.which_player_amount_add(self.which_player, total_value)
          messagebox.showinfo('Pembayaran air', f'{self.which_player_name} membayar air sebesar Rp.{f"{int(total_pay):,}".replace(",", ".")}\nDengan bangunan sejumlah {jumlah_properti}')
        case _:
          messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan air')
  self.nextPlayer()

def bansos(self):
  total_get = (random.randint(20, 500) * 1000)
  total_value = self.which_player_amount_read(self.which_player)
  total_value += total_get
  total_value = int(total_value)

  self.which_player_amount_add(self.which_player, total_value)
  messagebox.showinfo('Dapat Bansos', f'Selamat {self.which_player_name}, kamu mendapat bansos sebesar Rp. {f"{total_get:,}".replace(",", ".")}')
  self.nextPlayer()

def travelling(self):
  match self.which_player:
    case 'player1':
      self.player1_loc = simpledialog.askinteger('Travelling Kemana Saja', 'Jika kamu bisa pergi kemana saja, mana tujuanmu?')
      if self.player1_loc == None:
        self.player1_loc = 11
    case 'player2':
      self.player2_loc = simpledialog.askinteger('Travelling Kemana Saja', 'Jika kamu bisa pergi kemana saja, mana tujuanmu?')
      if self.player2_loc == None:
        self.player2_loc = 11
  self.nextPlayer()

def pulau_asing(self):
  messagebox.showinfo('Pulau Asing', f'Yah..., {self.which_player_name} terdampar di pulau asing.\nPada giliran selanjutnya anda harus mendapat dadu 6 untuk bisa melanjutkan perjalanan')
  self.player_status[int(self.giliran)] = 2
  self.nextPlayer()

def penjara(self):
  messagebox.showinfo('Penjara', f'Waduh, {self.which_player_name} masuk penjara, skip 1 putaran')
  self.player_status[int(self.giliran)] = 1
  self.nextPlayer()

def chance_card(self):
  roulet = random.randint(0, 4)
  if hasattr(self, 'card_bg_item'):
    self.canvas.delete(self.card_bg_item)
    self.canvas.delete(self.card_text)
  daftar_kartu = [f'memenangkan kompetisi\nSains Data dan mendapat uang sebesar Rp {f"{1000000:,}".replace(",", ".")}', 
                  'berpindah ke petak start\ndan mendapat sejumlah uang', 
                  f'dapat uang bunga dari bank \nmendapat uang sebesar Rp {f"{250000:,}".replace(",", ".")}',
                  f'anda dapat sekarung beras dari\nPak Zulhas kemudian menjualnya sebesar Rp {f"{90000:,}".replace(",", ".")}',
                  f'Hari ini adalah ulang tahun anda.\n Lawan memberikan anda Rp {f"{200000:,}".replace(",", ".")}']
  self.card_bg = import_image('assets/kartu_kesempatan.png')
  self.card_bg_item = self.canvas.create_image(0, 183, anchor='nw', image=self.card_bg)

  match roulet:
    case 0:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total += 1000000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 1:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      match self.which_player:
        case 'player1':
          self.player1_loc = 1
        case 'player2':
          self.player2_loc = 2
      self.pawn_update()
      self.start_bonus()
    case 2:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total += 250000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 3:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total += 90000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 4:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total += 200000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)

      total_invers = self.which_player_amount_read(self.which_player_invers)
      total_invers -= 200000
      total_invers = int(total_invers)
      self.which_player_amount_add(self.which_player_invers, total_invers)
      
  messagebox.showinfo('Kartu Kesempatan', f'{self.which_player_name}, kamu mendapat kartu kesempatan!')
  self.nextPlayer()
  
def badluck_card(self):
  roulet = random.randint(0, 4)
  if hasattr(self, 'card_bg_item'):
    self.canvas.delete(self.card_bg_item)
    self.canvas.delete(self.card_text)
  daftar_kartu = [f'Anda terkena penyakit dan harus\n membayar biaya rumah sakit sebesar Rp {f"{150000:,}".replace(",", ".")}',
                f'Anda diharuskan membayar biaya\n sekolah anak sebesar Rp {f"{300000:,}".replace(",", ".")}',
                f'Anda diharuskan membayar biaya\n pajak tahunan sebesar {f"{250000:,}".replace(",", ".")}',
                f'Anda menghancurkan properti tetangga,\n Bayar ganti rugi Rp {f"{50000:,}".replace(",", ".")}',
                f'Anda terkena tilang oleh pakpol \ndan harus kasih dia gocap (Rp {f"{100000:,}".replace(",", ".")})']
  self.card_bg = import_image('assets/kejadian_sial.png')
  self.card_bg_item = self.canvas.create_image(0, 183, anchor='nw', image=self.card_bg)

  match roulet:
    case 0:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total -= 150000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 1:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total -= 300000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 2:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total -= 250000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 3:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Hai {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total -= 50000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)
    case 4:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Hai {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.which_player_amount_read(self.which_player)
      total -= 100000
      total = int(total)
      self.which_player_amount_add(self.which_player, total)

  messagebox.showinfo('Kartu Kesialan', f'{self.which_player_name}, kamu mengalami kejadian sial!')
  self.nextPlayer()