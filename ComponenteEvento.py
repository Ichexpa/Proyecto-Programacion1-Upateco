import tkinter as tk
from tkinter import ttk
from Evento import Evento;

class ComponenteEvento(tk.Frame):
    colorDeFondo = "#BFDFB2"
    labelsCortos="consolas 14 bold";
    labelsLargos="consolas 14 bold";
    entrys="consolas 14 bold";
    colorBotones = "#62CFA4";
    def __init__(self, padre):
        super().__init__(padre)
        self.titulo=tk.StringVar();
        self.fecha=tk.StringVar();
        self.hora=tk.StringVar();
        self.duracion=tk.IntVar(value=1);
        #self.descipcion=tk.StringVar();
        self.importancia=tk.BooleanVar();
        self.fechaRecordatorio=tk.StringVar();
        self.horaRecordatorio=tk.StringVar();
        self.identificadorEvento=tk.StringVar();
        self.contenedorForm=tk.LabelFrame(self,text="Agregar nuevo Evento",font=self.labelsLargos,padx=30,pady=30);
        self.contenedorForm.grid(row=0, column=0,padx=10,pady=10);
        tk.Label(self.contenedorForm, text="Titulo", font=self.labelsCortos,bg=self.colorDeFondo).grid(row=0, column=0)
        tk.Entry(self.contenedorForm, textvariable=self.titulo, font=self.entrys, justify="center").grid(
            row=0, column=1, columnspan=3, sticky="we");
        tk.Label(self.contenedorForm, text="Fecha",
                 font=self.labelsCortos).grid(row=1, column=0)
        tk.Entry(self.contenedorForm, textvariable=self.fecha,
                 font=self.entrys, justify="center").grid(row=1, column=1)
        tk.Label(self.contenedorForm, text="Hora", font=self.labelsCortos).grid(
            row=1, column=2, ipadx=5, ipady=5)
        tk.Entry(self.contenedorForm, textvariable=self.hora, font=self.entrys, justify="center").grid(
            row=1, column=3, padx=5, pady=5, sticky="we")
        tk.Label(self.contenedorForm, text="Duracion", font=self.labelsCortos).grid(
            row=2, column=0,padx=5,pady=5);
        tk.Entry(self.contenedorForm, textvariable=self.duracion, font=self.entrys, justify="center").grid(
            row=2, column=1)
        tk.Label(self.contenedorForm, text="Importante", font=self.labelsCortos).grid(
            row=2, column=2, padx=10, pady=10)
        tk.Checkbutton(self.contenedorForm, variable=self.importancia, font=self.labelsCortos, bg=ComponenteEvento.colorDeFondo).grid(
            row=2, column=3)
        tk.Label(self.contenedorForm, text="Fecha de Recordatorio", font=self.labelsLargos).grid(
            row=3, column=0,columnspan=2, ipadx=5);
        tk.Label(self.contenedorForm, text="Hora de Recordatorio", font=self.labelsLargos).grid(
            row=3, column=2, columnspan=2,ipadx=5);
        tk.Entry(self.contenedorForm, textvariable=self.fechaRecordatorio,
                 font=self.entrys, justify="center").grid(row=4, column=0, columnspan=2);
        tk.Entry(self.contenedorForm, textvariable=self.horaRecordatorio,font=self.entrys, justify="center").grid(
            row=4, column=2, columnspan=2)
        tk.Label(self.contenedorForm, text="Identificar Evento como", font=self.labelsLargos).grid(
            row=5, column=0,columnspan=2,pady=10)
        tk.Entry(self.contenedorForm, textvariable=self.identificadorEvento,font=self.entrys, justify="center").grid(
            row=5, column=2, columnspan=2, sticky="we",pady=10)
        tk.Label(self.contenedorForm,text="Descripción",font=self.labelsCortos).grid(row=6,column=0,columnspan=4,pady=5);
        self.descripcion = tk.Text(
            self.contenedorForm, font=self.entrys,height=5,width=60);
        self.descripcion.grid(row=7, column=0, columnspan=4,padx=5,pady=5);
        tk.Button(self.contenedorForm, text="Agregar Evento", command=self.setEvento,
                  padx=5, pady=5,font=self.labelsCortos,bg=self.colorBotones).grid(row=8,column=0, columnspan=4, sticky="snew");
    def setEvento(self):
        self.evento=Evento(self.titulo.get(),
                      self.fecha.get(),
                      self.hora.get(),
                      self.duracion.get(),
                      self.descripcion.get("1.0", 'end-1c'),
                      self.fechaRecordatorio.get(),
                      self.horaRecordatorio.get(),
                      self.identificadorEvento.get(),
                      self.importancia.get());
        print(f"{self.importancia.get()} Descripcion {self.descripcion.get('1.0', 'end-1c')}")

    def getEvento(self):
        return self.evento;


app = ComponenteEvento(tk.Tk())
app.grid();

app.mainloop();
