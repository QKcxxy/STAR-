import cv2

img=cv2.imread('pic.jpg')
width=img.shape[1]
height=img.shape[0]
h, s, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
for i in range(height * width):
    y = i // width
    x = i % width
    if 45 <= h[y, x] <= 77 and 43 <= s[y, x] <= 255 and 46 <= v[y, x] <= 255:
        print(y,x)
