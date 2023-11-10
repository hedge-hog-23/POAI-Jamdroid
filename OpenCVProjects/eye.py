import cv2

eye_cascade = cv2.CascadeClassifier(r'C:\Users\Senth\OneDrive\Desktop\eye_document.xml')
face_cascade = cv2.CascadeClassifier(r"C:\Users\Senth\OneDrive\Desktop\haarcascade_frontalface_default.xml")

# img = cv2.imread(r'F:\opencv-master\opencv-master\samples\data\test.jpg')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 3)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
