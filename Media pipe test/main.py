import cv2
import mediapipe as mp
import time
import numpy as np


pose_detector_model = mp.solutions.pose
pose = pose_detector_model.Pose();

cap = cv2.VideoCapture(1);
prediction_time = 0;

while True:
    # captura de la imagen
    sucesss, image = cap.read();
    # conversion al formato RGB
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB);
    #obtencion de la prediccion
    results = pose.process(imgRGB);
    if(results.pose_landmarks):
        # si existe alguna deteccion, agregala a la imagen BGR obtenida por la camara
        mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, pose_detector_model.POSE_CONNECTIONS)
        # de todas las marcas de una deteccion recuperar 

        pose_landmarks = [];
        # recuperar las 33 marcas 
        for result in results.pose_landmarks.landmark:
            # de cada marca recuperar sus coordenadas
            # flatten convierte el arrego (33,4) a (132,)
            land_mark = np.array([result.x, result.y, result.z, result.visibility]).flatten();
            pose_landmarks.append(land_mark);
        



            

    current_time = time.time();
    fps = 1/(current_time - prediction_time);
    prediction_time = current_time;

    cv2.putText(image, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3 );
    cv2.imshow("Image", image);
    key = cv2.waitKey(1)
    if key == 27:
        break

#[[132],[132],...,[132]]
#132 = 33 * 4 =   132
# the length of pose_landmark array will be 33, like results.pose_landmarks.landmark
# [[x,y,z,v],[x,y,z,v],....]



cap.release()
cv2.destroyAllWindows()