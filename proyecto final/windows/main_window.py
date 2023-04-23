import customtkinter 
import utils.configWindow as utl

from frames.dashboard_frame import dash_board_frame
from frames.surveillance_frame import surveillance_frame;
from frames.reports_frame import reports_frame;

class Main_window:
                    
    def __init__(self, role=""): 
        # window components    
        self.window = None;
        self.sidebar_frame = None;
        self.home_button = None;
        self.surveillance_button = None;
        self.reports_button = None;
        self.sidebar_frame_label = None;
        self.logout_button = None;
        self.main_frame = None;

        # frames
        self.dashboard_frame = None;
        self.surveillance_frame = None;
        self.reports_frame = None;

        #images
        self.background = None;
        self.app_logo = None;
        self.home_icon = None;
        self.eye_icon = None;
        self.reports_icon = None;
        self.back_icon = None;

        #role
        self.role=role;
        self.init_window();

        # self.frameBotones=None
        # self.frameCamaras=None
        # self.botonGestionCamaras=None
        # self.camara1=None
        # self.inice_antes=False
        # self.archivo_js=None
        # self.boton_reportes=None
        # self.hilo1=None
        ##self.read_camera_state=False
        # self.imagen1=None;

    def init_window(self):
        self.load_main_window();
        self.load_window_components();
        self.create_main_frame();
        self.window.mainloop();


    def load_main_window(self):
        # configuracion de la ventana
        self.window = customtkinter.CTk();                             
        self.window.title('Sistema de vigilancia inteligente - Dashboard');
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight();                                    
        self.window.geometry("%dx%d+0+0" % (w, h));
        self.window.protocol("WM_DELETE_WINDOW", self.close_window);
        self.window.config(bg='#fcfcfc');
        self.window.resizable(width=0, height=0);  

    def load_window_components(self):
        #cargar imagenes
        self.background = utl.load_image("./assets/side_bar_bg.PNG", (400, 1024));
        self.app_logo = utl.load_image("./assets/logo.png", (80, 80));
        self.home_icon = utl.load_image("./assets/home_icon.png", (40, 40));
        self.eye_icon = utl.load_image("./assets/eye_icon.png", (40, 26));
        self.reports_icon = utl.load_image("./assets/reports_icon.png", (32, 26));
        self.back_icon = utl.load_image("./assets/back_icon.png", (10, 10));

        # sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self.window, width=500);
        self.sidebar_frame.pack(side="left", fill="y")  
        background_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.background)
        background_label.place(relx=-0.05, rely=0.1)

        # cabecera del sidebar
        sidebar_header_frame = customtkinter.CTkLabel(self.sidebar_frame, bg_color= "#202088", text="", width = 250, height=100)
        sidebar_header_frame.grid(row=0, column=0);
        sidebar_frame_image_label = customtkinter.CTkLabel(sidebar_header_frame, bg_color= "#202088", image=self.app_logo);
        sidebar_frame_image_label.place(relx=-0.05, rely=0.1)
        sidebar_frame_label = customtkinter.CTkLabel(sidebar_header_frame, text="Intelligent \n surveillance", text_color= "white", bg_color= "#202088", text_font=("Inter", 18));
        sidebar_frame_label.place(relx=0.4, rely=0.15)

        # botones del sidebar
        self.home_button = customtkinter.CTkButton(
            self.sidebar_frame, 
            corner_radius=0, 
            height=50, 
            text="Home", 
            fg_color=("#282889", "lightgray"), 
            text_color="white", 
            text_font=("Inter", 12), 
            image=self.home_icon, 
            command=self.got_to_dashboard);
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.surveillance_button = customtkinter.CTkButton(
            self.sidebar_frame, 
            corner_radius=0, height=50, 
            text="Surveillance",  
            fg_color=("#202088", "lightgray") , 
            text_color="white", 
            text_font=("Inter", 12), 
            image=self.eye_icon, 
            command=self.go_to_surveillance);
        self.surveillance_button.grid(row=2, column=0, sticky="ew");

        self.reports_button = customtkinter.CTkButton(
            self.sidebar_frame, 
            corner_radius=0, 
            height=50, 
            text="Reports", 
            text_color="white",  
            fg_color=("#202088", "lightgray"), 
            text_font=("Inter", 13), 
            image=self.reports_icon,
            command=self.go_to_reports);
        self.reports_button.grid(row=3, column=0, sticky="ew")

        #sidebar footer
        self.sidebar_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text="Logged as: "+ self.role, text_color= "white", bg_color= "#202088", text_font=("Inter", 12));
        self.sidebar_frame_label.place(relx=0.2, rely=0.80)

        self.logout_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=30, text="logout", fg_color=("#FF0036", "lightgray"), text_color="white", text_font=("Inter", 12), image=self.back_icon, command=self.logout )
        self.logout_button.place(relx=0.2, rely=0.85)
    

    def create_main_frame(self):
        # dashboard frame
        self.dashboard_frame = dash_board_frame(self.window);
        self.dashboard_frame.show_frame();


    def got_to_dashboard(self):
        if(self.dashboard_frame == None):
            self.dashboard_frame = dash_board_frame(self.window);
            self.dashboard_frame.show_frame();

        if(self.surveillance_frame != None):
            self.surveillance_frame.remove_frame();
            self.surveillance_frame = None;
        
        if(self.reports_frame != None):
            self.reports_frame.remove_frame();
            self.reports_frame = None;            

    def go_to_surveillance(self):
        if(self.dashboard_frame != None):
            self.dashboard_frame.remove_frame();
            self.dashboard_frame = None;
        
        if(self.surveillance_frame == None):
            self.surveillance_frame = surveillance_frame(self.window);
            self.surveillance_frame.show_frame();
            self.surveillance_frame.initialize_image_analisis();

        if(self.reports_frame != None):
            self.reports_frame.remove_frame();
            self.reports_frame = None;            

        #self.dashboard_frame = None;
        #self.surveillance_frame = None;
        #self.reports_frame = None;
        print(self.dashboard_frame);

        ##print(self.dashboard_frame.winfo_exists());

    def go_to_reports(self):
        if(self.surveillance_frame != None):
            self.surveillance_frame.remove_frame();
            self.surveillance_frame = None;
        
        if(self.dashboard_frame != None):
            self.dashboard_frame.remove_frame();
            self.dashboard_frame = None; 

        if(self.reports_frame == None):
            self.reports_frame = reports_frame(self.window);
            self.reports_frame.show_frame();         


        
    def close_window(self, event=0):
        print("cerrado")
        #self.read_camera_state=True
        self.window.destroy()

    def logout(self):
        self.window.destroy();
        self.role="";

   