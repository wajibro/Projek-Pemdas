from PIL import Image, ImageTk

def import_image(src):
  x = Image.open(src)
  return ImageTk.PhotoImage(x)

def import_imageRGBA(src):
  x = Image.open(src).convert('RGBA')
  return ImageTk.PhotoImage(x)
