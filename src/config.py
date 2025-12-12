from tkinter import *

def win_config():
  window = Tk()
  window.title('Monopoly')
  img = PhotoImage(file='icon.png')
  window.tk.call('wm', 'iconphoto', window._w, img) # Customize icon pojok window
  window.geometry('1280x720') # Mengatur resolusi window
  return window