from tkinter import *
from PIL import Image, ImageTk
import time
import random

from pages import loadscreen, name_init, play
from src import kordinat, dadu

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

window = Tk()
window.title('Monopoly')
window.iconbitmap('assets/icon.ico')
window.geometry('1280x720')
# window.attributes('-fullscreen', not window.attributes('-fullscreen'))

# def toggle_fullscreen(event=None):
#     window.attributes('-fullscreen', not window.attributes('-fullscreen'))
#     return "break"

# def exit_fullscreen(event=None):
#     window.attributes('-fullscreen', False)
#     return "break"

# window.bind('<F11>', toggle_fullscreen)
# window.bind('<Escape>', exit_fullscreen)

class setup:
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)

    self.canvas = Canvas(self.frame, width=1280, height=720, highlightthickness=0)
    self.canvas.pack(fill= 'both', expand= True)

    self.div()

  def hide(self):
    self.frame.pack_forget()

  def show(self):
    self.frame.pack(fill = 'both', expand = True)

class screen1(setup):
  def __init__(self, master):
    super().__init__(master)
    self.show()
    self.master.after(3000, self.changeTo)

    try:
      with open('src/player1_name.txt', 'w') as file:
        file.write('')

      with open('src/player2_name.txt', 'w') as file:
        file.write('')

      with open('src/player1_amount.txt', 'w') as file:
        file.write('')

      with open('src/player2_amount.txt', 'w') as file:
        file.write('')
    except:
      print("variable tidak tersimpan")
    
  def changeTo(self):
    self.hide()
    SCREEN2.show()

class screen2(setup):
  def __init__(self, master):
    super().__init__(master)
    self.master.after(3000, self.showof)

    window.bind('<Return>', self.changeTo)

  def changeTo(self, event=None):
    self.hide()
    SCREEN3.show()

class screen3(setup):
  def __init__(self, master):
    super().__init__(master)

    self.player1_name
    self.player2_name
    self.modal_amount

  def var_init(self, event=None):
    try:
      with open('src/player1_name.txt', 'w') as file:
        file.write(self.player1_name.get())

      with open('src/player2_name.txt', 'w') as file:
        file.write(self.player2_name.get())

      with open('src/player1_amount.txt', 'w') as file:
        file.write(self.modal_amount.get())

      with open('src/player2_amount.txt', 'w') as file:
        file.write(self.modal_amount.get())
    except:
      print("variable tidak tersimpan")

    self.hide()
    SCREEN4.show()

class screen4(setup):
  def __init__(self, master):
    super().__init__(master)
    self.giliran = True

    self.kordinat = kordinat.kordinat_peta()
    self.kordinat_x = kordinat.kordinat_x()
    self.kordinat_y = kordinat.kordinat_y()

    self.player1_loc = 1
    self.player2_loc = 1

    with open('src/player1_name.txt', 'r') as file:
      self.player1_name_raw = file.read()
    with open('src/player1_amount.txt', 'r') as file:
      self.player1_amount_raw = file.read()

    with open('src/player2_name.txt', 'r') as file:
      self.player2_name_raw = file.read()
    with open('src/player2_amount.txt', 'r') as file:
      self.player2_amount_raw = file.read()

    self.money_update()
    
  def pawn_update(self):
    if self.player1_loc >= len(self.kordinat)-1:
      self.player1_loc = 1
    if self.player2_loc >= len(self.kordinat)-1:
      self.player2_loc = 1

    self.canvas.delete(self.player1_pawnItem)
    self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc]+2, self.kordinat_y[self.player1_loc]+2, anchor= 'nw',  image= self.player1_pawn)
    self.canvas.delete(self.player2_pawnItem)
    self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc]-2, self.kordinat_y[self.player2_loc]-2, anchor= 'nw',  image= self.player2_pawn)

  def money_update(self):
    self.player1_name = Label(self.frame, text=f'Player 1 - {self.player1_name_raw}', font=('Poppins', 24), bg='white')
    self.player1_amount = Label(self.frame, text=f'Rp. {self.player1_amount_raw}', font=('Poppins', 24))
    self.player1_name.place(x=9, y=7)
    self.player1_amount.place(x=9, y=40)
    
    self.player2_name = Label(self.frame, text=f'Player 2 - {self.player2_name_raw}', font=('Poppins', 24), bg='white')
    self.player2_amount = Label(self.frame, text=f'Rp. {self.player2_amount_raw}', font=('Poppins', 24))
    self.player2_name.place(x=9, y=84)
    self.player2_amount.place(x=9, y=120)


  def roll_1(self, event=None):
    self.dadu_num = random.randint(1, 6)
    if self.giliran == True:
      self.player1_loc += self.dadu_num
    elif self.giliran == False:
      self.player2_loc += self.dadu_num

    self.pawn_update()
    self.giliran = not self.giliran

  def roll_2(self, event=None):
    self.dadu1 = dadu.roll_1()
    self.dadu2 = dadu.roll_1()

    if self.giliran == True:
      self.player1_loc += self.dadu1 + self.dadu2
    elif self.giliran == False:
      self.player2_loc += self.dadu1 + self.dadu2

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