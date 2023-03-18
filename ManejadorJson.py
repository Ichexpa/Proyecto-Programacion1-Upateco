import json;
class ManejadorJson:
    def __init__(self,ruta):
        self.ruta=ruta;
    def actualizarObjeto(self,diccionario):
        with open(self.ruta,"a",encoding="UTF-8") as archivo:
            json.dump(diccionario,archivo);
    def eliminarObjeto(self,diccionario):
        pass
    def getObjeto(self,diccionario):
        pass
    def agregarObjeto(self,diccionario):
        pass
Yeison=ManejadorJson("json.json");
