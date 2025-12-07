def x(self):
  if self.player1_loc >= len(self.kordinat)-1:
    self.player1_loc = 1
  if self.player2_loc >= len(self.kordinat)-1:
    self.player2_loc = 1

  self.canvas.delete(self.player1_pawnItem)
  self.canvas.delete(self.player2_pawnItem)
  self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc]+2, self.kordinat_y[self.player1_loc]+2, anchor= 'nw',  image= self.player1_pawn)
  self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc]-2, self.kordinat_y[self.player2_loc]-2, anchor= 'nw',  image= self.player2_pawn)