from cgitb import text
import customtkinter;
import utils.configWindow as utl;
from  windows.management_camera_window import Management_camera_window;

class dash_board_frame():

    def __init__(self, window):
        self.window = window;
        self.main_frame = None;
        self.frame_title = None;

    def show_frame(self):
        self.main_frame = customtkinter.CTkFrame(self.window, fg_color=("white", "white"));
        self.main_frame.pack(side="right", fill="both", expand=True);
        self.frame_title = customtkinter.CTkLabel(self.main_frame, text="Dashboard", text_font=("Inter", 18));
        self.frame_title.place(relx=0.01, rely=0.01);
        self.show_metrics();

    def show_metrics(self):
        print("showing metrics...");

    def remove_frame(self):
        self.main_frame.destroy();