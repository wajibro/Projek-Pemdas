from tkinter import messagebox
import time

def ular_tangga(self):
    current_name = self.player2_name if self.giliran else self.player1_name
    match self.which_player_loc:
      case 4: # Tangga 1
        if self.giliran:
            self.player2_loc = 38
            self.cek_petak()
        else:
            self.player1_loc = 38
            self.cek_petak()
        self.pawn_update()
        time.sleep(1)
        messagebox.showinfo(f'{current_name} - Telah Berubah Posisi', f'{current_name}, Anda tidak sengaja menemukan tangga')
      case 18: # Tangga 2
        if self.giliran:
            self.player2_loc = 24
            self.cek_petak()
        else:
            self.player1_loc = 24
            self.cek_petak()
        time.sleep(1)
        self.pawn_update()
        messagebox.showinfo(f'{current_name} - Telah Berubah Posisi', f'{current_name}, Anda tidak sengaja menemukan tangga')
      case 14: # Ular 1
        if self.giliran:
            self.player2_loc = 7
            self.cek_petak()
        else:
            self.player1_loc = 7
            self.cek_petak()
        time.sleep(1)
        self.pawn_update()
        messagebox.showinfo(f'{current_name} - Telah Berubah Posisi', f'{current_name}, Anda telah dimakan sang ular')
      case 27: # Ular 2
        if self.giliran:
            self.player2_loc = 35
            self.cek_petak()
        else:
            self.player1_loc = 35
            self.cek_petak()
        time.sleep(1)
        self.pawn_update()
        messagebox.showinfo(f'{current_name} - Telah Berubah Posisi', f'{current_name}, Anda telah dimakan sang ular')