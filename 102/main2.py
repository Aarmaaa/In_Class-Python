import cv2
import time
import random

start_time = time.time()


def  take_snapshot():
    capture = cv2.VideoCapture(0)
    result = True
    number = random.randint(0,100)

    while(result):
        ret, frame = capture.read()
        img = "Picture" + str(number) + ".png"
        cv2.imwrite(img, frame)
        start_time = time.time()

        result = False

    capture.release()
    cv2.destroyAllWindows()

def main():
    
    while(True):
        if (time.time() - start_time >= 5) :
            take_snapshot()

main()