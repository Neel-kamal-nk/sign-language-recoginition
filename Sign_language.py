import os
#os is used for handling file and directory operations.
import cv2
#cv2 is used for reading ,writing and showing images.
''' It provides a wide range of tools and functions for image and video analysis, 
including image processing, computer vision algorithms, and machine learning integration. '''


DATA_DIR = "C://Users//neelk//Vs Code//data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 5
#Number of data
dataset_size = 110 #the number of images you want to collect for each class

cap = cv2.VideoCapture(0) #This line initializes video capture from the default camera (camera with index 0).
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    #done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
    '''cv2.FONT_HERSHEY_SIMPLEX: This argument specifies the font type for the text. In this case,
    cv2.FONT_HERSHEY_SIMPLEX represents a simple font type that is easy to read.
    1.3: This argument specifies the font scale factor. It determines the size of the text.
    A value of 1.3 means the text will be 1.3 times the default font size.
    (0, 255, 0): This argument specifies the color of the text using the BGR (Blue, Green, Red) color format. 
    In this case, (0, 255, 0) corresponds to green, so the text will be displayed in green.
    3: This argument specifies the thickness of the lines used to draw the text.
    A thickness of 3 means the text will have relatively thick lines.
    cv2.LINE_AA: This argument specifies the type of line used for drawing the text. cv2.
    LINE_AA stands for anti-aliased lines, which helps improve the appearance of the text by smoothing the edges.'''
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

'''This loop continuously captures video frames from the webcam, saves them as JPEG images in the  
respective class folder (e.g., "0.jpg", "1.jpg", etc.), and increments the counter until the desired 
dataset_size is reached.'''

cap.release()
cv2.destroyAllWindows()
'''These lines release the webcam resource and close any OpenCV windows
 that were opened during the data collection process.'''