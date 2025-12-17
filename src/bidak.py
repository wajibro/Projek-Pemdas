def x(self):
  self.canvas.delete(self.player1_pawnItem)
  self.canvas.delete(self.player2_pawnItem)
  self.canvas.delete(self.penjara_img)
  self.player1_pawnItem = self.canvas.create_image(self.kordinat_x[self.player1_loc]+2, self.kordinat_y[self.player1_loc]+2, anchor= 'nw',  image= self.player1_pawn)
  self.player2_pawnItem = self.canvas.create_image(self.kordinat_x[self.player2_loc]-2, self.kordinat_y[self.player2_loc]-2, anchor= 'nw',  image= self.player2_pawn)
  self.penjara_img = self.canvas.create_image(1067, 66, anchor='nw', image=self.penjara_import)