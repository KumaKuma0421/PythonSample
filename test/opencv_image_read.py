import cv2

filePath = "/usr/share/pixmaps/faces/coffee2.jpg"
img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("./testGrayScale.jpg", img)
cv2.destroyAllWindows()