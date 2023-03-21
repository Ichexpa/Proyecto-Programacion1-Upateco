import json;
from datetime import date, datetime,timedelta;
from AdministradorDeFechas import AdministradorDeFechas
class ManejadorJson:
    def __init__(self,ruta):
        self.ruta=ruta;
        self.contenedorObjetos=[];
        self.cargarContenedorEvento()
    def comprobarRepitencia(self,evento):
        #if(evento[""])
        pass

    def agregarObjetoAFichero(self, evento):
        self.contenedorObjetos.append(evento);          
        self.escribirEnFichero()

    def encontrarObjeto(self, evento):
        eventoAEliminar=AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(evento[1],evento[2]);
        for indice,objeto in enumerate(self.contenedorObjetos):
            fechaDelEventoAElminar=AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(objeto["fecha"],objeto["hora"]);
            if(eventoAEliminar==fechaDelEventoAElminar):
                return indice,objeto;
        print("No se econtro coincidencia");
    
    def eliminarObjeto(self,evento):
        indice=self.encontrarObjeto(evento)[0];
        print("Indice del objeto a eliminar"+ str(indice));
        del self.contenedorObjetos[indice];
        self.escribirEnFichero();
    
    def escribirEnFichero(self):
        with open(self.ruta, "w", encoding="UTF-8") as archivo:
            json.dump(self.contenedorObjetos, archivo)

    def modificarObjeto(self,evento):
        indice=self.encontrarObjeto(evento);
        
        pass
    def cargarContenedorEvento(self):
        try:
            with open(self.ruta, "r", encoding="UTF-8") as archivo:
                self.contenedorObjetos = json.load(archivo);
        except FileNotFoundError:
            print("No se encontro la ruta especificada, Se procedera a crearla");
            archivo=open(self.ruta,"w");
            archivo.close();
    def obtenerPrimerosSieteDias(self,dias=7):
        listaPrimerosDias=[]
        for indice,item in enumerate(self.contenedorObjetos):
            fechaAComparar = AdministradorDeFechas.cadenaDeFechaADate(item["fecha"]);
            if (AdministradorDeFechas.seEncuentraEnLaSemana(fechaAComparar,dias)):
                listaPrimerosDias.append(self.contenedorObjetos[indice]);
        return listaPrimerosDias;

    def obtenerMes(self,mesInferior,mesSuperior):
        listaDeEventosMeses=[];        
        for indice, item in enumerate(self.contenedorObjetos):
            fechaAComparar = AdministradorDeFechas.cadenaDeFechaADate(item["fecha"]);
            if (AdministradorDeFechas.comprobarSiSeEncuentraEnElMesActual(fechaAComparar,mesInferior,mesSuperior)):
                listaDeEventosMeses.append(self.contenedorObjetos[indice]);
        return listaDeEventosMeses
    
        

        

""" Yeison=ManejadorJson("json.json");
Yeison.agregarObjetoAFichero({'titulo': 'Pimpeano', 'fecha': '12,32', 'hora': '232', 'duracion': 24, 'descripcion': '',
                              'importancia': False, 'fechaRecordatorio': 415, 'horaRecordatorio': 223, 'identificadorEvento': 343})
 """