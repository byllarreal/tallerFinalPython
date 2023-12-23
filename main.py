import xml.etree.ElementTree as ET
from menus import Menu
from Taller1 import Taller_uno
from Taller2 import Taller_dos
from TallerFinal import Taller_final

Menu=Menu()


Taller_uno=Taller_uno()
Taller_dos=Taller_dos()
Taller_final=Taller_final()

while True:
    Menu.items("Talleres.xml","Desarrollo de Talleres")
    Menu.crear()

    while True:
        try:
            taller=int(input("Ingrese número de taller o 4 para terminar: "))
            if taller>0 and taller<=4:
                break
            else:
                print("Debes ingresar número entre 1 y 4")
        except:
            print("Debes ingresar el número correspondiente al taller")
    if taller!=4:
        if taller==1:
            Taller_uno.iniciar()
        elif taller==2:
            Taller_dos.iniciar()
        elif taller==3:
            Taller_final.iniciar()
    else:
        break