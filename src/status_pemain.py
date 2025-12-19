from tkinter import *
from tkinter import messagebox

def update_data(self):
    self.player1_name = self.name_read_player('player1')
    self.player2_name = self.name_read_player('player2')
    self.player1_amount = self.amount_read_player('player1')
    self.player2_amount = self.amount_read_player('player2')

    self.which_player = 'player2' if self.giliran else 'player1'
    self.which_player_invers = 'player1' if self.giliran else 'player2'

    self.which_player_name = self.player2_name if self.giliran else self.player1_name
    self.which_player_name_invers = self.player1_name if self.giliran else self.player2_name

    self.which_player_loc = self.player2_loc if self.giliran else self.player1_loc
    self.which_player_loc_invers = self.player1_loc if self.giliran else self.player2_loc

    if hasattr(self, 'player1_amount_label'):
        self.player1_amount_label.destroy()
    if hasattr(self, 'player2_amount_label'):
        self.player2_amount_label.destroy()
    if hasattr(self, 'player_giliran'):
        self.player_giliran.destroy()

    self.player1_name_label = Label(self.frame, text=f'Player 1 - {self.player1_name}', font=('Poppins', 24), bg='white')
    self.player1_amount_label = Label(self.frame, text=f'Rp {f"{int(self.player1_amount):,}".replace(",", ".")}', font=('Poppins', 12), bg='white')

    self.player2_name_label = Label(self.frame, text=f'Player 2 - {self.player2_name}', font=('Poppins', 24), bg='white')
    self.player2_amount_label = Label(self.frame, text=f'Rp {f"{int(self.player2_amount):,}".replace(",", ".")}', font=('Poppins', 12), bg='white')

    self.player_giliran = Label(self.frame, text=self.which_player_name, bg='white', font=('Poppins', 18))
    
    self.player1_name_label.place(x=24, y=5)
    self.player1_amount_label.place(x=9, y=45)
    self.player2_name_label.place(x=24, y=84)
    self.player2_amount_label.place(x=9, y=130)
    self.player_giliran.place(x=169, y=579)

    self.list_harga()
    if self.player1_name != '' and self.player2_name != '':    
        self.game_over()