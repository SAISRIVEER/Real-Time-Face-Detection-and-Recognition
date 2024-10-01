import cv2
import face_recognition
from simple_facerecognition import SimpleFacerecognition

sfr = SimpleFacerecognition()
sfr.load_encoding_images("IMAGES/")
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_locations, face_names = sfr.detect_known_faces(img)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(img, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,200), 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,200), 4) 

    # faces = face_cascade.detectMultiScale(rgb_img, 1.5, 4)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("FACE DETECTION", img)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
