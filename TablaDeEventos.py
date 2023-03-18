import tkinter as tk
from tkinter import ttk;
from VentanaDetalleEvento import VentanaDetalleEvento
class TablaDeEventos(tk.Frame):

    def __init__(self,padre):
        super().__init__(padre);
        self.padre=padre;
        self.estilo = ttk.Style()
        self.estilo.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('consolas', 11))  # Modify the font of the body
        self.estilo.configure("mystyle.Treeview.Heading", font=(
            'consolas', 12, 'bold'))  # Modify the font of the headings
        self.estilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
                    'sticky': 'nswe'})])  # Remove the borders
        self.tabla = ttk.Treeview(self, columns=("Titulo", "Fecha", "Hora",
                            "Duracion", "Descripcion", "Importante"), style="mystyle.Treeview")
        #tabla.column para setear el tamaño de las columnas y alineacion creo
        self.tabla.column("#0", width=0)
        self.tabla.column("Titulo", width=200, anchor="center")
        self.tabla.column("Fecha", width=100, anchor="center")
        self.tabla.column("Hora", width=50, anchor="center")
        self.tabla.column("Duracion", width=100, anchor="center")
        self.tabla.column("Descripcion", width=110, anchor="center")
        self.tabla.column("Importante", width=120, anchor="center")

        #tabla.heading para referenciar a la columna supongo
        self.tabla.heading("#0", text="")
        self.tabla.heading("Titulo", text="Titulo", anchor="center")
        self.tabla.heading("Fecha", text="Fecha", anchor="center")
        self.tabla.heading("Hora", text="Hora", anchor="center")
        self.tabla.heading("Duracion", text="Duracion", anchor="center")
        self.tabla.heading("Descripcion", text="Descripcion", anchor="center")
        self.tabla.heading("Importante", text="Importante", anchor="center")
        self.tabla.insert("", index=0, iid=0, values=(
            "Pasear al perro", "12/02/2002", "22:10", "1 hora", "LLevar alimento", "NO"))
        self.tabla.insert("", index=1, iid=1, values=(
            "Salir a caminar", "12/01/2012", "12:10", "2 horas", "LLevar agua", "Si"))
        self.tabla.insert("", index=2, iid=2, values=("Prepararse para el parcial",
                    "12/02/2022", "23:10", "1 minuto", "LLevar apuntes", "Si"))
        self.tabla.grid();
        #ttk.Button(self,text="Mostrar Detalle del Evento Seleccionado",command=self.abrirVentanaDetalle).grid()
        self.tabla.bind("<Double-1>", self.mostrarDetalleEventoSeleccionado)

    def mostrarDetalleEventoSeleccionado(self, e):
        
        seleccionado=self.tabla.focus();
        valor = self.tabla.item(seleccionado,"value") ;
        VentanaDetalleEvento(self.padre,valor);
        print(valor);
        print(type(valor));
        print(len(valor));
        #self.tabla.item(seleccionado, values=(
        #    valor[0], valor[1], valor[2], valor[3], valor[4], "SIII"))
root=tk.Tk();
app=TablaDeEventos(root);
app.grid();
root.mainloop();