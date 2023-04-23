from tkinter import *
from utils.camera_status import activate_camera;
from vista.ventana_gestionar_camaras import *

class connect_camera_window:
    def __init__(self):
        self.listaCamaras=[]
        self.ventana=Tk()
        self.ventana.title("Cámaras")
        self.titulo=Label(self.ventana,text="Agregar cámara")
        self.labelNombre=Label(self.ventana,text="Nombre: ")

        self.espacioNombre=Entry(self.ventana)
        self.botonAceptar=Button(self.ventana,text="Aceptar",command=self.registrar_camara)
        self.botonCancelar=Button(self.ventana,text="Cancelar")

        self.variable = StringVar(self.ventana)
        self.variable.set("seleccione una camara") 
        self.menuOpciones = OptionMenu(self.ventana, self.variable,"camara 1")

        self.titulo.grid(row=0,column=1)
        self.labelNombre.grid(row=1,column=0)
        self.espacioNombre.grid(row=1,column=1)
        self.menuOpciones.grid(row=2,column=1)
        self.botonAceptar.grid(row=3,column=1)
        self.botonCancelar.grid(row=3,column=3)
        self.ventana.mainloop()

    def registrar_camara(self):
        nombre=self.espacioNombre.get()
        modelo="camara 1"
        activar_camara(nombre=nombre,modelo=modelo,numero_slot=1)
        ventana_gestionar_camaras.iniciar_componentes()