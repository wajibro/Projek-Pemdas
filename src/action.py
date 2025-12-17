from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import random

def import_image(src, resize= None, png= None): # Fungsi untuk mengimport gambar
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if png:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def cek_petak(self):
  # Hanya jalankan aksi yang relevan untuk petak saat ini
  # Mengambil lokasi pemain aktif dan panggil fungsi yang sesuai
  loc = self.which_player_loc

  # Bonus start dice/lap
  self.start_bonus()

  if loc == 3:
    self.pay_tax()
    return True

  if loc in (19, 35):
    self.pay_needs()
    return True

  if loc in (24, 36):
    self.bansos()
    return True

  if loc == 11:
    self.travelling()
    return True
  
  if loc == 21:
    self.pulau_asing()
    return True

  if loc == 31:
    self.penjara()
    return True

  if loc in (16, 26, 38):
    self.chance_card()
    return True

  if loc == 7:
    self.badluck_card()
    return True
  
  return False

def start_bonus(self):
  if self.move_latch == True:
    if self.which_player_loc == 1:
      get_latch = False
      if get_latch == False:
        total_value = int(self.amount_read_player(self.which_player))
        total_value += 100000
        self.amount_add_player(self.which_player, int(total_value))
        messagebox.showinfo('Bonus Start', f'{self.which_player_name} mendapat bonus sebesar Rp.100.000 saat melewati start')
        get_latch = True
        self.kunci_dadu = False
        if hasattr(self, 'gonnaBuy_btn'):
          self.gonnaBuy_btn.destroy()
        if hasattr(self, 'nextPlayer_btn'):
          self.nextPlayer_btn.destroy()
        
        self.nextPlayer()

def pay_rent(self):
    town_name = self.list_town_name(self.which_player_loc)
    prop_cache = self.props_read(self.which_player)

    # Hitung harga sewa dasar
    base_rent = self.price_level()  # Tanpa parameter, atau dengan parameter yang sesuai
    
    # Versi 1: Jika price_level tidak perlu parameter lokasi
    player_amount = int(self.amount_read_player(self.which_player)) - base_rent
    player_amount_invers = int(self.amount_read_player(self.which_player_invers)) + base_rent

    # Versi 2: Jika perlu menyesuaikan dengan properti yang dimiliki
    if prop_cache.count(town_name) >= 2:
        player_amount = int(self.amount_read_player(self.which_player)) - base_rent * 2
        player_amount_invers = int(self.amount_read_player(self.which_player_invers)) + base_rent * 2

    self.amount_add_player(self.which_player, player_amount)
    self.amount_add_player(self.which_player_invers, player_amount_invers)

    # Tampilkan pesan dengan jumlah yang sesuai
    rent_amount = base_rent * 2 if prop_cache.count(town_name) >= 2 else base_rent
    messagebox.showinfo('Informasi', f'{self.which_player_name} membayar sewa ke {self.which_player_name_invers} sebesar Rp. {rent_amount}')

def pay_tax(self):
  cekProperti = self.props_read(self.which_player)
  daftar_properti = cekProperti.split(', ')

  base_value = 200000
  total_value = int(self.amount_read_player(self.which_player))
  total_tax = base_value + ((len(daftar_properti)-1) * (base_value/2))
  total_value -= total_tax
  total_value = int(total_value)

  if cekProperti != '':
    self.amount_add_player(self.which_player, int(total_value))
    messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{total_tax}\nDengan bangunan sejumlah {len(daftar_properti)-1}')
  else:
    self.amount_add_player(self.which_player, int(total_value))
    messagebox.showinfo('Pembayaran pajak', f'{self.which_player_name} membayar pajak sebesar Rp.{total_tax}\nTanpa bangunan')

  self.kunci_dadu = False
  if hasattr(self, 'gonnaBuy_btn'):
    self.gonnaBuy_btn.destroy()
  if hasattr(self, 'nextPlayer_btn'):
    self.nextPlayer_btn.destroy()
  
  self.nextPlayer()

def pay_needs(self):
  cekProperti = self.props_read(self.which_player)
  total_value = int(self.amount_read_player(self.which_player))
  daftar_properti = cekProperti.split(', ')
  total_pay  = ((len(daftar_properti)-1) * 50000)
  total_value -= total_pay
  total_value = int(total_value)

  if self.which_player_loc == 19:
    if cekProperti == '':
      messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan listrik')
    else:
      self.amount_add_player(self.which_player, int(total_value))
      messagebox.showinfo('Pembayaran listrik', f'{self.which_player_name} membayar listrik sebesar Rp.{total_pay}\nDengan bangunan sejumlah {len(daftar_properti)-1}')
    self.nextPlayer()

  if self.which_player_loc == 35:
    if cekProperti == '':
      messagebox.showinfo('Informasi', f'{self.which_player_name} anda tidak memiliki tagihan air')
    else:
      self.amount_add_player(self.which_player, int(total_value))
      messagebox.showinfo('Pembayaran air', f'{self.which_player_name} membayar air sebesar Rp.{total_pay}\nDengan bangunan sejumlah {len(daftar_properti)}')
    self.nextPlayer()

