import cv2
img=cv2.VideoCapture(0)

while True:
    ret, frames= img.read()
    cv2.imshow("dhanush",frames)
    key= cv2.waitKey(20)
    if key==27:
        break