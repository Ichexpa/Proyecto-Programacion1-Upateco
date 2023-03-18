import calendar 
class Evento:
    def __init__(self, titulo, fecha, hora, duracion, fechaRecordatorio, horaRecordatorio, identificadorEvento, descripcion="", importancia=False):
        self.titulo=titulo;
        self.fecha=fecha;
        self.hora=hora;
        self.duracion=duracion;
        self.descripcion=descripcion
        self.importancia=importancia;
        self.fechaRecordatorio=fechaRecordatorio;
        self.horaRecordatorio=horaRecordatorio;
        self.identificadorEvento=identificadorEvento;
