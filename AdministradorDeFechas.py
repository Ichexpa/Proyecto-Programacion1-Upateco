from datetime import date, datetime,timedelta;

from calendar import monthrange

class AdministradorDeFechas:

    def __init__(self):
        #Debo modulizar este codigo
        self.actualizarAtributosFecha(7);
        #hasta aca
        #self.fechaLimiteInferior=0;
        #self.fechaLimiteSuperior=0;

    def cadenaDeFechaADate(fecha):
       return datetime.strptime(fecha,'%d-%m-%Y').date();

    def actualizarAtributosFecha(self,dias):
        fechaActual = datetime.now().date();
        self.fechaLimiteSuperior=fechaActual+timedelta(days=dias);
        #print(self.fechaLimiteInferior);
        #print(f"La fecha superior es {self.fechaLimiteSuperior}")
        self.fechaLimiteInferior = self.fechaLimiteSuperior-timedelta(days=7)

    def seEncuentraEnLaSemana(self,fecha,dias):
        self.actualizarAtributosFecha(dias);
        return fecha >= self.fechaLimiteInferior and fecha <= self.fechaLimiteSuperior
    
    def mostrarFormateadaFechaDiaMes(fecha):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];
        return f'{dias[fecha.weekday()]} {fecha.day} de {meses[fecha.month-1]} del {fecha.year}';

    def unirFechaYHoraCadenasEnDatetime(fecha,hora):
        
        fechaYhora=f'{fecha} {hora}';
        fechaYhoraConvertidos=datetime.strptime(fechaYhora,"%d-%m-%Y %H:%M");
        return fechaYhoraConvertidos;
    def getMesActual(self,fecha):

        ultimoDiaDelMes=monthrange(fecha.year,fecha.month);
        self.fechaPrimerDia = date(fecha.year,fecha.month, 1)
        self.fechaUltimoDia = date(fecha.year, fecha.month, ultimoDiaDelMes[1])        
        
    def aumentarMes(self):
        self.fechaUltimoDia = self.fechaUltimoDia+timedelta(days=1)
    def restarMes(self):
        self.fechaPrimerDia=self.fechaPrimerDia-timedelta(days=1);

    def comprobarSiSeEncuentraEnElMesActual(fecha,fechaInferior, fechaSuperior):
        return fecha>=fechaInferior and fecha<=fechaSuperior;

    def getNombreMesActual(self):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
        return f'{meses[self.fechaPrimerDia.month-1]} del {self.fechaPrimerDia.year}'
