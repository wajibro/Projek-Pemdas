list_town = [2, 5, 6, 8, 9, 10, 12, 13, 15, 17, 20, 22, 23, 25, 28, 29, 30, 32, 33, 34, 37, 39, 40]
ular_tangga = [4, 18, 14, 27]

def cek_petak(self):
  self.stats_update()

  match self.which_player_loc:
    case x if x in ular_tangga:
      self.ular_tangga()
    case x if x in list_town:
      self.ask()
    case 1:
      self.start_bonus()
    case 3:
      self.pay_tax()
    case x if x in [19, 35]:
      self.pay_needs()
    case x if x in [24, 36]:
      self.bansos()
    case x if x in [16, 26, 38]:
      self.chance_card()
    case 7:
      self.badluck_card()
    case 11:
      self.travelling()
    case 21:
      self.pulau_asing()
    case 31:
      self.penjara

# Simpan data pembelian properti
def which_player_props_add(self, player, prop):
  match player:
    case 'player1':
      self.props_player1.append(prop)
    case 'player2':
      self.props_player2.append(prop)

# Periksa data pembelian yang sudah tersimpan
def which_player_props_read(self, player):
  match player:
    case 'player1':
      return self.props_player1
    case 'player2':
      return self.props_player2
  
def which_player_amount_read(self, x):
  match x:
    case 'player1':
      return self.player1_amount
    case 'player2':
      return self.player2_amount
    
def which_player_amount_add(self, player, x):
  match player:
    case 'player1':
      self.player1_amount = int(x)
    case 'player2':
      self.player2_amount = int(x)