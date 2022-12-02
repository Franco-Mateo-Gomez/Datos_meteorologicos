import pandas as pd
import matplotlib.pyplot as plt
import styles

#Importar dataset del aeropuerto local SAWE=  Río Grande
metar_data=pd.read_csv("DataReport/SAWE.csv")

#Convertir cada columna en una lista específica
diasDelMes=metar_data['Dia_mes'].tolist()
temperatura=metar_data['Temp_media_C'].tolist()
temperaturaMin=metar_data['Temp_min'].tolist()
temperaturaMax=metar_data['Temp_max'].tolist()
velocVientos=metar_data['Vientos'].tolist()

#-------Código principal-------#
plt.suptitle("Datos meteorológicos del aeropuerto de Río Grande, Tierra del Fuego")

# Gráfica N°1 - PICOS DE TEMPERATURA
plt.subplot(121)
plt.title('PICOS DE TEMPERATURA',y=1.03)
plt.tight_layout(pad=1)
plt.bar(diasDelMes, temperaturaMax, width= 0.5, label = 'Máxima', align='edge', color="#93574A")
plt.bar(diasDelMes, temperaturaMin, width= 0.5, label = 'Mínima', align='edge', color="#AB9264")
plt.xlabel('Días',labelpad = 10, color="#4B5056",fontsize=10)
plt.ylabel('°C',labelpad = 25, color="#4B5056",rotation=0,fontsize=10)
plt.legend(loc='upper right')
plt.tick_params(colors='#4B5056', which='both',labelsize=10)
#Color de ejes
plt.gca().spines['bottom'].set_color('#4B5056')

#Gráfica 2 - PROMEDIO DE TEMPERATURA
plt.subplot(222)
plt.title("TEMPERATURA MEDIA",y=1.1)
plt.xlabel('Días',labelpad = 10, color="#4B5056",fontsize=10)
plt.ylabel('°C',labelpad = 25, color="#4B5056",rotation=0,fontsize=10)
plt.bar(diasDelMes,temperatura,color='#4B5056',alpha=0.9,width= 0.5)
plt.tick_params(colors='#4B5056', which='both',labelsize=10)
#Color de ejes
plt.gca().spines['bottom'].set_color('#4B5056')

#Gráfica 3 - VIENTOS Y DIRECCIÓN
plt.subplot(224)
plt.title("VIENTOS")
plt.xlabel('Días',labelpad = 10, color="#4B5056",fontsize=10)
plt.ylabel('Km/h',labelpad = 28, color="#4B5056",rotation=0,fontsize=10)
plt.plot(diasDelMes,velocVientos,color='#4B5056',linewidth=2,marker='o')
plt.gca().spines['bottom'].set_color('#4B5056')
plt.tick_params(colors='#4B5056', which='both',labelsize=10)

#Ingreso de valores de dirección promedio del viento
plt.text(1.5,33,"250°")
plt.text(2.5,26,"293°")
plt.text(1.2,20.3,"295°")
plt.text(3.2,20.2,"250°")
plt.text(5.5,25,"0°")
plt.text(6.5,10.5,"90°")
plt.text(7.5,17,"0°")
plt.text(8.1,30.3,"295°")
plt.text(9.5,27.5,"255°")
plt.text(10.5,20,"270°")
plt.text(11,11,"25°")
plt.text(12.5,15.2,"24°")
plt.text(13,12,"0°")
plt.text(14.5,10.5,"90°")
plt.text(15.5,17,"296°")
plt.text(16,23.2,"270°")
plt.text(16.2,27.8,"271°")
plt.text(18.5,23,"314°")
plt.text(17.3,32,"249°")
plt.text(20.5,32,"314°")
plt.text(21.5,16,"3°")
plt.text(22.5,21,"293°")
plt.text(23.5,27,"315°")
plt.text(24,41,"250°")
plt.text(25,37.4,"353°")
plt.text(26.5,34,"2°")
plt.text(24.8,20.6,"269°")
plt.text(27.5,12.7,"1°")
plt.text(29.5,35,"270°")
plt.text(30.4,43.5,"271°")

#Color de ejes
plt.gca().spines['bottom'].set_color('#EEEEEE')

plt.tight_layout()  #Espaciado entre Subplots (Gráficas)

plt.show()