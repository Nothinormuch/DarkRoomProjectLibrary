import cv2
cam = cv2.VideoCapture(0)
imagecount=1
while True:
    frame = cam.read()[1]
    frame[0:280,0:260] =  frame[100:380 , 200:460]
    cv2.imshow("Image",frame)
    if cv2.waitKey(1) == 13:
        break
    elif cv2.waitKey(1) == ord("q"):
        cv2.imwrite("./Images/Image{}.png".format(imagecount),frame)
        imagecount+=1
cv2.destroyAllWindows()
cam.release()