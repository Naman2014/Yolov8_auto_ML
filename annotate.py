import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter.simpledialog import askstring
import os

image_path = r'C:\Users\naman\Desktop\Trumio\AWS Images - Copy\image_121.jpg'

image = cv.imread(image_path)
image = cv.resize(image, (640, 480))

rectangles = []

def get_class_name():
    root = tk.Tk()
    root.withdraw()  

    class_name = askstring("Class Name", "Enter the name of the class:")
    return class_name

def click_event(event, x, y, flags, param):
    global rectangles, str_msg
    if event == cv.EVENT_LBUTTONDOWN:
        rectangles.append([(x, y)])
        cv.imshow('image', image)

    elif event == cv.EVENT_LBUTTONUP and len(rectangles[-1]) == 1:
        rectangles[-1].append((x, y))
        str_msg = "Tap at two points"
        cv.rectangle(image, rectangles[-1][0], rectangles[-1][1], (0, 255, 0), 2)
        cv.imshow('image', image)
        if len(rectangles[-1]) == 2:
            class_name = get_class_name()
            image_name = os.path.splitext(os.path.basename(image_path))[0]

            if class_name is not None:
                output_file = f"data\\train\\labels\\{image_name}.txt"

                with open(output_file, "a") as file:
                    x, y = rectangles[-1][0]
                    w = rectangles[-1][1][0] - rectangles[-1][0][0]
                    h = rectangles[-1][1][1] - rectangles[-1][0][1]
                    center_x = x + w // 2
                    center_y = y + h // 2
                    file.write(f"{class_name}, {center_x},{center_y},{w},{h}\n")

                cv.putText(image, class_name, (x, y), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)

cv.namedWindow('image')
cv.setMouseCallback('image', click_event)

while True:
    cv.imshow('image', image)
    if cv.waitKey(1) == 27:
        break

image_name = os.path.splitext(os.path.basename(image_path))[0]
cv.imwrite(f"{image_name}_annotated.jpg", image)
print("Coordinates of Rectangles:", rectangles)

cv.destroyAllWindows()
