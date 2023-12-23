import xml.etree.ElementTree as ET
import random
from menus import Menu
from metodos import Metodos
import datetime
import time

class Taller_final:       
    def __init__(self):
        self.Menu=Menu()
        

    def iniciar(self):
        while True:
            self.Menu.items("TallerFinal.xml","Ejercicios Finales")        
            self.Menu.crear()
            root=ET.parse(f"./Talleres/TallerFinal.xml")
            while True:
                try:
                    punto=int(input("Ingrese ejercicio o 6 para Salir: "))
                    if punto>=1 and punto<=6:
                        break
                    else:
                        print("Debes ingresar valor entre 1 y 6")
                except:
                    print("Debes ingresar solo valores")
            if punto!=6:
                enunciado=root.find(f'.//ejercicio[@num="{punto}"]/enun').text
                print(enunciado)    
                if punto==1:
                    while True:
                        cod=input("Ingrese codigo del alumno o 000 para terminar: ")                        
                        if cod!="000":
                            calificaciones=[]                        
                            h=0
                            areas=["Python","Java","Web Service","NoSQL","NetWrorking"]                        
                            for area in areas:
                                h=0
                                print(f"Ingrese calificación para el área de {area}")
                                while True:                            
                                    try:
                                        nota=float(input("Calificación: "))
                                        if nota>=0 and nota<=5:
                                            break 
                                        else:
                                            print("Nota fuera de rango")                                       
                                    except:
                                        print("Debes ingresar un valor")
                                if nota>=1 and nota<=2.5:
                                    h=1
                                elif nota>=2.6 and nota<=2.9:
                                    h=2                            
                                concepto=Metodos([nota,0]).calificacion()
                                calificaciones.append([area,nota,concepto,h,0,""])                                        
                            habilitar=False
                            for calif in calificaciones:
                                print(calif)  
                                if calif[3]!=0:
                                    habilitar=True
                            if habilitar:
                                print("Hay recuperaciones pendinetes, ingresa calificación de la habilitación")
                                print("Recuerda que para recuperar una nota entre 1 y 2.5 la habilitación debe ser >=4")
                                print("Y para recuperar una nota de 2.6 a 2.9 debe ser >=3")
                                for calif in calificaciones:
                                    if calif[3]!=0:
                                        print(f"Ingresa calificación para {calif[0]}")
                                        while True:
                                            try:
                                                nh=float(input("Calificación habilitación: "))
                                                if nh>=0 and nh<=5:
                                                    break
                                                else:
                                                    print("Nota fuera de rango")                                       
                                            except:
                                                print("Debes ingresar un valor")
                                        calif[4]=nh
                                        calif[5]=Metodos([nh,calif[3]]).calificacion()
                            print("*** Calificaciones Finales ***")
                            for calif in calificaciones:
                                print(calif)  
                        else:
                            break                      

                elif punto==2:
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese numero o 0 para terminar: ")) 
                                if numero>=0:
                                    break
                                else:
                                    print("Para este ejercicio no puedes ingresar negativos")
                            except:
                                print("Debes ingresar un valor")

                        if numero!=0:       
                            respupar="No"
                            respuprimo="No"
                            respuesta=f"El número {numero} {respupar} es par y {respuprimo} es primo"
                            if Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuprimo} es primo"
                            if Metodos([numero]).primo()[0]:
                                respuprimo="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuprimo} es primo"
                            print(respuesta)
                            print(f"El número {numero} {respupar} es par, la división con 2 {respupar} es exacta: Cociente={numero/2} Resto={numero%2}")
                            print(f"El número {numero} {respuprimo} es primo, sus divisores son: {Metodos([numero]).primo()[1]}")
                        else:
                            break
                elif punto==3:
                    try:
                        while True:
                            hora_actual = datetime.datetime.now()
                            hora_str = hora_actual.strftime("%H:%M:%S")
                            print("\rHora actual ((Ctrl + C) Para finalizar):", hora_str, end="", flush=True)
                            time.sleep(1)
                    except KeyboardInterrupt:
                        print("\nHora detenida")
                    sx=input()
                elif punto==4:
                    while True:
                        while True:
                            try:
                                minimos=int(input("Ingrese cantidad de salarios mínimos del empleado o 0 para terminar: "))
                                if minimos>=0:
                                    break
                                else:
                                    print("No se aceptan números negativos")
                            except:
                                print("Debes ingresar un valor")
                        salario=minimos*1160000
                        if minimos!=0:       
                            discriminado=Metodos([salario]).calculoSalarial()
                            print(f"Para un salario de {salario}: ")
                            for i,v in discriminado[1].items():
                                print(f"{i} : {v}")
                            print(f"Total Salario empleado: ${discriminado[2]}")
                        else:
                            break
                elif punto==5:                                            
                            self.Menu.items("combos.xml","Nuestros Combos")
                            self.Menu.crear()
                            rootm=ET.parse("./Talleres/combos.xml")
                            total=0
                            tiket=[]
                            while True:
                                while True:
                                    try:
                                        menuop=int(input("Haga su pedido o 5 para terminar: "))
                                        if menuop>=1 and menuop<=5:
                                            break
                                        else:
                                            print("Opción inexistente")
                                    except:
                                        print("Debes ingresar valor")
                                if menuop!=5:
                                    enunciadop=rootm.find(f'.//ejercicio[@num="{menuop}"]/enun').text
                                    nombre=rootm.find(f'.//ejercicio[@num="{menuop}"]').get('nom')
                                    precio=int(rootm.find(f'.//ejercicio[@num="{menuop}"]/enun').get('precio'))
                                    total+=precio
                                    esta=False
                                    cant=1
                                    for t in tiket:                                        
                                        if t[0]==menuop:
                                            t[3]+=precio
                                            t[2]+=1
                                            esta=True
                                    if not esta:
                                        tiket.append([menuop,nombre,cant,precio])
                                    print(enunciadop)
                                    print(nombre)                             

                                    print(f"Total mesa:          ${total}")
                                else:
                                    print("** Tu factura -->")
                                    print("#   Combo        Cant      Precio")
                                    print("*********************************")
                                    for ti in tiket:
                                        print(f"{ti[0]}   {ti[1]}   {ti[2]}   {ti[3]}")

                                    print(f"Total mesa:             ${total}")
                                    input()
                                    break                                
                            
                        
                else:
                    print("Opción no valida")
                
            else:
                break



            
    