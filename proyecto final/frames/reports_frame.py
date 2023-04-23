from tkinter import Label
import customtkinter;
from utils.manage_reports import get_reports, delete_report
from PIL import ImageTk,Image

class reports_frame():

    def __init__(self, window):
        self.window = window;
        self.main_frame = None;
        self.titulo = None;
        self.reports_data = None;
        self.reports_frame = None;

        ##self.ventana.title("reportes")

    def show_frame(self):
        self.main_frame = customtkinter.CTkFrame(self.window, fg_color=("white", "white"));

        self.titulo = customtkinter.CTkLabel(self.main_frame, text="Reportes", text_font=("Inter", 18));
        self.titulo.place(relx=0.01, rely=0.01);
        self.load_reports();

        self.main_frame.pack(side="right", fill="both", expand=True);

    def remove_frame(self):
        self.main_frame.destroy();

    def load_reports(self):

        self.reports_frame = customtkinter.CTkFrame(self.main_frame, fg_color=("white", "white"));
        self.reports_frame.place(relx=0.01, rely=0.05);

        self.reports_data = get_reports();

        i = 1;

        for report in self.reports_data:
            report_record=""
            report_record+="camera: "+self.reports_data[report]["camera"]
            report_record+="\n location: "+self.reports_data[report]["location"]
            report_record+="\n timestamp: "+self.reports_data[report]["timestamp"]            
            report_record+="\n detection: "+self.reports_data[report]["detection"]
            report_record+="\n image_route:"+"./data/images/"+self.reports_data[report]["image_name"]
            report_record+="\n"

            self.show_report(
                record=report_record,
                row=i, 
                image_route="./data/images/"+self.reports_data[report]["image_name"],
                report_id=report );

            i += 1;
        

    def show_report(self, record, row, image_route, report_id):
        report_frame = customtkinter.CTkFrame(self.reports_frame, fg_color=("white", "white"));
        report_label = customtkinter.CTkLabel(report_frame, text=record);
        
        image_report = ImageTk.PhotoImage(Image.open(image_route).resize((200,200)));
        label_image_report=Label(report_frame, text=image_route, bg="#E6DAD7")


        remove_report_btn = customtkinter.CTkButton(
            master = report_frame,
            text = "Eliminar reporte",
            command = lambda: self.delete_report(report_id),
            fg_color = ("red", "red"))


        remove_report_btn.grid(column=1,row=1)
        report_label.grid(column=0,row=0)
        label_image_report.grid(column=1,row=0)
        report_frame.grid(column=0,row=row)

    def close(self):
        self.main_frame.destroy();
    
    def delete_report(self, report_id):
        delete_report(report_id);
        self.close();
        self.init_frame();
