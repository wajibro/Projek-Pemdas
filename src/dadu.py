import random

def x(self, event=None):
    self.dadu_num = random.randint(1, 6)
    if self.giliran == True:
      self.player1_loc += self.dadu_num
    elif self.giliran == False:
      self.player2_loc += self.dadu_num

    self.pawn_update()
    self.giliran = not self.giliran