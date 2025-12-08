from tkinter import *

def ask(self):
  self.gonnaBuy_btn = Button(self.frame, text= 'Beli Properti', command= self.gonnaBuy, font=('Poppins', 18))
  self.nextPlayer_btn = Button(self.frame, text= 'Lanjut', command= self.nextPlayer, font=('Poppins', 18))

  self.gonnaBuy_btn.place(x= 41, y= 499)
  self.nextPlayer_btn.place(x= 221, y= 499)

def gonnaBuy(self):
  self.thisTownPrice = 100000
  self.gonnaBuy_btn.destroy()
  self.nextPlayer_btn.destroy()

  self.buy1_btn = Button(self.frame, text= 'Bangun 1 Apartement', command= self.buy1_apar, font=('Poppins', 12))
  self.buy2_btn = Button(self.frame, text= 'Bangun 2 Apartement', command= self.buy2_apar, font=('Poppins', 12))

  self.buy1_price = Label(self.frame, text= f'-{self.thisTownPrice}', fg= 'red', bg= 'white', font= ('Poppins', 16))
  self.buy2_price = Label(self.frame, text= f'-{int(self.thisTownPrice + (self.thisTownPrice * 1/2))}', fg= 'red', bg= 'white', font= ('Poppins', 16))

  self.buy1_btn.place(x= 53, y= 480)
  self.buy2_btn.place(x= 225, y= 480)

  self.buy1_price.place(x= 68, y= 511)
  self.buy2_price.place(x= 230, y= 511)

def nextPlayer(self):
  self.gonnaBuy_btn.destroy()
  self.nextPlayer_btn.destroy()
  
  self.giliran = not self.giliran
  self.kunci_dadu = False
  self.stats_update()