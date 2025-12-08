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

def import_image(src, size=None, png=False):
    x = Image.open(src)
    
    if png:
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
    
  def dice_img(self, x):
    return import_image(f'assets/dadu_{x}.png', png= 1)
  
  
  
  def div(self):
    self.canvas.create_image(0, 0, anchor='nw', image=self.dice_img(1))
    
    self.cihuy = import_image('assets/dadu_1.png', png= 1)
    self.canvas.create_image(0, 0, anchor='nw', image=self.cihuy)

x = screen(window)

window.mainloop()