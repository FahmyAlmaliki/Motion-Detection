# Motion Detection with Alarm

Sistem deteksi gerakan real-time menggunakan OpenCV yang dapat membunyikan alarm ketika gerakan terdeteksi melalui webcam.

## Fitur

- **Deteksi gerakan real-time** menggunakan webcam
- **Alarm suara** otomatis ketika gerakan terdeteksi
- **Visualisasi gerakan** dengan kotak pembatas hijau
- **Interface sederhana** dengan tampilan video langsung
- **Kontrol mudah** dengan tombol ESC untuk keluar

## Persyaratan Sistem

- Python 3.x
- Windows OS (untuk fitur alarm suara)
- Webcam yang terhubung

## Dependensi

Pastikan Anda telah menginstal pustaka berikut:

```bash
pip install opencv-python
```

**Catatan:** Modul `winsound` sudah termasuk dalam instalasi Python standar di Windows.

## Cara Penggunaan

1. **Clone atau download repository ini**
   ```bash
   git clone https://github.com/FahmyAlmaliki/Motion-Detection.git
   cd Motion-Detection
   ```

2. **Jalankan program**
   ```bash
   python motion.py
   ```

3. **Menggunakan aplikasi:**
   - Program akan otomatis mengakses webcam default (kamera 0)
   - Tunggu beberapa detik hingga kamera siap
   - Gerakan akan terdeteksi dan ditandai dengan kotak hijau
   - Alarm beep akan berbunyi ketika gerakan terdeteksi
   - Tekan tombol **ESC** untuk keluar dari program

## Cara Kerja

1. **Inisialisasi:** Program mengambil frame pertama sebagai referensi
2. **Preprocessing:** Setiap frame dikonversi ke grayscale dan di-blur untuk mengurangi noise
3. **Deteksi perbedaan:** Menghitung perbedaan absolut antara frame referensi dan frame saat ini
4. **Thresholding:** Menggunakan binary threshold untuk menyoroti area yang berubah
5. **Deteksi kontur:** Mencari kontur dari area yang berubah
6. **Filtering:** Mengabaikan kontur kecil (< 1000 piksel) untuk menghindari false positive
7. **Alarm:** Membunyikan beep 1000 Hz selama 200ms ketika gerakan terdeteksi

## Parameter yang Dapat Disesuaikan

Anda dapat memodifikasi parameter berikut dalam kode untuk menyesuaikan sensitivitas:

- **Blur kernel size:** `(21, 21)` - ukuran kernel Gaussian blur
- **Threshold value:** `25` - nilai ambang batas untuk deteksi perbedaan
- **Minimum contour area:** `1000` - area minimum kontur yang dianggap sebagai gerakan
- **Beep frequency:** `1000` Hz - frekuensi suara alarm
- **Beep duration:** `200` ms - durasi suara alarm

## Struktur File

```
Motion-Detection/
│
├── motion.py          # File utama program deteksi gerakan
└── README.md         # Dokumentasi proyek
```

## Troubleshooting

### Kamera tidak terdeteksi
- Pastikan webcam terhubung dengan benar
- Coba ubah parameter `cv2.VideoCapture(0)` menjadi `cv2.VideoCapture(1)` atau nomor lain
- Pastikan tidak ada aplikasi lain yang menggunakan webcam

### Alarm tidak berbunyi
- Pastikan volume sistem tidak dalam mode mute
- Fitur alarm hanya bekerja di sistem Windows
- Periksa apakah modul `winsound` terimpor dengan benar

### Deteksi terlalu sensitif
- Tingkatkan nilai threshold (dari 25 ke nilai yang lebih tinggi)
- Perbesar ukuran minimum area kontur (dari 1000 ke nilai yang lebih besar)
- Perbesar ukuran kernel blur untuk mengurangi noise

### Deteksi kurang sensitif
- Kurangi nilai threshold (dari 25 ke nilai yang lebih kecil)
- Perkecil ukuran minimum area kontur
- Kurangi ukuran kernel blur

## Kontribusi

Kontribusi selalu diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## Lisensi

Proyek ini bersifat open source dan tersedia di bawah [MIT License](LICENSE).

## Author

**Fahmy Almaliki**
- GitHub: [@FahmyAlmaliki](https://github.com/FahmyAlmaliki)

## Acknowledgments

- OpenCV community untuk pustaka computer vision yang luar biasa
- Python community untuk dukungan dan dokumentasi yang comprehensive
