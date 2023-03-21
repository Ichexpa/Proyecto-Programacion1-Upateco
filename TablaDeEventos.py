import tkinter as tk
from tkinter import ttk,messagebox;
from VentanaDetalleEvento import VentanaDetalleEvento
from ManejadorJson import ManejadorJson
from AdministradorDeFechas import AdministradorDeFechas
from datetime import datetime
class TablaDeEventos(tk.Frame):

    def __init__(self,padre,manejadorJson):
        super().__init__(padre);
        self.contadorSiguienteSemana=7;
        self.padre=padre;
        self.administradorDeFecha=AdministradorDeFechas();
        self.administradorDeFecha.getMesActual(datetime.now().date())
        self.accesorAlFicheroJson = manejadorJson;
        self.estilo = ttk.Style()
        self.estilo.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('consolas', 11))  # Modify the font of the body
        self.estilo.configure("mystyle.Treeview.Heading", font=(
            'consolas', 12, 'bold'))  # Modify the font of the headings
        self.estilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
                    'sticky': 'nswe'})])  # Remove the borders
        self.botonSiguienteSemana=tk.Button(self,text="Siguiente Semana");
        self.botonSiguienteSemana.bind("<Button-1>", self.siguienteSemana)
        self.botonSiguienteSemana.grid(row=1, column=3)

        self.botonAnteriorSemana = tk.Button(self, text="Anterior Semana")
        self.botonAnteriorSemana.bind("<Button-1>", self.anteriorSemana)
        self.botonAnteriorSemana.grid(row=1, column=2)
        
        self.botonMesSiguiente = tk.Button(self, text="Mes siguiente")
        self.botonMesSiguiente.bind("<Button-1>", self.siguienteMes)

        self.botonMesAnterior = tk.Button(self, text="Mes anterior")
        self.botonMesAnterior.bind("<Button-1>", self.mesAnterior)

        self.comboOpcionesDeFiltro=ttk.Combobox(values=["Filtrar por Mes","Filtrar por Semana"]);
        self.comboOpcionesDeFiltro.current(1)#Por defecto estara apuntando a filtrar por semana
        self.comboOpcionesDeFiltro.bind("<<ComboboxSelected>>",self.seleccionDeFiltro);
        self.comboOpcionesDeFiltro.grid(row=0,column=3);
    
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
        self.tabla.grid(row=2,column=0,columnspan=4);
        self.cargarTablaPorSemana();
        #ttk.Button(self,text="Mostrar Detalle del Evento Seleccionado",command=self.abrirVentanaDetalle).grid()
        self.tabla.bind("<Double-1>", self.mostrarDetalleEventoSeleccionado)

    def mostrarDetalleEventoSeleccionado(self, e):        
        seleccionado=self.tabla.focus();
        valor = self.tabla.item(seleccionado,"value") ;
        VentanaDetalleEvento(self.padre,valor);
    def agregarEventoATabla(self,evento):
        #Se guarda el evento formateado al json que a su vez lo guarda en la lista de la clase
        resultadoGuardado=self.accesorAlFicheroJson.agregarObjetoAFichero(evento.getEventoComoDict());
        if(resultadoGuardado):
            fechaTipoDate = AdministradorDeFechas.cadenaDeFechaADate(evento.fecha)
            seEncuentraEnLaSemana = AdministradorDeFechas.seEncuentraEnLaSemana(fechaTipoDate,  # Retorna un booleano
                                                                            self.contadorSiguienteSemana)
            seEncuentraEnElMes = AdministradorDeFechas.comprobarSiSeEncuentraEnElMesActual(fechaTipoDate,
                                                                                       self.administradorDeFecha.fechaPrimerDia,
                                                                                       self.administradorDeFecha.fechaUltimoDia)
            if (self.comboOpcionesDeFiltro.get() == "Filtrar por Mes" and seEncuentraEnElMes):
                self.agregarEventoOrdenado(evento)
            elif (self.comboOpcionesDeFiltro.get() == "Filtrar por Semana" and seEncuentraEnLaSemana):
                self.agregarEventoOrdenado(evento)
        else:
            messagebox.showerror("Evento existente","Ya existe un evento con la fecha y hora indicada");
            
        #Se pasa a fecha la fecha que se encontraba en string para poder comprobar si se encuentra en la semana
        
    #Si esta en mes y se encuentra en el parametro se agrega a la tabla
    #Se esta en la semana y se enceuntra entre los intervalos se agrega a la tabla
    def agregarEventoOrdenado(self,evento):
        tuplaNuevoEvento = (evento.titulo,
                            evento.fecha,
                            evento.hora,
                            evento.duracion,
                            evento.descripcion,
                            self.esImportante(evento.importancia))
        self.tabla.insert("", tk.END, values=tuplaNuevoEvento);

        self.agregarFechaOrdenada();
    def cargarTablaPorSemana(self):
        self.eliminarFilas();
        listaDeEventosPrimeraSemana = self.accesorAlFicheroJson.obtenerPrimerosSieteDias(self.contadorSiguienteSemana);
        ##Carga la tabla ordenada
        #No usar hasta validar campos obligatorios
        listaDeEventosPrimeraSemana=sorted(listaDeEventosPrimeraSemana,
                                           key= lambda elemento:
                                           AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(elemento["fecha"],elemento["hora"]))
        for evento in listaDeEventosPrimeraSemana:
            self.tabla.insert("", tk.END, values=(evento["titulo"],
                                                      evento["fecha"],
                                                      evento["hora"],
                                                      evento["duracion"],
                                                      evento["descripcion"],
                                                      self.esImportante(evento["importancia"])));
        # Esto solo se aplicara cuando se clickee siguiente
    def esImportante(self,valor):
        if (valor):
            esImportante = "Si"
        else:
            esImportante="No"
        return esImportante;
    def eliminarFilas(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila);
    
    def agregarFechaOrdenada(self):
        filasDeTabla=self.tabla.get_children();
        filasDeTabla = sorted(filasDeTabla, key=lambda e: AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(
            self.tabla.item(e)["values"][1], self.tabla.item(e)["values"][2]))
        
        for index,k in enumerate(filasDeTabla):
            self.tabla.move(k, '', index)

    def siguienteSemana(self,e):
        self.contadorSiguienteSemana += 7
        self.cargarTablaPorSemana();
        
    
    def anteriorSemana(self,e):
        self.contadorSiguienteSemana -= 7
        #print("Entro al metodo")
        #if(self.contadorSiguienteSemana<=7):
            #self.botonAnteriorSemana["state"]=tk.DISABLED;
        #    self.botonAnteriorSemana.grid_forget();
        #else:
            #print("Entro al else")           
        self.cargarTablaPorSemana();

    def modificarFila(self,evento,indiceFila):
       self.tabla.item(indiceFila, values=(evento.titulo,
                                     evento.fecha,
                                     evento.hora,
                                     evento.duracion,
                                     evento.descripcion,
                                     self.esImportante(evento.importancia)))
    def filtrarPorMes(self):
        self.cargarRegistrosDelMesEnTabla();
        self.botonMesSiguiente.grid(row=1, column=3)
        self.botonMesAnterior.grid(row=1,column=2);
    def cargarRegistrosDelMesEnTabla(self):
        self.eliminarFilas()
        listaDeEventosDentroDelMes = self.accesorAlFicheroJson.obtenerMes(self.administradorDeFecha.fechaPrimerDia,
                                                                          self.administradorDeFecha.fechaUltimoDia)
        listaDeEventosDentroDelMes = sorted(listaDeEventosDentroDelMes,
               key=lambda elemento:
               AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(elemento["fecha"], elemento["hora"]))
        """ print(
            f"Primera fecha inciada {self.administradorDeFecha.fechaPrimerDia}, {self.administradorDeFecha.fechaUltimoDia}")
        print(listaDeEventosDentroDelMes) """
        
        for evento in listaDeEventosDentroDelMes:
            self.tabla.insert("", tk.END, values=(evento["titulo"],
                                                  evento["fecha"],
                                                  evento["hora"],
                                                  evento["duracion"],
                                                  evento["descripcion"],
                                                  self.esImportante(evento["importancia"])));
    def siguienteMes(self,e):
        self.administradorDeFecha.aumentarMes();
        self.administradorDeFecha.getMesActual(self.administradorDeFecha.fechaUltimoDia);
        self.cargarRegistrosDelMesEnTabla();        
        #print(f"Mostrando Fecha desde siguiente mes {self.administradorDeFecha.fechaUltimoDia} {self.administradorDeFecha.fechaPrimerDia}")
    def mesAnterior(self,e):
        self.administradorDeFecha.restarMes();
        self.administradorDeFecha.getMesActual(self.administradorDeFecha.fechaPrimerDia);
        self.cargarRegistrosDelMesEnTabla(); 
    def seleccionDeFiltro(self,e):
        self.botonAnteriorSemana.grid_forget();
        self.botonSiguienteSemana.grid_forget();
        self.botonMesSiguiente.grid_forget();
        self.botonMesAnterior.grid_forget();
        if(self.comboOpcionesDeFiltro.get()=="Filtrar por Semana"):
            self.cargarTablaPorSemana();
            self.botonSiguienteSemana.grid(row=1,column=3)
            self.botonAnteriorSemana.grid(row=1,column=2);
        else:            
            self.filtrarPorMes();