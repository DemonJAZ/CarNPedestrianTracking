import cv2


car_detection = cv2.CascadeClassifier("cars.xml")
pedestrian_detection = cv2.CascadeClassifier("haarcascade_fullbody.xml")

video = cv2.VideoCapture("NEWYORK.mp4")

while True:

    Successfull_read,frame= video.read()
    gray_fram = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    get_car = car_detection.detectMultiScale(gray_fram)
    get_pedestian = pedestrian_detection.detectMultiScale(gray_fram)
    for (x, y, w, h) in get_car:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0,255), 3)
    for (x, y, w, h) in get_pedestian:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0,0), 3)

    cv2.imshow("program",frame)
    key = cv2.waitKey(1)

    ## press Q to quit
    if key == 81 or key == 113:
        break
video.release()