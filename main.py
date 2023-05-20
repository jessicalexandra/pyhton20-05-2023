from data.apartamentos import apartamento1,apartamento2
import pandas as pd

#crear el dataframe

tabla1=pd.DataFrame(apartamento1,columns=['edades'])
tabla2=pd.DataFrame(apartamento2,columns=['edades'])
tabla3=pd.read_csv('./data/empleados.csv')

# print(tabla1)
# print(tabla2)

estadisticasAPT01=tabla1.describe()
estadisticasAPT02=tabla2.describe()
estadisticasEmpleados=tabla3.describe()

print(estadisticasAPT01)
print('\n')
print(estadisticasAPT02)
print('\n')
print(estadisticasEmpleados)