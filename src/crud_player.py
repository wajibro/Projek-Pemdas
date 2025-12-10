def name_add(self, name1, name2): # Menambahkan nama pemain ke file teks
  try:
    with open('src/data_pemain/nama/player1_name.txt', 'w') as file:
        file.write(str(name1))
    with open('src/data_pemain/nama/player2_name.txt', 'w') as file:
        file.write(str(name2))
  except:
    print("Fungsi name_add error")

def name_read_player(self, player): # Membaca nama pemain dari file teks
  if player == 'player1':
    with open('src/data_pemain/nama/player1_name.txt', 'r') as file:
      return file.read()
  elif player == 'player2':
    with open('src/data_pemain/nama/player2_name.txt', 'r') as file:
      return file.read()

def amount_set(self, x): # Mengatur ulang jumlah uang pemain ke file teks (awal permainan)
  try:
    with open('src/data_pemain/uang/player1_amount.txt', 'w') as file:
        file.write(x)
    with open('src/data_pemain/uang/player2_amount.txt', 'w') as file:
      file.write(x)
  except:
    print("Fungsi amount_set error")

def amount_add_player(self, player, amount): # Membaca jumlah uang pemain dari file teks
  if player == 'player1':
    with open('src/data_pemain/uang/player1_amount.txt', 'w') as file:
      file.write(str(amount))
  elif player == 'player2':
    with open('src/data_pemain/uang/player2_amount.txt', 'w') as file:
      file.write(str(amount))

def amount_read_player(self, player): # Membaca jumlah uang pemain dari file teks
  if player == 'player1':
    with open('src/data_pemain/uang/player1_amount.txt', 'r') as file:
      return file.read()
  elif player == 'player2':
    with open('src/data_pemain/uang/player2_amount.txt', 'r') as file:
      return file.read()