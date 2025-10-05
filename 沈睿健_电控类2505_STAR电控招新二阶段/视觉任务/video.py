import cv2

def transition(img):
    h, s, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    for i in range(height*width):
        y = i // width
        x = i % width
        if 45 <= h[y, x] <= 77 and 43 <= s[y, x] <= 255 and 46 <= v[y, x] <= 255:
            pass
        else:
            img[y][x] = [0, 0, 0]
    return img


vd = cv2.VideoCapture("video.mp4")
ret, frame = vd.read()
height = frame.shape[0]
width = frame.shape[1]
while True:
    ret, frame = vd.read()
    if not ret:
        break
    cv2.imshow('Video', transition(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vd.release()
cv2.destroyAllWindows()
