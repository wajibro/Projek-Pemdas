import tkinter as tk

def toggle_fullscreen(event=None):
    # Toggle antara fullscreen dan windowed
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))
    return "break"

def exit_fullscreen(event=None):
    # Keluar dari fullscreen
    root.attributes('-fullscreen', False)
    return "break"

# Buat window utama
root = tk.Tk()
root.title("Aplikasi Fullscreen")
root.geometry("800x600")

# Tombol untuk toggle fullscreen
btn_toggle = tk.Button(root, text="Toggle Fullscreen (F11)", command=toggle_fullscreen)
btn_toggle.pack(pady=20)

# Tombol keluar
btn_exit = tk.Button(root, text="Keluar (ESC)", command=root.quit)
btn_exit.pack(pady=10)

# Binding keyboard
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', exit_fullscreen)

root.mainloop()