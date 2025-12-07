from tkinter import *
from PIL import Image, ImageTk
import time
import random

window = Tk()
window.title('Monopoly')
window.iconbitmap('assets/icon.ico')
window.geometry('1280x720')

global player_1_loc
player_1_loc = 1

# def roll_dice():
#   player_1_loc += random.randint(1, 10)

kordinat = [[0,0]]
for i in range(0, 9): # Garis Bawah Peta
   kordinat.append([1303-(76*i), 813])

for i in range(1, 9): # Garis Kiri Peta
   kordinat.append([1303-(76*8), 813-(76*i)])

for i in range(1, 9): # Garis Atas Peta
   kordinat.append([(1303-(76*8))+(76*i), 813-(76*8)])

for i in range(1, 8): # Garis Kanan Peta
   kordinat.append([1303, 813-(76*8)+(76*i)])

kordinat_x = [x[0] for x in kordinat]
kordinat_y = [x[1] for x in kordinat]

def import_image(src, size=None, rgba=False):
    x = Image.open(src)
    
    if rgba:
        x = x.convert('RGBA')
    
    if size:
        x = x.resize(size)
    
    return ImageTk.PhotoImage(x)

class setup:
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)

    self.canvas = Canvas(self.frame, width=1440, height=1024, highlightthickness=0)
    self.canvas.pack(fill= 'both', expand= True)

    self.div()

  def hide(self):
    self.frame.pack_forget()

  def show(self):
    self.frame.pack(fill = 'both', expand = True)

class screen(setup):
  def __init__(self, master):
    super().__init__(master)
    self.show()
  
  def div(self):
    self.bg = import_image('assets/background-start.png')
    self.canvas.create_image(0, 0, anchor='nw', image= self.bg)

    self.btn = Button(self.frame, text= 'Roll Dice', command= self.roll_dice)
    self.btn.place(x=0, y=0)

    self.map = import_image('assets/peta.png', size=(840,840), rgba= True)
    self.canvas.create_image(588, 101, anchor= 'nw', image= self.map)

    self.player_1_pawn = import_image('assets/player_1.png', size= (22,34), rgba= True)
    self.player_1_pawnItem = self.canvas.create_image(kordinat_x[player_1_loc], kordinat_y[player_1_loc], anchor= 'nw',  image= self.player_1_pawn)

  def roll_dice(self):
     global player_1_loc
     
     x = random.randint(1, 6)
     player_1_loc = player_1_loc + x
     if player_1_loc > len(kordinat):
        player_1_loc = 1
     self.update_pawn()

  def update_pawn(self):
    self.canvas.delete(self.player_1_pawnItem)
    self.player_1_pawnItem = self.canvas.create_image(kordinat_x[player_1_loc], kordinat_y[player_1_loc], anchor= 'nw',  image= self.player_1_pawn)

x = screen(window)

window.mainloop()