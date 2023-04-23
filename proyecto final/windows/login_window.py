import tkinter as tk
from tkinter import ttk;
import utils.configWindow as utl
from windows.main_window import Main_window

class Login_window():

    def __init__(self):
        self.window = tk.Tk();
        self.window.title("Intelligent surveillance - login");
        self.window.geometry("800x500");
        self.window.config(bg= "#fcfcfc")
        self.window.resizable(width= 0, height= 0);
        utl.centerWindow(self.window, 800, 500);
        
        logo= utl.load_image("./assets/logo.png", (200, 200))
        
        #frame_logo
        frame_logo =tk.Frame(self.window, bd= 0, width= 300, relief= tk.SOLID, padx= 10, pady= 10, bg= "#191970" );
        frame_logo.pack(side= "left", expand= tk.YES, fill= tk.BOTH);
        label = tk.Label(frame_logo, image= logo, bg= "#191970");
        label.place(x= 0, y= 0, relwidth= 1, relheight= 1);
        
        #frame_form
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg="#fcfcfc");
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH);

        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="black");
        frame_form_top.pack(side="top",fill=tk.X);
        title = tk.Label(frame_form_top, text="Intelligent \n surveillance", font=("Inter", 30), fg="#666a88", bg="#fcfcfc", pady=50);
        title.pack(expand=tk.YES, fill=tk.BOTH);

        #frame_form_content
        frame_form_content = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc");
        frame_form_content.pack(side="bottom", expand=tk.YES, fill=tk.BOTH);

        email_label = tk.Label( frame_form_content, text="Email*: ",font=("Inter", 12), fg="#666a88", bg= "#fcfcfc", anchor="w");
        email_label.pack(fill=tk.X, padx=20, pady=5);
        self.email = ttk.Entry(frame_form_content, font=("Inter", 12));
        self.email.pack(fill=tk.X, padx=20, pady=10);

        password_label = tk.Label( frame_form_content, text="Password*: ",font=("Inter", 12), fg="#666a88", bg= "#fcfcfc", anchor="w");
        password_label.pack(fill=tk.X, padx=20, pady=5);
        self.password = ttk.Entry(frame_form_content, font=("Inter", 12));
        self.password.pack(fill=tk.X, padx=20, pady=10);
        self.password.config(show="*");

        login_btn = tk.Button(frame_form_content, text="Login", font=('Inter', 12), bg='#3a7ff6', bd=0, fg="#fff", command=self.login)
        login_btn.pack(fill=tk.X, padx=20, pady=10)
        #login_btn.bind("<Return>", (lambda event: self.login()))

        register_btn = tk.Button(frame_form_content, text="Create account", font=('Inter', 12), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.register)
        register_btn.pack(fill=tk.X, padx=20, pady=10)
        #register_btn.bind("<Return>", (lambda event: self.register()))

        enter_as_guest_btn = tk.Button(frame_form_content, text="Enter as guest", font=('Inter', 12), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.EnterAsGuest)
        enter_as_guest_btn.pack(fill=tk.X, padx=20, pady=10)

        self.window.mainloop();

    def login(self):
        print('login....')

    def register(self):
        print('register....')

    def EnterAsGuest(self):
        self.window.destroy();
        Main_window(role="guest");
        

