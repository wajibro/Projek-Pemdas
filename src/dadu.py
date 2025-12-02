from tkinter import *
from PIL import Image, ImageTk
import random

def import_image(src, resize= None, rgba= None):
  x = Image.open(src)

  if resize:
    x.resize(resize)
  if rgba:
    x.convert('RGBA')

  return ImageTk.PhotoImage(x)

def roll_1():
    return 

def dadu_img():
  dadu = []
  for i in range(1,7):
    dadu.append([import_image(f'assets/dadu_{i}.png', resize= (135, 135), rgba= True)])

  return dadu