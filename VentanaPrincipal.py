import tkinter as tk
from tkinter import ttk,messagebox
from ComponenteEvento import ComponenteEvento;
from TablaDeEventos import TablaDeEventos;

class VentanaPrincipal(tk.Frame):
    fuenteBotones = ("consolas", 14, "bold");
    def __init__(self,padre,manejadorJSon):
        super().__init__(padre);
        self.padre=padre;
        self.manejadorJson=manejadorJSon;
        self.tablaDeEventos=TablaDeEventos(self,self.manejadorJson);
        self.tablaDeEventos.grid(row=1,column=1);
        self.componenteEvento = ComponenteEvento(self, self.tablaDeEventos,self.manejadorJson);
        self.componenteEvento.grid(row=1, column=0);
        self.frameTitulo=tk.Frame(self);
        self.frameTitulo.grid(row=0, column=0, columnspan=2);
        self.tituloLabel = tk.Label(self.frameTitulo, text="Agenda de Eventos", font=("consolas", 25, "bold"));
        self.tituloLabel.grid();
        self.botonEditar=tk.Button(self.tablaDeEventos.contenedorTabla,text="Editar",font=self.fuenteBotones,bg="#43DFAD",fg="white");
        self.botonEditar.bind("<Button-1>",lambda e: self.boton_presionado(self.seleccionarEventoAEditar));
        self.botonEditar.grid(row=4,column=2,sticky="we",padx=5,pady=5);
        self.botonEliminar = tk.Button(self.tablaDeEventos.contenedorTabla, text="Eliminar", font=self.fuenteBotones, bg="#DF4843",fg="white");
        self.botonEliminar.bind("<Button-1>",lambda e: self.boton_presionado(self.eliminarEventoSeleccionado));
        self.botonEliminar.grid(row=4,column=3,sticky="we",padx=5,pady=5);
        
    def boton_presionado(self,callback):
        self.after(100, callback);
    def seleccionarEventoAEditar(self):
        seleccionado = self.tablaDeEventos.tabla.focus();
        if(not seleccionado):
            messagebox.showerror("Error","No se seleccionó un evento para editar");    
        else:
            valor = self.tablaDeEventos.tabla.item(seleccionado, "value");  
            indiceDiccionario, evento = self.manejadorJson.encontrarObjeto(valor);
            self.componenteEvento.editarRegistro(evento, indiceDiccionario, seleccionado);
            
    def eliminarEventoSeleccionado(self):
        seleccionado = self.tablaDeEventos.tabla.focus();
        if(not seleccionado):
            messagebox.showerror("Error","No se seleccionó una evento para eliminar");       
        else:   
            valor = self.tablaDeEventos.tabla.item(seleccionado, "value");
            print(valor);
            continuar = messagebox.askyesno(message="¿Desea continuar?\n Evento: " + valor[0], title="Se eliminara un evento");
            if continuar:                
                self.tablaDeEventos.tabla.delete(seleccionado);
                self.manejadorJson.eliminarObjeto(valor);
    

        
        

