def IVRCalling():
    from twilio.rest import Client
    client = Client('ACead14325b467812d6a514c68eafa0125','cb8775d418bd3a5d7c3e34a4234f9ebb')
    # call = client.calls.create(to='+919667405524',from_='+16187536219', url='https://drive.google.com/uc?export=download&id=16wAhwyzeXnrrw09WydQhLMR0-06gw5wz')
    call = client.calls.create(to='+919667405524',from_='+16187536219', url='http://demo.twilio.com/docs/voice.xml')
    if call.sid:
        print("Call Made Sucessfully!")



def NewsFrame():
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

NewsFrame()
