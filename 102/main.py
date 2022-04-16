import cv2

def take_snapshot():
    #initialize cv2
    capture = cv2.VideoCapture(0)
    result = True
    #Infinite while loop
    while(result):
        #Reading the frames while the camera is on
        ret, frame = capture.read()

        #Storing the photo to a folder
        cv2.imwrite("Picture1.jpg", frame)

        #To stop the infinite loop
        result = False

    #Release the camera
    capture.release()
    #All the windows are destroyed that were being used
    cv2.destroyAllWindows()

take_snapshot()