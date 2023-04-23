
from tkinter import Label, OptionMenu, StringVar
from tkinter.ttk import LabelFrame
import customtkinter;
from utils.devices import get_conected_cameras;
from utils.camera_status import *;

class Management_camera_window():

    def __init__(self):
        self.window=customtkinter.CTk();
        self.window.geometry("350x350");

        self.title = Label(self.window,text="Administrar cámara.");
        self.title.grid(row=0, column=2);

        self.cameras_frame = LabelFrame(self.window);
        self.cameras_frame.config(width=600, height=450);
        self.cameras_frame.grid(row=2, column=2);

        self.init_components()
        self.window.mainloop();


    def init_components(self):
        self.cameras_list = get_conected_cameras();
        self.cameras_json=load_all_cameras_state();

        self.camera1_name = customtkinter.CTkLabel(master=self.cameras_frame, text=self.cameras_json["camera_1"]["name"]);
        self.camera1_state = customtkinter.CTkLabel(master=self.cameras_frame, text=self.cameras_json["camera_1"]["state"]);
        self.camera1_model = customtkinter.CTkLabel(master=self.cameras_frame, text=self.cameras_json["camera_1"]["model"]);

        self.init_selection_menu();

        
    def init_selection_menu(self):
        self.camera1_name_field = customtkinter.CTkEntry(self.cameras_frame);

        self.selected_option = StringVar(self.cameras_frame);
        
        self.selected_option.set(self.cameras_list[0]);
        
        self.menu1 = OptionMenu(self.cameras_frame, self.selected_option, *self.cameras_list); 

        self.edit_btn1 = customtkinter.CTkButton(self.cameras_frame, text="Editar", command=self.open_editor, fg_color=("#5AF06C", "#5AF06C"));
        self.delete_btn1 = customtkinter.CTkButton(self.cameras_frame, text="Eliminar", command=self.remove_camera, fg_color=("red", "red"));

        self.save_changes_btn1 = customtkinter.CTkButton(self.cameras_frame, text="Aceptar Cambios", command=self.update_window, fg_color=("#5AF06C", "#5AF06C"));
        self.cancel_btn1 = customtkinter.CTkButton(self.cameras_frame, text="Cancelar", command=self.close_editor, fg_color=("red", "red"));

        self.camera1_name.grid(row=2,column=0)
        self.camera1_state.grid(row=3,column=0)
        self.camera1_model.grid(row=4,column=0)

        self.edit_btn1.grid(row=5,column=0)
        self.delete_btn1.grid(row=5,column=1)


    def close_editor(self):
        self.camera1_name_field.destroy();
        self.menu1.destroy();
        self.save_changes_btn1.destroy();
        self.cancel_btn1.destroy();
        self.init_components();

    def open_editor(self):
        self.camera1_name.destroy();
        self.camera1_model.destroy();
        self.camera1_state.destroy();
        self.edit_btn1.destroy();
        self.delete_btn1.destroy();
        self.camera1_name_field.grid(row=2,column=0)
        self.menu1.grid(row=4,column=0)
        self.save_changes_btn1.grid(row=5,column=0)
        self.cancel_btn1.grid(row=5,column=1)

    def remove_camera(self):
        self.camera1_name.destroy();
        self.camera1_model.destroy();
        self.camera1_state.destroy();
        self.edit_btn1.destroy();
        self.delete_btn1.destroy();

        disable_camera("camera_1");
        self.init_components();

    def update_window(self):
        name = self.camera1_name_field.get();
        model = self.selected_option.get();
        print(name)
        print(model)
        activate_camera(name, model, camera="camera_1");
        self.close_editor();


