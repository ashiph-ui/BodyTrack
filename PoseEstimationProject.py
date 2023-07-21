import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('BodyTrack\\videos\\1.mp4')
cap.set(3, 1920)
cap.set(4, 1080)
pTime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, "fps: " + str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


