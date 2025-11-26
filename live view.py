# Ini adalah file test
from tkinter import *
from PIL import Image, ImageTk
import time

from src import name_init

window = Tk()
window.title('Monopoly')
window.iconbitmap('assets/icon.ico')
window.geometry('1440x1024')

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

screen.div = name_init.name_init_screen # Ganti sesuai nama program desain nama_folder.nama_method

x = screen(window)
window.mainloop()