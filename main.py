from tkinter import *
from PIL import Image, ImageTk
import time

from pages import loadscreen, name_init

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

    self.canvas = Canvas(self.frame, width=1440, height=1024, highlightthickness=0)
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
    
  def changeTo(self):
    self.hide()
    SCREEN2.show()

class screen2(setup):
  def __init__(self, master):
    super().__init__(master)

  def changeTo(self, event=None):
    self.hide()
    # SCREEN3.show()

# class screen3(setup):
#   def __init__(self, master):
#     super().__init__(master)

screen1.div = loadscreen.splash1
screen2.div = loadscreen.splash2
  
SCREEN1 = screen1(window)
SCREEN2 = screen2(window)
# SCREEN3 = screen3(window)

window.mainloop()