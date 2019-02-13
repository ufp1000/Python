import cv2

image=cv2.imread("smallgray.png", 0)

print(image)

cv2.imwrite("newsmallgray.png", image)