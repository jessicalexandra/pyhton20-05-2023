import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalarioPorEdad(dataFrame,rangos,columnaInteres,columnaPromediar,nombreGrafica):
    plt.figure()

    #crear una columna nueva por rangos de edad

    dataFrame['rangosEdad']=pd.cut(dataFrame[columnaInteres],bins=rangos)

    #calcular la suma de los salarios por rango de edad

    salarioPorRango=dataFrame.groupby('rangosEdad')[columnaPromediar].sum()

    #definimos los datos a graficar
    salario=salarioPorRango.values
    rangosEdad=salarioPorRango.index
    plt.pie(salario,labels=rangosEdad,autopct='%1.1f%%')
    plt.title('Salarios por rango de edad')
    plt.savefig(f'./assets/img/{nombreGrafica}.png')
