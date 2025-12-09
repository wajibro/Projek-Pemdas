kordinat = [[0,0]]

kordinat.append([1100, 603])
for i in range(0, 9): # Garis Bawah Peta
  kordinat.append([1036-(48*i), 596])

kordinat.append([593, 603])
for i in range(0, 9): # Garis Kiri Peta
  kordinat.append([599, 539-(48*i)])

kordinat.append([593, 96])
for i in range(0, 9): # Garis Atas Peta
  kordinat.append([657+(48*i), 105])

kordinat.append([1100, 96])
for i in range(0, 9): # Garis Kanan Peta
  kordinat.append([1094, 160+(48*i)])

kordinat.append([0, 0])

def kordinat_x():
  return [x[0] for x in kordinat]

def kordinat_y():
  return [x[1] for x in kordinat]