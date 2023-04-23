import cv2;

def get_conected_cameras():
    cameras_list = [];
    camera_1 = cv2.VideoCapture(0);

    try:
        cam_1_conectada = camera_1.read();
    except: 
        pass

    if(cam_1_conectada):
        cameras_list.append("camera_1");

    return(cameras_list);