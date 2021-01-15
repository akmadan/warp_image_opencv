import cv2
import numpy as np


def getpoints(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 4, (255,0,0), -1)
        points.append([x,y])
        print(points)
        if len(points)==4:
            getperspective()
    cv2.imshow('image', img)

def getperspective():
    width = points[1][0] - points[0][0]
    height = points[2][1] - points[0][1]
    pts1 = np.float32([points[0:4]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow('output', imgOutput)



points = []
img = cv2.imread('assets/cards.jpg')
while True:
    img = cv2.resize(img, (400, 300))
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', getpoints)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    elif cv2.waitKey(1) & 0xff == ord('r'):
        img = cv2.imread('assets/cards.jpg')
        points = []
        img = cv2.resize(img, (400, 300))
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', getpoints)
    else:
        continue














