from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('test gambar')
window.geometry('1440x1024')

# Gunakan Canvas untuk transparansi yang proper
canvas = Canvas(window, width=1440, height=1024, highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Background
bg_image = Image.open('assets/background-start.png')
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor='nw', image=bg_photo)

# Logo dengan transparansi - PASTIKAN file PNG sudah benar-benar transparan
logo_image = Image.open('assets/logo-M.png').convert('RGBA')
logo_photo = ImageTk.PhotoImage(logo_image)
canvas.create_image(100, 100, anchor='nw', image=logo_photo)  # Posisi bisa disesuaikan

window.mainloop()