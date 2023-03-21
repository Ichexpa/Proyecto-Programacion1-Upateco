from datetime import date, datetime,timedelta;

from calendar import monthrange
class AdministradorDeFechas:

    def cadenaDeFechaADate(fecha):
       return datetime.strptime(fecha,'%d-%m-%Y').date();
    def seEncuentraEnLaSemana(fecha,dias):
        fechaActual = datetime.now().date();
        fechaLimiteSuperior=fechaActual+timedelta(days=dias);
        print(f"La fecha superior es {fechaLimiteSuperior}");
        fechaLimiteInferior=fechaLimiteSuperior-timedelta(days=7)
        print(f"La fecha Inferior es {fechaLimiteInferior}")
        return fecha >= fechaLimiteInferior and fecha <= fechaLimiteSuperior
    def unirFechaYHoraCadenasEnDatetime(fecha,hora):
        fechaYhora=f'{fecha} {hora}';
        fechaYhoraConvertidos=datetime.strptime(fechaYhora,"%d-%m-%Y %H:%M");
        return fechaYhoraConvertidos;
    def getMesActual(self,fecha):
        ultimoDiaDelMes=monthrange(fecha.year,fecha.month);
        self.fechaPrimerDia = date(fecha.year,fecha.month, 1)
        self.fechaUltimoDia = date(fecha.year, fecha.month, ultimoDiaDelMes[1])        
        """ print(f"primera fecha {self.fechaPrimerDia}");
        print(f"ultima fecha {self.fechaUltimoDia}"); """
    def aumentarMes(self):
        self.fechaUltimoDia = self.fechaUltimoDia+timedelta(days=1)
    def restarMes(self):
        self.fechaPrimerDia=self.fechaPrimerDia-timedelta(days=1);

    def comprobarSiSeEncuentraEnElMesActual(fecha,fechaInferior, fechaSuperior):
        return fecha>=fechaInferior and fecha<=fechaSuperior;

#print(AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime("21-02-2022","12:30")>datetime.now());
""" fecha=AdministradorDeFechas()
fechaPrim = date(2023,12,20)
fecha.getMesActual(fechaPrim)
fecha.aumentarMes()
fecha.getMesActual(fecha.fechaUltimoDia)
fecha.restarMes();
fecha.getMesActual(fecha.fechaPrimerDia);
fecha.restarMes()
fecha.getMesActual(fecha.fechaPrimerDia) """
