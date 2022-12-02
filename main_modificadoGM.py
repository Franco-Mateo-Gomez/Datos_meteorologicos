import pandas as pd
import matplotlib.pyplot as plt

#Importar dataset del aeropuerto local SAWE=  Río Grande
metar_data=pd.read_csv("DataReport/SAWE.csv")

#Convertir cada columna en una lista específica
diasDelMes=metar_data['Dia_mes'].tolist()
temperatura=metar_data['Temp_media_C'].tolist()
temperaturaMin=metar_data['Temp_min'].tolist()
temperaturaMax=metar_data['Temp_max'].tolist()
velocVientos=metar_data['Vientos'].tolist()


#plt.subplots(nrows=2, ncols=1)
plt.style.use('ggplot')

#-------Código principal-------#
plt.suptitle("Datos meteorológicos del aeropuerto de Río Grande, Tierra del Fuego")

#Gráfica 1 - TEMPERATURA
plt.subplot(222)
plt.title("TEMPERATURA MEDIA")
plt.xlabel('Número de días')
plt.ylabel('°C')
plt.tight_layout(pad=1)
plt.bar(diasDelMes,temperatura)
plt.ylim(-2,+20)


#Gráfica 2 - VIENTOS
plt.subplot(224)
plt.title("VIENTOS")
plt.xlabel('Número de días')
plt.ylabel('Km/h')
plt.tight_layout(pad=1)
plt.plot(diasDelMes,velocVientos,marker='o')

#Ingreso de valores de dirección promedio del viento
plt.text(1.5,33,"250°")
plt.text(2.5,26,"293°")
plt.text(1.3,20.8,"295°")
plt.text(3.5,20.5,"250°")
plt.text(5.5,25,"0°")
plt.text(6.5,10,"90°")
plt.text(7.5,17,"0°")
plt.text(7.5,31,"295°")
plt.text(9.5,28,"255°")
plt.text(10.5,20,"270°")
plt.text(10.5,11.4,"25°")
plt.text(12.5,15,"24°")
plt.text(13.3,11,"0°")
plt.text(14.5,10,"90°")
plt.text(15.5,17,"296°")
plt.text(14,25,"270°")
plt.text(16.5,27.8,"271°")
plt.text(18.5,23,"314°")
plt.text(17.3,31,"249°")
plt.text(20.5,32,"314°")
plt.text(21.5,16,"3°")
plt.text(22.5,21,"293°")
plt.text(23.5,27,"315")


plt.tight_layout()  #Espaciado entre Subplots (Gráficas)

#Graficá 3 temperatura maxima y minima
plt.subplot(121)
plt.tight_layout(pad=1)
plt.bar(diasDelMes, temperaturaMax, width= 0.25, label = 'Temperatura maxima', align='edge', color="red")
plt.bar(diasDelMes, temperaturaMin, width= 0.25, label = 'Temperatura minima', align='edge', color="skyblue")
plt.xlabel('Número de días')
plt.ylabel('°C')
plt.legend(loc='upper right')
plt.title('PICOS DE TEMPERATURAS')
plt.xticks(diasDelMes)
plt.grid(True, linewidth= 1, linestyle="--")

plt.show()