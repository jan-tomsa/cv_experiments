import numpy as np
import cv2
from matplotlib import pyplot as plt
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # set dictionary size depending on the aruco marker selected
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)

    # detector parameters can be set here (List of detection parameters[3])
    parameters = aruco.DetectorParameters_create()
    parameters.adaptiveThreshConstant = 10

    # lists of ids and the corners belonging to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # font for displaying text (below)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # check if the ids list is not empty
    # if no check is added the code will crash
    if np.all(ids != None):

        # draw a square around the markers
        aruco.drawDetectedMarkers(frame, corners, ids)

        pt42 = (0,0)
        pt14 = (0,0)
        pt22 = (0,0)
        pt76 = (0,0)
        # code to show ids of the marker found
        strg = ''
        for i in range(0, ids.size):
            strg += str(ids[i][0])+', '
            #cv2.putText(frame, str(ids[i][0]), (corners[i]
            #cv2.line(frame, (0,0), (100,100), (255,0,0), 2)
            if ids[i] == 42:
                pt42 = tuple(corners[i][0][0])
            if ids[i] == 14:
                pt14 = tuple(corners[i][0][1])
            if ids[i] == 22:
                pt22 = tuple(corners[i][0][3])
            if ids[i] == 76:
                pt76 = tuple(corners[i][0][2])
            
        cv2.line(frame, pt42, pt14, (0,0,255), 2)
        cv2.line(frame, pt14, pt76, (0,0,255), 2)
        cv2.line(frame, pt76, pt22, (0,0,255), 2)
        cv2.line(frame, pt22, pt42, (0,0,255), 2)
        #print(corners[i][0][0])

        cv2.putText(frame, "Id: " + strg, (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    else:
        # code to show 'No Ids' when no markers are found
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)


    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('Aruco',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
