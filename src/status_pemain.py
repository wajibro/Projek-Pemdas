from tkinter import *

def x(self):
  self.player1_name = self.name_read_player('player1')
  self.player2_name = self.name_read_player('player2')
  self.player1_amount = self.amount_read_player('player1')
  self.player2_amount = self.amount_read_player('player2')
  
  self.player1_name_label = Label(self.frame, text=f'Player 1 - {self.player1_name}', font=('Poppins', 24), bg='white')
  self.player1_amount_label = Label(self.frame, text=f'Rp. {self.player1_amount}', font=('Poppins', 24))

  self.player2_name_label = Label(self.frame, text=f'Player 2 - {self.player2_name}', font=('Poppins', 24), bg='white')
  self.player2_amount_label = Label(self.frame, text=f'Rp. {self.player2_amount}', font=('Poppins', 24))

  self.player1_name_label.place(x=9, y=7)
  self.player1_amount_label.place(x=9, y=40)
  self.player2_name_label.place(x=9, y=84)
  self.player2_amount_label.place(x=9, y=120)