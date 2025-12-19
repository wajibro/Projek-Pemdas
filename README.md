# Proyek Pemdas - Game Monopoly Indonesia

Proyek ini adalah implementasi game Monopoly yang disesuaikan dengan konteks Indonesia, dibangun menggunakan bahasa pemrograman Python dengan library Tkinter untuk antarmuka grafis dan PIL untuk manipulasi gambar.

## Struktur Proyek

```
projek-pemdas/
├── main.py                 # File utama program
├── assets/                 # Folder untuk aset gambar
│   ├── apar_1.png         # Gambar apartemen pemain 1
│   ├── apar_2.png         # Gambar apartemen pemain 2
│   ├── background.png     # Latar belakang utama
│   ├── bg_town1-8.png     # Latar belakang info kota
│   ├── btn_name_init.png  # Tombol inisialisasi nama
│   ├── btn_start.png      # Tombol mulai
│   ├── dadu_0-6.png       # Gambar dadu
│   ├── kartu_kesempatan.png # Kartu kesempatan
│   ├── kejadian_sial.png  # Kartu kejadian sial
│   ├── logo_M.png         # Logo game
│   ├── modal_entry.png    # Modal input
│   ├── monopoly_guy.png   # Karakter Monopoly
│   ├── penjara.png        # Gambar penjara
│   ├── peta.png           # Peta permainan
│   ├── player_1.png       # Bidak pemain 1
│   ├── player_2.png       # Bidak pemain 2
│   ├── player1_entry.png  # Input pemain 1
│   ├── player2_entry.png  # Input pemain 2
│   ├── Poppins-Regular.ttf # Font custom
│   ├── Press Enter to Start.png
│   ├── team-screen.png    # Layar tim
│   └── title_sub.png      # Subjudul
├── pages/                 # Folder untuk halaman UI
│   ├── loadscreen.py      # Layar loading dan splash screen
│   ├── name_init.py       # Halaman inisialisasi nama pemain
│   └── play.py            # Halaman utama permainan
├── src/                   # Folder untuk logika backend
│   ├── action.py          # Sistem aksi permainan (sewa, pajak, bonus, dll)
│   ├── bidak.py           # Sistem pergerakan bidak pemain
│   ├── buy_props.py       # Sistem pembelian properti
│   ├── config.py          # Konfigurasi jendela
│   ├── crud_player.py     # Manajemen data pemain
│   ├── dadu.py            # Sistem lempar dadu
│   ├── kordinat.py        # Koordinat peta permainan
│   ├── move_option.py     # Opsi pergerakan pemain
│   ├── status_pemain.py   # Update status pemain
│   └── data_pemain/       # Folder data pemain
│       ├── nama/
│       │   ├── player1_name.txt
│       │   └── player2_name.txt
│       ├── properti/
│       │   ├── player1_props.txt
│       │   └── player2_props.txt
│       └── uang/
│           ├── player1_amount.txt
│           └── player2_amount.txt
└── test/                  # Folder untuk testing
    └── fullscreen.py      # Test fullscreen
```

## Deskripsi File Utama

### main.py
File utama yang menjalankan seluruh program. Berisi:
- Setup jendela Tkinter dengan konfigurasi fullscreen
- Import semua modul yang diperlukan
- Definisi class untuk setiap layar (screen1-4)
- Sistem navigasi antar layar
- Event handling untuk fullscreen dan exit
- Inisialisasi game loop

Fitur utama:
- Fullscreen toggle dengan F11
- Exit fullscreen dengan Escape
- Window close handler dengan konfirmasi

### pages/loadscreen.py
Menangani layar loading dan splash screen:
- `splash1()`: Menampilkan layar tim dengan logo
- `showof1()`: Transisi ke layar utama dengan background dan logo
- `splash2()`: Layar awal dengan background biru
- `showof2()`: Menampilkan karakter Monopoly, judul, dan tombol start

### pages/name_init.py
Halaman inisialisasi nama pemain:
- Input field untuk nama pemain 1 dan 2
- Validasi input nama
- Transisi ke layar permainan utama

### pages/play.py
Halaman utama permainan:
- Menampilkan peta Monopoly Indonesia
- UI untuk status pemain (nama, uang)
- Area untuk informasi properti
- Tombol-tombol aksi permainan

## Modul Backend (src/)

### action.py
Menangani semua aksi permainan:
- `pay_rent()`: Sistem pembayaran sewa
- `cek_petak()`: Pengecekan petak yang dilewati
- `start_bonus()`: Bonus melewati start
- `pay_tax()`: Pembayaran pajak
- `pay_needs()`: Pembayaran kebutuhan (air/listrik)
- `bansos()`: Bantuan sosial
- `travelling()`: Kartu perjalanan
- `chance_card()`: Kartu kesempatan
- `badluck_card()`: Kartu sial
- `pulau_asing()`: Event pulau asing
- `penjara()`: Sistem penjara

