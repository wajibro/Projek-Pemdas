# Proyek Pemdas - Game Monopoly Indonesia v2.0

Proyek ini adalah implementasi game Monopoly yang disesuaikan dengan konteks Indonesia, dibangun menggunakan bahasa pemrograman Python dengan library Tkinter. Versi 2.0 membawa perubahan besar, termasuk mekanika permainan baru dan perbaikan arsitektur kode.

## Apa yang Baru di v2.0?
- **Mekanika Ular Tangga**: Beberapa petak di papan sekarang berfungsi sebagai ular atau tangga, memindahkan pemain ke posisi baru secara tak terduga.
- **Refactoring Logika Game**: Logika inti permainan dan penanganan data pemain telah disentralisasi ke dalam modul `data_handle.py` untuk meningkatkan modularitas dan kemudahan pengelolaan.
- **Penyimpanan Data Dalam Memori**: Sistem penyimpanan data pemain berbasis file `.txt` telah diganti dengan manajemen data di dalam memori selama sesi permainan, menghasilkan gameplay yang lebih cepat dan lancar.
- **Perbaikan Bug**: Berbagai perbaikan bug terkait giliran pemain, kondisi game over, dan event kartu telah diimplementasikan.

## Struktur Proyek

```
projek-pemdas/
├── main.py                 # File utama program
├── README.md               # File ini
├── assets/                 # Folder untuk aset gambar
├── pages/                  # Folder untuk modul UI per halaman
│   ├── loadscreen.py
│   ├── name_init.py
│   ├── opsi_ui.py
│   └── play.py
├── src/                    # Folder untuk logika backend
│   ├── action.py
│   ├── bidak.py
│   ├── buy_props.py
│   ├── config.py
│   ├── dadu.py
│   ├── data_handle.py      # Modul logika utama & data
│   ├── kordinat.py
│   ├── move_option.py
│   ├── status_pemain.py
│   └── ular_tangga.py      # Modul mekanika ular tangga
└── test/                   # Folder untuk skrip testing
```

## Deskripsi Modul Utama

### `main.py`
File utama yang menjalankan seluruh aplikasi. Bertanggung jawab untuk:
- Setup jendela utama Tkinter.
- Inisialisasi dan manajemen setiap layar/halaman permainan.
- Mengatur navigasi antar layar.
- Menangani event global seperti fullscreen (F11) dan keluar (Esc).

### `pages/`
Setiap file dalam direktori ini mengelola satu halaman atau layar spesifik dari antarmuka pengguna (UI), dari layar pemuatan awal hingga papan permainan utama.

### `src/`
Direktori ini berisi semua logika inti (backend) dari permainan.

- **`data_handle.py`**: Merupakan otak dari permainan di v2.0.
  - **`cek_petak()`**: Fungsi sentral yang menentukan aksi apa yang harus diambil berdasarkan posisi pemain di papan (misalnya, membeli properti, membayar pajak, atau mendarat di petak ular/tangga).
  - Mengelola status pemain (uang dan properti) di dalam memori selama permainan berjalan.

- **`ular_tangga.py`**: Mengimplementasikan mekanika ular tangga. Saat pemain mendarat di petak tertentu, modul ini dipanggil untuk memindahkan pemain ke posisi baru.

- **`action.py`**: Berisi implementasi dari berbagai aksi di papan permainan seperti membayar sewa, mengambil kartu kesempatan, membayar pajak, dan lain-lain.

- **`buy_props.py`**: Mengelola logika pembelian properti (apartemen) oleh pemain, termasuk daftar harga properti yang dibagi berdasarkan tingkatan kota.

- **`dadu.py` & `bidak.py`**: Mengatur fungsionalitas lempar dadu dan pergerakan visual bidak pemain di papan permainan.

- **`status_pemain.py`**: Mengatur pembaruan informasi status pemain (nama dan uang) yang ditampilkan di UI.

- **`move_option.py`**: Menyajikan dialog dan opsi kepada pemain setelah bergerak, seperti pilihan untuk membeli properti atau mengakhiri giliran.

## Mekanika Permainan

### Alur Permainan
1.  **Layar Pemuatan**: Aplikasi dimulai dengan splash screen.
2.  **Menu Utama**: Pemain menekan 'Enter' untuk memulai.
3.  **Inisialisasi Pemain**: Pemain memasukkan nama untuk Player 1 dan Player 2.
4.  **Permainan Utama**: Papan permainan ditampilkan dan permainan dimulai.

### Aturan Dasar
- Dua pemain bermain secara bergantian.
- Pemain melempar dadu untuk bergerak di sekitar papan.
- Pemain dapat membeli properti (apartemen) di berbagai kota di Indonesia.
- Mendarat di properti lawan mengharuskan pemain membayar sewa.
- Pemenang ditentukan saat salah satu pemain kehabisan uang (bangkrut).

### Event & Petak Khusus
- **Start**: Melewati petak 'Start' memberikan bonus uang.
- **Properti**: Dapat dibeli jika belum dimiliki. Jika dimiliki lawan, pemain harus bayar sewa.
- **Pajak**: Pemain harus membayar sejumlah pajak.
- **Kartu Kesempatan/Sial**: Pemain mengambil kartu yang memberikan efek positif atau negatif.
- **Penjara**: Pemain kehilangan satu giliran.
- **Ular Tangga**: Mendarat di petak ini akan memindahkan pemain ke petak lain, bisa maju (tangga) atau mundur (ular).

## Cara Menjalankan

1.  Pastikan Python 3.x terinstall di sistem Anda.
2.  Install library yang dibutuhkan:
    ```bash
    pip install pillow
    ```
3.  Jalankan program dari direktori root:
    ```bash
    python main.py
    ```

## Kontrol
-   **F11**: Masuk/Keluar mode layar penuh (fullscreen).
-   **Escape**: Keluar dari mode layar penuh.
-   **Mouse**: Digunakan untuk semua interaksi dalam game (klik tombol).

## Teknologi
-   **Python 3.x**: Bahasa pemrograman utama.
-   **Tkinter**: Framework standar Python untuk GUI.
-   **Pillow (PIL Fork)**: Library untuk memanipulasi dan menampilkan gambar.