import cv2
cam = cv2.VideoCapture(0)
imagecount=1
while True:
    frame = cam.read()[1]
    faceframe=frame[100:380 , 200:460]
    scalepercent=50
    shrunkheight=int(faceframe.shape[0]*(scalepercent/100))
    shrunkwidth=int(faceframe.shape[1]*(scalepercent/100))
    # print(shrunkheight,shrunkwidth)
    shrunkframe=cv2.resize(faceframe,(shrunkwidth,shrunkheight))
    # print(shrunkframe.shape)
    finalframe=frame
    finalframe[0:shrunkheight,0:shrunkwidth] = shrunkframe
    cv2.imshow("Image",finalframe)
    if cv2.waitKey(1) == 13:
        break
    elif cv2.waitKey(1) == ord("q"):
        cv2.imwrite("Image{}.png".format(imagecount),finalframe)
        imagecount+=1
cv2.destroyAllWindows()
cam.release()
