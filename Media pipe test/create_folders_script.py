import os;
import numpy as np;

DATA_PATH = os.path.join('TRAIN_DATA'); 
detections = np.array(['robo', 'pelea'])
number_of_train_videos = 30
number_of_frames_per_video = 30

for detection in detections: 
    for video in range(number_of_train_videos):
        try: 
            #TRAIN_DATA/robo/0
            #TRAIN_DATA/robo/1
            os.makedirs(os.path.join(DATA_PATH, detection, str(video)))
        except:
            pass

