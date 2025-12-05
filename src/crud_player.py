def name_add(self, name1, name2): # Menambahkan nama pemain ke file teks
  try:
      with open('src/data_pemain/player1_name.txt', 'w') as file:
          file.write(str(name1))
      with open('src/data_pemain/player2_name.txt', 'w') as file:
          file.write(str(name2))
  except:
      print("Fungsi name_add error")

def name_read_player(self, x): # Membaca nama pemain dari file teks
  if x == 'player1':
      with open('src/data_pemain/player1_name.txt', 'r') as file:
        p1_name = file.read()
      return p1_name
  elif x == 'player2':
      with open('src/data_pemain/player2_name.txt', 'r') as file:
        p2_name = file.read()
      return p2_name

def amount_read_player(self, x): # Membaca jumlah uang pemain dari file teks
  if x == 'player1':
      with open('src/data_pemain/player1_amount.txt', 'r') as file:
        p1 = file.read()
      return p1
  elif x == 'player2':
      with open('src/data_pemain/player2_amount.txt', 'r') as file:
        p2 = file.read()
      return p2