def bansos(self):
  total_value = int(self.amount_read_player(self.which_player))
  total_get = (random.randint(20, 500) * 1000)
  total_value += total_get
  total_value = int(total_value)

  self.amount_add_player(self.which_player, int(total_value))
  messagebox.showinfo('Dapat Bansos', f'Selamat {self.which_player_name}, kamu mendapat bansos sebesar {total_get}')
  self.nextPlayer()

def travelling(self):
  if self.which_player == 'player1':
    self.player1_loc = simpledialog.askinteger('Travelling Kemana Saja', 'Jika kamu bisa pergi kemana saja, mana tujuanmu?')
    if self.player1_loc == None:
      self.player1_loc = 11
  elif self.which_player == 'player2':
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
  daftar_kartu = ['memenangkan kompetisi\nSains Data dan mendapat uang sebesar Rp 1.000.000', 
                  'berpindah ke petak start\ndan mendapat sejumlah uang', 
                  'dapat uang bunga dari bank \nmendapat uang sebesar Rp 250.000',
                  'anda dapat sekarung beras dari pak zulhas\n kemudian menjualnya sebesar Rp 90.000',
                  'Hari ini adalah ulang tahun anda.\n Lawan memberikan anda Rp 200000']
  self.card_bg = import_image('assets/kartu_kesempatan.png')
  self.card_bg_item = self.canvas.create_image(0, 183, anchor='nw', image=self.card_bg)

  match roulet:
    case 0:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) + 1000000
      self.amount_add_player(self.which_player, total)
    case 1:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      if self.which_player == 'player1':
        self.player1_loc = 1
      elif self.which_player == 'player2':
        self.player2_loc = 1
      self.pawn_update()
      self.start_bonus()
    case 2:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, kamu {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) + 250000
      self.amount_add_player(self.which_player, total)
    case 3:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) + 90000
      self.amount_add_player(self.which_player, total)
    case 4:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Selamat {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) + 200000
      self.amount_add_player(self.which_player, total)

      total_invers = self.amount_read_player(self.which_player_invers)
      total_invers = int(total_invers) - 200000
      self.amount_add_player(self.which_player_invers, total_invers)
      
  messagebox.showinfo('Kartu Kesempatan', f'{self.which_player_name}, kamu mendapat kartu kesempatan!')
  self.nextPlayer()
  
def badluck_card(self):
  roulet = random.randint(0, 4)
  if hasattr(self, 'card_bg_item'):
    self.canvas.delete(self.card_bg_item)
    self.canvas.delete(self.card_text)
  daftar_kartu = ['Anda terkena penyakit dan harus\n membayar biaya rumah sakit sebesar Rp 150000',
                'Anda diharuskan membayar biaya\n sekolah anak sebesar Rp 300000',
                'Anda diharuskan membayar biaya\n pajak tahunan sebesar 250000',
                'Anda menghancurkan properti tetangga,\n Bayar ganti rugi Rp 100000',
                'Anda terkena tilang oleh pakpol \ndan harus kasih dia gocap (Rp 50.000)']
  self.card_bg = import_image('assets/kejadian_sial.png')
  self.card_bg_item = self.canvas.create_image(0, 183, anchor='nw', image=self.card_bg)
  match roulet:
    case 0:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) - 150000
      self.amount_add_player(self.which_player, total)
    case 1:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) - 300000
      self.amount_add_player(self.which_player, total)
    case 2:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'{self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) - 250000
      self.amount_add_player(self.which_player, total)
    case 3:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Hai {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) - 50000
      self.amount_add_player(self.which_player, total)
    case 4:
      self.card_text = self.canvas.create_text(0, 250, anchor='nw', text=f'Hai {self.which_player_name}, {daftar_kartu[roulet]}', fill='white', font=('Arial', 12, 'bold'))
      total = self.amount_read_player(self.which_player)
      total = int(total) - 100000
      self.amount_add_player(self.which_player, total)

  messagebox.showinfo('Kartu Kesialan', f'{self.which_player_name}, kamu mengalami kejadian sial!')
  self.nextPlayer()