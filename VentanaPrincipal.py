import tkinter as tk
from tkinter import ttk,messagebox
from ComponenteEvento import ComponenteEvento;
from TablaDeEventos import TablaDeEventos;
from ManejadorJson import ManejadorJson;
from AdministradorDeFechas import AdministradorDeFechas
class VentanaPrincipal(tk.Frame):
    fuenteBotones="consoles 13 bold";
    def __init__(self,padre):
        super().__init__(padre);
        self.padre=padre;
        self.manejadorJson=ManejadorJson("eventos.json");
        self.tablaDeEventos=TablaDeEventos(self,self.manejadorJson);
        self.tablaDeEventos.grid(row=0,column=1);
        self.componenteEvento = ComponenteEvento(self, self.tablaDeEventos,self.manejadorJson)
        self.componenteEvento.grid(row=0, column=0)
        #Tengo pensado que los botones y sus funcionalidades tengan una clase aparte
        self.botonEditar=tk.Button(self.tablaDeEventos,text="Editar",font=self.fuenteBotones,bg="#43DFAD");
        self.botonEditar.bind("<Button-1>",lambda e: self.boton_presionado(self.seleccionarEventoAEditar))
        self.botonEditar.grid(row=3,column=2,sticky="we",padx=5,pady=5);
        self.botonEliminar = tk.Button(self.tablaDeEventos, text="Eliminar",font=self.fuenteBotones,bg="#DF4843")
        self.botonEliminar.bind("<Button-1>",lambda e: self.boton_presionado(self.eliminarEventoSeleccionado))
        self.botonEliminar.grid(row=3,column=3,sticky="we",padx=5,pady=5);
        
    def boton_presionado(self,callback):
        self.after(100, callback)
        #self.padre.after(100, mostrar_alerta)
    def seleccionarEventoAEditar(self):
        seleccionado = self.tablaDeEventos.tabla.focus()
        if(not seleccionado):
            messagebox.showerror("Error","No se seleccionó un evento para editar");    
        else:
            valor = self.tablaDeEventos.tabla.item(seleccionado, "value")  
            indiceDiccionario, evento = self.manejadorJson.encontrarObjeto(
                valor)
            self.componenteEvento.editarRegistro(
                evento, indiceDiccionario, seleccionado)
            
    def eliminarEventoSeleccionado(self):
        seleccionado = self.tablaDeEventos.tabla.focus()
        if(not seleccionado):
            messagebox.showerror("Error","No se seleccionó una evento para eliminar");       
        else:   
            continuar=messagebox.askyesno(message="¿Desea continuar?", title="Se eliminara un evento");
            if continuar:
                valor = self.tablaDeEventos.tabla.item(seleccionado, "value")
                self.tablaDeEventos.tabla.delete(seleccionado);
                self.manejadorJson.eliminarObjeto(valor);
    

        
        

