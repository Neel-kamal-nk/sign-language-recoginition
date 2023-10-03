import os
import pickle
'''pickle is a module in Python used for serializing and deserializing Python objects. 
It allows you to convert complex data structures, such as
 lists and dictionaries, into a byte stream that can be easily saved to a file or transmitted over a network'''

import mediapipe as mp
'''MediaPipe is a framework for building multimodal (eg. video, audio, any time series data), 
cross platform (i.e Android, iOS, web, edge devices) applied ML pipelines.
    It consists of a growing set of ML solutions developed by Google Research that enable developers and
        researchers to build pipelines and
        understand their data.'''
import cv2

mp_hands = mp.solutions.hands
'''This line essentially imports and assigns the hands module from the mediapipe library to the variable mp_hands. 
This module is responsible for hand tracking and landmark detection using the MediaPipe framework.'''
#mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
#used to create an instance of the Hands class from the mediapipe library
DATA_DIR = "C://Users//neelk//Vs Code//data"

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

            data.append(data_aux)
            labels.append(dir_)

f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