### buy_props.py
Sistem pembelian properti:
- Daftar kota-kota di Indonesia (23 kota)
- Sistem harga berdasarkan tier kota
- Fungsi pembelian 1 atau 2 apartemen
- Penyimpanan data properti pemain
- Perhitungan sewa berdasarkan jumlah properti

Kota-kota yang tersedia:
- Tier 1: Medan, Makassar, Semarang
- Tier 2: Bandung, Surabaya, Batam
- Tier 3: Bekasi, Tanggerang, Depok
- Tier 4: Jakarta, Banten
- Tier 5: Ternate, Ambon, Irian
- Tier 6: Padang, Palembang, Lampung
- Tier 7: Pontianak, Banjarmasin
- Tier 8: Balikpapan, Jogja, Solo, Denpasar

### crud_player.py
Manajemen data pemain:
- `name_add()`: Menyimpan nama pemain
- `name_read_player()`: Membaca nama pemain
- `amount_set()`: Set jumlah uang awal
- `amount_add_player()`: Menambah/kurangi uang pemain
- `amount_read_player()`: Membaca jumlah uang pemain

### dadu.py
Sistem lempar dadu:
- `roll_dice()`: Generate angka acak 1-6
- `pos_increase()`: Update posisi pemain
- `dice_img()`: Update tampilan gambar dadu
- `dadu_update()`: Refresh UI dadu

### bidak.py
Sistem pergerakan bidak:
- Update posisi visual bidak pemain di peta
- Sinkronisasi dengan koordinat dari kordinat.py

### status_pemain.py
Update tampilan status pemain:
- `update_data()`: Refresh nama dan jumlah uang pemain
- Sinkronisasi dengan data dari crud_player.py

### move_option.py
Opsi pergerakan pemain:
- `ask()`: Dialog pembelian properti atau lanjut
- `gonnaBuy()`: Pilihan untuk beli properti
- `nextPlayer()`: Ganti giliran pemain

### kordinat.py
Koordinat peta permainan:
- Array koordinat X dan Y untuk setiap petak
- Pemetaan posisi bidak pemain

### config.py
Konfigurasi jendela:
- Setup ukuran jendela (1280x720)
- Konfigurasi canvas utama

## Mekanika Permainan

### Alur Permainan
1. **Loading Screen**: Tampilan splash screen tim
2. **Main Menu**: Layar utama dengan tombol start
3. **Name Initialization**: Input nama pemain 1 dan 2
4. **Main Game**: Permainan Monopoly Indonesia

### Aturan Dasar
- 2 pemain bergantian
- Lempar dadu untuk bergerak
- Beli properti di kota-kota Indonesia
- Bayar sewa saat mendarat di properti lawan
- Berbagai event khusus (kartu, pajak, bonus)
- Pemain kalah jika uang habis (bangkrut)

### Sistem Uang
- Uang awal: Rp 1.500.000 per pemain
- Bonus start: Rp 200.000
- Harga properti bervariasi berdasarkan tier kota
- Sewa = 50% harga properti (1 apartemen) atau 100% (2 apartemen)

### Event Khusus
- **Start**: Bonus Rp 200.000
- **Pajak**: Bayar berdasarkan jumlah properti
- **Kebutuhan**: Bayar air/listrik berdasarkan properti
- **Bansos**: Dapat Rp 20.000-50.000
- **Travelling**: Pilih petak tujuan
- **Chance Card**: Kartu kesempatan acak
- **Bad Luck Card**: Kartu sial acak
- **Pulau Asing**: Stuck sampai lempar 6 atau bayar Rp 100.000
- **Penjara**: Skip 1 giliran

## Cara Menjalankan

1. Pastikan Python 3.x terinstall
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Jalankan program:
   ```bash
   python main.py
   ```

## Kontrol
- **F11**: Toggle fullscreen
- **Escape**: Exit fullscreen
- **Mouse**: Klik tombol dan interaksi UI

## Teknologi yang Digunakan
- **Python 3.x**: Bahasa pemrograman utama
- **Tkinter**: GUI framework
- **PIL (Pillow)**: Manipulasi gambar
- **OS/CTypes**: Load font custom

## Tim Pengembang
- Wajibro (Lead Developer)
- Tim Pemdas

## Lisensi
Proyek ini dibuat untuk tujuan edukasi dalam mata kuliah Pemrograman Dasar.
