def pay_props(self):
  player_amount = int(self.amount_read_player(self.which_player)) - 100000
  player_amount_invers = int(self.amount_read_player(self.which_player_invers)) + 100000
  self.amount_add_player(self.which_player, player_amount)
  self.amount_add_player(self.which_player_invers, player_amount_invers)