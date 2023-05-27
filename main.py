from data.apartamentos import apartamento1,apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTabla

#crear el dataframe

tabla1=pd.DataFrame(apartamento1,columns=['edades'])
tabla2=pd.DataFrame(apartamento2,columns=['edades'])
tabla3=pd.read_csv('./data/empleados.csv')

# print(tabla1)
# print(tabla2)
print(tabla3)

#efectuando filtros con python
#1 necisto definir una condicion logica

empleadosJovenesAnalistas1=tabla3.query('edad<28 and cargo=="analista1"')
empladosSalariosBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir=tabla3.query('edad>=50 ')

# estadisticasAPT01=tabla1.describe()
# estadisticasAPT02=tabla2.describe()
# estadisticasEmpleados=tabla3.describe()

# print(estadisticasAPT01)
# print('\n')
# print(estadisticasAPT02)
# print('\n')
# print(estadisticasEmpleados)

#2 crearmos la tabla html con el dataframe del filtro
crearTabla(empleadosJovenesAnalistas1,"tablaJovenes")
crearTabla(empladosSalariosBajo,"tablaBajoSalario")
crearTabla(empleadosADespedir,"tablaoportunidaddemejora")

