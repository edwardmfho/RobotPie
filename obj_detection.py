import cv2
import numpy as np
from datetime import datetime
from config import *

"""
Module to detect object for the RobotPie

To-do:
 - recognize person and return such result to main module for further action 
   (person-following algorithm)


"""


video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

img_counter = 0

net = cv2.dnn.readNet(YOLO_WEIGHTS_PATH,YOLO_CFG_PATH)
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


while True:

	ret, frame = video_capture.read()
	height, width, channels = frame.shape

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	k = cv2.waitKey(1)
# Base on https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/
	blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
	net.setInput(blob)
	outs = net.forward(output_layers)

	class_ids = []
	confidences = []
	boxes = []
	for out in outs:
	    for detection in out:
	        scores = detection[5:]
	        class_id = np.argmax(scores)
	        confidence = scores[class_id]
	        if confidence > 0.5:
	            # Object detected
	            center_x = int(detection[0] * width)
	            center_y = int(detection[1] * height)
	            w = int(detection[2] * width)
	            h = int(detection[3] * height)
	            # Rectangle coordinates
	            x = int(center_x - w / 2)
	            y = int(center_y - h / 2)
	            boxes.append([x, y, w, h])
	            confidences.append(float(confidence))
	            class_ids.append(class_id)

	indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
	font = cv2.FONT_HERSHEY_PLAIN
	
	# Command line printing object detected in frame. 
	for i in range(len(boxes)):
	    if i in indexes:
	        x, y, w, h = boxes[i]
	        label = str(classes[class_ids[i]])
	        print('{} was detected in the scene.'.format(label))
	        color = colors[i]
	        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
	        cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)        
		
	cv2.imshow('Object Detection', frame)

	if k % 256 == 27:
		break

	elif k % 256 == 32:
		img_name = "facedetect_webcam_{}.png".format(img_counter)
		cv2.imwrite(img_name, frame)
		print("{} written!".format(img_name))
		img_counter += 1

video_capture.release()
cv2.destroyAllWindows()