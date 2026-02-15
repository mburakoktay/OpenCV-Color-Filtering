import cv2 as cv
import numpy as np


# for tranckbar
def nothing(x):
    pass


# Trackbars
cv.namedWindow("Trackbar")

# Senin değişken isimlerini daha net hale getirdik (azMavi -> minMavi)
cv.createTrackbar("minMavi", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxMavi", "Trackbar", 255, 255, nothing)
cv.createTrackbar("minYesil", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxYesil", "Trackbar", 255, 255, nothing)
cv.createTrackbar("minKirmizi", "Trackbar", 0, 255, nothing)
cv.createTrackbar("maxKirmizi", "Trackbar", 255, 255, nothing)

# Read video
takip = cv.VideoCapture("takip.mp4")

while True:
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    kontrol, frame = takip.read()

    
    if not kontrol:
        break

    # Read trackbar's value
    minM = cv.getTrackbarPos("minMavi", "Trackbar")
    maxM = cv.getTrackbarPos("maxMavi", "Trackbar")
    minY = cv.getTrackbarPos("minYesil", "Trackbar")
    maxY = cv.getTrackbarPos("maxYesil", "Trackbar")
    minK = cv.getTrackbarPos("minKirmizi", "Trackbar")
    maxK = cv.getTrackbarPos("maxKirmizi", "Trackbar")

    
    alt_sinir = np.array([minM, minY, minK])
    ust_sinir = np.array([maxM, maxY, maxK])

    # Mask 
    maske = cv.inRange(frame, alt_sinir, ust_sinir)
    son_hal = cv.bitwise_and(frame, frame, mask=maske)

    # Show videos
    cv.imshow("Orijinal Video", frame)
    cv.imshow("Maske (Siyah-Beyaz)", maske)
    cv.imshow("Filtrelenmiş Sonuc", son_hal)

    # Exit with "q"
    if cv.waitKey(20) & 0xFF == ord("q"):
        break





