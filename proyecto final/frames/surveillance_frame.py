import argparse
from datetime import datetime
import os
import sys
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn


from PIL import Image, ImageTk;

from utils.common import DetectMultiBackend;

from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.manage_reports import add_report
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync

from tkinter import Label;
import customtkinter;
import time;
import utils.configWindow as utl;
from utils.camera_status import load_all_cameras_state;
from  windows.management_camera_window import Management_camera_window;
import threading;
from utils.alert import sound_alert;

class surveillance_frame():

    def __init__(self, window):
        self.window = window;
        self.main_frame = None;
        self.manage_cameras_btn = None;
        self.frame_title = None;

        self.no_cameras_connected_frame = None;
        self.no_cameras_connected_label = None;

        self.thread1 = None;
        self.thread2 = None;

        self.camera_image_label = None;
        self.isInit = False;
        self.loading_camera_image = True;
        
    def show_frame(self):
        self.main_frame = customtkinter.CTkFrame(self.window, fg_color=("white", "white"));
        self.main_frame.pack(side="right", fill="both", expand=True);

        self.frame_title = customtkinter.CTkLabel(self.main_frame, text="Vigilancia", text_font=("Inter", 18));
        self.frame_title.place(relx=0.01, rely=0.01);

        self.camera_image_label=Label(self.main_frame, bg="black");

        conection_state = load_all_cameras_state();
        if (conection_state["camera_1"]["state"] == "disconnected"):
            self.show_no_cameras_connected_frame();
        
        
    def initialize_image_analisis(self):
        print("inicio del hilo 1");
        self.thread1 = threading.Thread(name="load_cameras_state", target=self.load_cameras_state)
        self.thread1.start() 


    def remove_frame(self):
        self.main_frame.destroy();

    def show_no_cameras_connected_frame(self):
        self.no_cameras_connected_frame = customtkinter.CTkFrame(
            self.main_frame, 
            width=600,
            height=600);
   
        self.no_cameras_connected_label = customtkinter.CTkLabel(
            self.no_cameras_connected_frame, 
            bg_color=("white","white"), 
            width=500,
            height=400,
            text="No se detectaron camaras conectadas",
            text_font=("Inter", 16)
            );

        self.manage_cameras_btn = customtkinter.CTkButton(self.no_cameras_connected_frame, 
            text="Agregar camara", 
            height=40,
            fg_color=("#4763E4", "#4763E4"),
            text_color=("white", "white"),
            command=Management_camera_window,
            text_font=("Inter", 12));

        self.no_cameras_connected_frame.place(relx=0.3, rely=0.1);
        self.no_cameras_connected_label.pack();
        self.manage_cameras_btn.place(relx=0.35, rely=0.6)

    def hide_no_cameras_connected_frame(self):
        self.no_cameras_connected_frame.destroy();
        self.no_cameras_connected_label.destroy();
        self.manage_cameras_btn.destroy();

    def show_camera1_image(self):
        print("asd");

    def remove_camera1_image(self):
        print("removing");

    def close(self):
        self.loading_camera_image = False;
        self.main_frame.destroy();



    def load_cameras_state(self):
        print("cargando estado de las camaras");
        while True:
            time.sleep(1);
            conection_state = load_all_cameras_state();

            if (conection_state["camera_1"]["state"] == "connected"):

                if not(self.isInit):
                    #######################
                    self.no_cameras_connected_frame.destroy();
                    self.camera_image_label.place(relx=0.3, rely=0.1);
                    ################
                    self.isInit = True;
                    ##crear el hilo para ejecutar el programa principal
                    self.thread2 = threading.Thread(name="processing_camera_image", target=self.processing_camera_image);
                    self.thread2.start();
            else:
                ####################
                self.isInit = False;

            if not(self.loading_camera_image):
                self.show_no_cameras_connected_frame();
                print("fin hilo1")
                break
            
            time.sleep(2) 


    def processing_camera_image(self):
        print("procesando imagen");
        print("volviendo a cargar modelo.....");
        weights='./assets/models/modelo_entrenado.pt';  
        source=0 
        imgsz=320  
        conf_thres=0.25  
        iou_thres=0.45  # NMS IOU threshold
        max_det=1000  # maximum detections per image
        device=""   # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False 
        save_txt=False  
        save_conf=False  
        save_crop=False 
        nosave=False  
        classes=None  
        agnostic_nms=False  
        augment=False 
        visualize=False 
        update=False  
        project='runs/detect'  
        name='exp' 
        exist_ok=False  
        line_thickness=3 
        hide_labels=False  
        hide_conf=False  
        half=False 
        dnn=False  
        
        source = str(0)
        save_img = not nosave and not source.endswith('.txt')
        is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
        webcam = source.isnumeric() or source.endswith('.txt') or (is_url and not is_file)

        device = select_device(device)
        model = DetectMultiBackend(weights, device=device, dnn=dnn)
        stride, names, pt, jit, onnx = model.stride, model.names, model.pt, model.jit, model.onnx
        imgsz = check_img_size(imgsz, s=stride)  #tam imag modelo

        # Lectura de datos
        if webcam:
            view_img = check_imshow()
            cudnn.benchmark = True  # aumentar la velocidad de lectura de iamgenes 
            dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt and not jit)
            bs = len(dataset)  # tamaño del lote

        # ejecucion de la funcion de prediccion.
        #valores iniciales de 
        #calculo de los frames
        dt, seen = [0.0, 0.0, 0.0], 0

        new_prediction="";

        for path, im, im0s, vid_cap, s in dataset:
            visualize = False
            time.sleep(1)
            conection_state = load_all_cameras_state();

            if (conection_state["camera_1"]["state"]=="connected"):
                t1 = time_sync()
                im = torch.from_numpy(im).to(device) #obtener la imagen de la camara
                im = im.half() if half else im.float() #normalizar imagen entre 0 y 1 considerando los valores flotantes
                im /= 255 
                t2 = time_sync()
                dt[0] += t2 - t1

                
                pred = model(im, augment=augment, visualize=visualize)
                t3 = time_sync()
                dt[1] += t3 - t2

                # NMS
                pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
                dt[2] += time_sync() - t3

                # obtencion de la imagen dibujada
                #de cada prdiccion del dataset realizar una prediccion y contar el numero de imagenes analizadas
                for i, det in enumerate(pred):  
                    seen += 1
                    if webcam:  # tamaño de lote >= 1
                        p, im0, frame = path[i], im0s[i].copy(), dataset.count 
                    else:
                        p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
                    p = Path(p) 
                
                    #   
                    gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                
                    annotator = Annotator(im0, line_width=line_thickness, example=str(names))
                    if len(det):
                        # rescalar boxes de la img_size para el tamaño im0 si hay una diferencia. 
                        det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                        # imprimir resultados
                        for c in det[:, -1].unique():# de todas las predicciones sin repetir  
                            s += f"{names[int(c)]}"+" "  # numero de detecciones por clases

                        #para escribir los resultados, los puntos obtenidos deben ser normalizados
                        for *xyxy, conf, cls in reversed(det):
                            #si se almacena la imagen o hay imagen que visualizar se escribe 
                            if save_img or save_crop or view_img:  # Add bbox to image
                                c = int(cls)  # integer class
                                label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                                annotator.box_label(xyxy, label, color=colors(c, True))

                    timestamp = str(datetime.now().strftime('%d/%m/%Y %H:%M:%S'));

                    image_name = str(datetime.now().strftime('%d%m%Y_%H%M%S'));

                    if view_img:
                        im0=cv2.cvtColor(im0,cv2.COLOR_BGR2RGB)
                
                        im0 = cv2.putText(
                            im0,
                            conection_state["camera_1"]["name"],
                            (20, 40),
                            cv2.FONT_HERSHEY_TRIPLEX,
                            1,
                            color = (0,0,0),
                            thickness = 2);
                        
                        im0 = cv2.putText(
                            im0,
                            timestamp,
                            (200,40),
                            cv2.FONT_HERSHEY_TRIPLEX,
                            1,
                            color = (0,0,0),
                            thickness = 1);
        
                        im = Image.fromarray(im0);
                        img=ImageTk.PhotoImage(image=im)
                        ####################################################
                        self.camera_image_label.configure(image=img)
                        
                    if(new_prediction != s):
                        new_prediction = s
                        if (s != "" and s != " "):

                            add_report(camera="camera_1",
                                            location=conection_state["camera_1"]["name"],
                                            timestamp=timestamp,
                                            detection= new_prediction,
                                            image=conection_state["camera_1"]["name"]+"_"+i+".png"
                                            )


                            cv2.imwrite("./data/images/"+conection_state["camera_1"]["name"]+"_"+image_name+".png", im0);
                            sound_alert();
                            print(s)
                                        
        
            else:
                dataset.cap.release()
                dataset = None
                print("fin de hilo 2")
                break

