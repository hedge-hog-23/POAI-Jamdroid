import numpy as np
import cv2


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 255, 0), -1)
        points.append((x, y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255, 0, 255), 5)
        cv2.imshow("Image", img)
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     blue = img[x, y, 0]
    #     green = img[x, y, 1]
    #     red = img[x, y, 2]
    #     cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    #     img1 = np.zeros((512, 512, 3), np.uint8)
    #     img1[:] = [blue, green, red]
    #     cv2.imshow('SAI is COOL', img1)


img = np.zeros((512, 512, 3), np.uint8)

# img = cv2.imread(r'F:\opencv-master\opencv-master\samples\data\lena.jpg')
cv2.imshow("Image", img)
points = []
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
