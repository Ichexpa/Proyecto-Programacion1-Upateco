import tkinter as tk
from tkinter import ttk


class VentanaDetalleEvento(tk.Frame):
    titulosEvento = "consolas 14 bold"
    informacionEvento="consolas 12";
    def __init__(self, padre,evento):
        super().__init__(padre);
        self.ventana=tk.Toplevel(padre,padx=20,pady=20);
        self.ventana.title(evento[0]);
        #self.ventana.geometry("500x500")
        self.grid();
        tk.Label(self.ventana,text="Titulo",font=self.titulosEvento).grid(row=0,column=0);
        tk.Label(self.ventana,text=evento[0],font=self.informacionEvento).grid(row=0,column=1);
        tk.Label(self.ventana,text="Fecha",font=self.titulosEvento).grid(row=1,column=0);
        tk.Label(self.ventana,text=evento[1],font=self.informacionEvento).grid(row=1,column=1);
        tk.Label(self.ventana,text="Hora",font=self.titulosEvento).grid(row=2,column=0);
        tk.Label(self.ventana,text=evento[2],font=self.informacionEvento).grid(row=2,column=1);
        tk.Label(self.ventana,text="Duracion",font=self.titulosEvento).grid(row=3,column=0);
        tk.Label(self.ventana,text=evento[3],font=self.informacionEvento).grid(row=3,column=1);
        tk.Label(self.ventana, text="Importante",font=self.titulosEvento).grid(row=4, column=0)
        tk.Label(self.ventana, text=evento[5], font=self.informacionEvento).grid(row=4, column=1)
        tk.Label(self.ventana,text="Descripción",font=self.titulosEvento).grid(row=5,column=0,columnspan=2);
        tk.Label(self.ventana,text=evento[4],font=self.informacionEvento).grid(row=6,column=0,columnspan=2);
        #tk.Label(self.ventana,text=evento[1]).grid();


