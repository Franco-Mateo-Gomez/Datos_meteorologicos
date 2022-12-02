import matplotlib.pyplot as plt

#---Código de estilos---#
palette={"background": "#F7F6F5"}

#Marcas de ejes
plt.rcParams["axes.spines.bottom"]=True
plt.rcParams["axes.spines.left"]=False
plt.rcParams["axes.spines.right"]=False
plt.rcParams["axes.spines.top"]=False

#Formato de rejilla
plt.rcParams["axes.grid"]=True
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 1
plt.rcParams["axes.grid.axis"] = 'y'
plt.rcParams["grid.color"] = "#4B5056"

#Texto: Título
plt.rcParams["figure.titlesize"] = 18
plt.rcParams["figure.titleweight"] = "regular"

plt.rcParams["axes.titlesize"] = 14
plt.rcParams['axes.titleweight'] = "regular"
plt.rcParams['axes.titlecolor']= '#4B5056'
plt.rcParams['axes.titlelocation']= 'center'

plt.rcParams['font.weight'] = "regular"
plt.rcParams['font.size'] = 9
plt.rcParams['text.color'] = "#4B5056"

#Background color
plt.rcParams["figure.facecolor"] = palette["background"]
plt.rcParams["axes.facecolor"] = palette["background"]

#---Fin de código de estilos---#