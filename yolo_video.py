from YOLOtiny import *
from predictor import *
from lib.preprocess import *
import cv2

model = YOLOtiny()
serializers.load_npz("YOLOtiny_v2.model", model)

cap = cv2.VideoCapture("input_video.mp4")

while(True):
    ret, img = cap.read()
    objects = predict(model, img)
    print(objects)

    for object in objects:
        cv2.rectangle(img, object[0][0:2], object[0][2:4], (0, 0, 255), 2)
        cv2.putText(img, "%s:%.2f%%" % (object[1], object[2]), (object[0][0], object[0][1]-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
