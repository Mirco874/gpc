from turtle import width
import customtkinter 
import utils.configWindow as utl
from PIL import Image, ImageTk
import cv2
import imutils

class Surveillance:
                    
    def __init__(self, role=""):
        self.role=role;       
        self.window = customtkinter.CTk();                            
        self.window.title('Intelligent surveillance - Surveillance');
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight();                                    
        self.window.geometry("%dx%d+0+0" % (w, h));
        self.window.config(bg='#fcfcfc');
        self.window.resizable(width=0, height=0); 
        

        #images
        background = utl.load_image("./assets/side_bar_bg.PNG", (400, 1024));
        app_logo = utl.load_image("./assets/logo.png", (80, 80));
        home_icon = utl.load_image("./assets/home_icon.png", (40, 40));
        eye_icon = utl.load_image("./assets/eye_icon.png", (40, 26));
        reports_icon = utl.load_image("./assets/reports_icon.png", (32, 26));
        back_icon = utl.load_image("./assets/back_icon.png", (10, 10));

        #side bar
        sidebar_frame = customtkinter.CTkFrame(self.window, width=500);
        sidebar_frame.pack(side="left", fill="y")  

        background_label = customtkinter.CTkLabel(sidebar_frame, image=background)
        background_label.place(relx=-0.05, rely=0.1)

        # sidebar header
        sidebar_header_frame = customtkinter.CTkLabel(sidebar_frame, bg_color= "#202088", text="", width = 250, height=100)
        sidebar_header_frame.grid(row=0, column=0);

        sidebar_frame_image_label = customtkinter.CTkLabel(sidebar_header_frame, bg_color= "#202088", image=app_logo);
        sidebar_frame_image_label.place(relx=-0.05, rely=0.1)

        sidebar_frame_label = customtkinter.CTkLabel(sidebar_header_frame, text="Intelligent \n surveillance", text_color= "white", bg_color= "#202088", text_font=("Inter", 18));
        sidebar_frame_label.place(relx=0.4, rely=0.15)

        #sidebar buttons
        home_button = customtkinter.CTkButton(sidebar_frame, corner_radius=0, height=50, text="Home", fg_color=("#282889", "lightgray"), text_color="white", text_font=("Inter", 12), image=home_icon )
        home_button.grid(row=1, column=0, sticky="ew")

        surveillance_button = customtkinter.CTkButton(sidebar_frame, corner_radius=0, height=50, text="Surveillance",  fg_color=("#202088", "lightgray") , text_color="white", text_font=("Inter", 12), image=eye_icon )
        surveillance_button.grid(row=2, column=0, sticky="ew")

        reports_button = customtkinter.CTkButton(sidebar_frame, corner_radius=0, height=50, text="Reports", text_color="white",  fg_color=("#202088", "lightgray") , text_font=("Inter", 13), image=reports_icon)
        reports_button.grid(row=3, column=0, sticky="ew")

        #sidebar footer
        sidebar_frame_label = customtkinter.CTkLabel(sidebar_frame, text="Logged as: "+ self.role, text_color= "white", bg_color= "#202088", text_font=("Inter", 12));
        sidebar_frame_label.place(relx=0.2, rely=0.80)

        logout_button = customtkinter.CTkButton(sidebar_frame, corner_radius=0, height=30, text="logout", fg_color=("#FF0036", "lightgray"), text_color="white", text_font=("Inter", 12), image=back_icon, command=self.logout )
        logout_button.place(relx=0.2, rely=0.85)

        self.createMainFrame();
        self.window.mainloop()
    
    def createMainFrame(self):
       
        main_frame = customtkinter.CTkFrame(self.window, fg_color=("white", "black"))
        main_frame.pack(side="right", fill="both", expand=True)
        
        load_image_btn = customtkinter.CTkButton(main_frame, corner_radius=10, height=30, text="Load image from camera", fg_color=("#202088", "lightgray"), text_color="white", text_font=("Inter", 12), command=self.load_image_from_camera)
        load_image_btn.place(relx=0.3, rely=0.1)

        remove_image_btn = customtkinter.CTkButton(main_frame, corner_radius=10, height=30, text="Remove image from camera", fg_color=("#202088", "lightgray"), text_color="white", text_font=("Inter", 12), command=self.end)
        remove_image_btn.place(relx=0.5, rely=0.1)

        self.video_label=customtkinter.CTkLabel(main_frame, fg_color=("black", "lightgray"), width=640,height=480 )
        self.video_label.place(relx=0.2, rely=0.2)

    def logout(self):
        self.window.destroy();
        self.role="";


    def load_image_from_camera(self):
        global video;
        video = cv2.VideoCapture(0);
        self.start();
    
    def start(self):
        global video;
        ret, frame = video.read()
        if( ret == True):
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image=img)
            self.video_label.configure(image=image);
            self.video_label.image=image;
            self.video_label.after(10,self.start)

    def end(self):
        global video
        video.release();
        self.video_label.image="";
        