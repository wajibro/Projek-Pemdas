from tkinter import *

def tampilan_opsi(self):
    self.gonnaBuy_btn = Button(self.frame, text= 'Beli Properti', command= self.gonnaBuy, font=('Poppins', 12))
    self.nextPlayer_btn = Button(self.frame, text= 'Lanjut', command= self.nextPlayer, font=('Poppins', 12))

    self.gonnaBuy_item = self.canvas.create_window(81, 509, window= self.gonnaBuy_btn)
    self.nextPlayer_item = self.canvas.create_window(261, 509, window= self.nextPlayer_btn)

def tampilan_inginBeli(self):
    harga = self.price_level()

    self.canvas.delete(self.gonnaBuy_item)
    self.canvas.delete(self.nextPlayer_item)

    self.buy1_btn = Button(self.frame, text= 'Bangun 1 Apartement', command= self.buy1_apar, font=('Poppins', 8))
    self.buy2_btn = Button(self.frame, text= 'Bangun 2 Apartement', command= self.buy2_apar, font=('Poppins', 8))

    self.buy1_price = Label(self.frame, text= f'-Rp {f"{int(harga):,}".replace(",", ".")}', fg= 'red', bg= 'white', font= ('Poppins', 10))
    self.buy2_price = Label(self.frame, text= f'-Rp {f"{int(harga*2):,}".replace(",", ".")}', fg= 'red', bg= 'white', font= ('Poppins', 10))

    self.canvas.create_window(93, 490, window= self.buy1_btn)
    self.canvas.create_window(265, 490, window= self.buy2_btn)

    self.canvas.create_window(108, 526, window= self.buy1_price)
    self.canvas.create_window(270, 526, window= self.buy2_price)