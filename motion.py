import cv2
import time
import winsound  # Modul untuk menghasilkan bunyi beep di Windows

# Inisialisasi kamera
cap = cv2.VideoCapture(0)
time.sleep(2)  # Tunggu 2 detik untuk memastikan kamera siap

# Baca frame awal sebagai referensi untuk mendeteksi perbedaan gerakan
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)  # Blur untuk mengurangi noise

while True:
    # Baca frame baru dari kamera
    ret, frame2 = cap.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
    frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)  # Blur frame baru

    # Hitung perbedaan antara frame sebelumnya dan sekarang
    diff = cv2.absdiff(frame1_gray, frame2_gray)

    # Binarisasi gambar untuk menyoroti perbedaan yang mencolok
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)  # Perbesar area putih untuk deteksi lebih baik

    # Temukan kontur (area gerakan) dari hasil threshold
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False  # Flag untuk menyimpan status deteksi gerakan

    for contour in contours:
        # Abaikan kontur kecil yang dianggap bukan gerakan signifikan
        if cv2.contourArea(contour) < 1000:
            continue

        # Jika gerakan cukup besar, tandai sebagai terdeteksi
        motion_detected = True
        (x, y, w, h) = cv2.boundingRect(contour)  # Dapatkan area kotak pembatas
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Gambar kotak pada frame
        cv2.putText(frame2, "Gerakan Terdeteksi", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Tampilkan teks peringatan

    # Jika gerakan terdeteksi, bunyikan alarm beep
    if motion_detected:
        winsound.Beep(1000, 200)  # Frekuensi 1000 Hz selama 200 milidetik

    # Tampilkan hasil deteksi pada jendela
    cv2.imshow("Motion Detection with Alarm", frame2)

    # Update frame sebelumnya untuk perbandingan di iterasi berikutnya
    frame1_gray = frame2_gray.copy()

    # Tekan tombol 'Esc' (kode ASCII 27) untuk keluar dari program
    if cv2.waitKey(10) & 0xFF == 27:
        break

# Bersihkan resource setelah selesai
cap.release()
cv2.destroyAllWindows()
