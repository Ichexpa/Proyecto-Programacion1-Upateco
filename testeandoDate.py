from datetime import datetime, date

fecha_str = '2022-03-21'
fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
fechaEnOtroFormato = fecha.strftime('%d-%m-%Y')#devueve un string
print(fechaEnOtroFormato);
fechaFormateada = datetime.strptime(fechaEnOtroFormato, '%d-%m-%Y');
print(fechaFormateada);
print(str(fechaFormateada))

#from datetime import date, datetime,timedelta

""" fecha = datetime.now().date();

print(fecha>date(2022,3,20)) """

""" fechaActual = datetime.now().date()
fechaLimite = fechaActual+timedelta(days=7)
print(type(fechaLimite)); """
""" fecha_str = fecha.strftime('%d-%m-%Y')
print(fecha_str);

print(type(fecha_str))
 """