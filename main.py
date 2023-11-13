import cv2
import numpy as np

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan bir kareyi oku
    ret, kare = kamera.read()

    # Orijinal görüntüyü göster
    cv2.imshow("Orijinal Görüntü", kare)

    # Görüntüyü HSV renk uzayına çevir
    hsv_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Kırmızı renk sınırlarını belirle (HSV formatında)
    alt_kirmizi = np.array([0, 100, 100])
    ust_kirmizi = np.array([10, 255, 255])

    # Belirtilen sınırlar içindeki renkleri bul ve maskeyi uygula
    kirmizi_maske = cv2.inRange(hsv_kare, alt_kirmizi, ust_kirmizi)

    # Kırmızı renklere ait olan bölgeyi göster
    kirmizi_sonuc = cv2.bitwise_and(kare, kare, mask=kirmizi_maske)
    cv2.imshow("Sadece Kirmizi Renk", kirmizi_sonuc)

    # Eğer 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
cv2.destroyAllWindows()

