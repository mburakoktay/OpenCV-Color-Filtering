import cv2 as cv
import numpy as np


# Boş bir fonksiyon (Trackbar için gerekli)
def nothing(x):
    pass


# 1. Kontrol Penceresi ve Trackbarlar
cv.namedWindow("Trackbar")

# Senin değişken isimlerini daha net hale getirdik (azMavi -> minMavi)
cv.createTrackbar("minMavi", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxMavi", "Trackbar", 255, 255, nothing)
cv.createTrackbar("minYesil", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxYesil", "Trackbar", 255, 255, nothing)
cv.createTrackbar("minKirmizi", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxKirmizi", "Trackbar", 255, 255, nothing)

# Video dosyasını oku
takip = cv.VideoCapture("takip.mp4")

while True:
    kontrol, frame = takip.read()

    # Video biterse döngüyü kır (Hata almamak için)
    if not kontrol:
        break

    # Trackbar değerlerini oku
    minM = cv.getTrackbarPos("minMavi", "Trackbar")
    maxM = cv.getTrackbarPos("maxMavi", "Trackbar")
    minY = cv.getTrackbarPos("minYesil", "Trackbar")
    maxY = cv.getTrackbarPos("maxYesil", "Trackbar")
    minK = cv.getTrackbarPos("minKirmizi", "Trackbar")
    maxK = cv.getTrackbarPos("maxKirmizi", "Trackbar")

    # Renk aralıklarını tanımla (BGR sırasıyla)
    alt_sinir = np.array([minM, minY, minK])
    ust_sinir = np.array([maxM, maxY, maxK])

    # Maskeleme ve Sonuç
    maske = cv.inRange(frame, alt_sinir, ust_sinir)
    son_hal = cv.bitwise_and(frame, frame, mask=maske)

    # Görüntüleri göster
    cv.imshow("Orijinal Video", frame)
    cv.imshow("Maske (Siyah-Beyaz)", maske)
    cv.imshow("Filtrelenmiş Sonuc", son_hal)

    # 'q' tuşu ile çıkış yap
    if cv.waitKey(20) & 0xFF == ord("q"):
        break

takip.release()
cv.destroyAllWindows()