from tkinter import *


def update_data(self):
    self.player1_name = self.name_read_player('player1')
    self.player2_name = self.name_read_player('player2')
    self.player1_amount = self.amount_read_player('player1')
    self.player2_amount = self.amount_read_player('player2')

    if hasattr(self, 'player1_amount_label'):
        self.player1_amount_label.destroy()
    if hasattr(self, 'player2_amount_label'):
        self.player2_amount_label.destroy()
    if hasattr(self, 'player_giliran'):
        self.player_giliran.destroy()

    self.player1_name_label = Label(self.frame, text=f'Player 1 - {self.player1_name}', font=('Poppins', 24), bg='white')
    self.player1_amount_label = Label(self.frame, text=f'Rp. {self.player1_amount}', font=('Poppins', 24))

    self.player2_name_label = Label(self.frame, text=f'Player 2 - {self.player2_name}', font=('Poppins', 24), bg='white')
    self.player2_amount_label = Label(self.frame, text=f'Rp. {self.player2_amount}', font=('Poppins', 24))

    giliran_text = self.player2_name if self.giliran else self.player1_name
    self.player_giliran = Label(self.frame, text=giliran_text, font=('Poppins', 24))
    
    self.player1_name_label.place(x=24, y=7)
    self.player1_amount_label.place(x=9, y=40)
    self.player2_name_label.place(x=24, y=84)
    self.player2_amount_label.place(x=9, y=120)
    self.player_giliran.place(x=169, y=579)

    self.list_harga()