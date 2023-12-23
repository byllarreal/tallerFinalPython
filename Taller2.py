import xml.etree.ElementTree as ET
import random
import time
from menus import Menu
from metodos import Metodos


class Taller_dos:       
    def __init__(self):
        self.Menu=Menu()
        

    def iniciar(self):
        while True:
            self.Menu.items("Taller2.xml","Ejercicios de cíclos")        
            self.Menu.crear()
            root=ET.parse(f"./Talleres/Taller2.xml")
            punto=input("Ingrese ejercicio u 11 para Salir: ")
            if punto!='11':
                enunciado=root.find(f'.//ejercicio[@num="{punto}"]/enun').text
                print(enunciado)    
                if punto=='1':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número de la tabla o 0 para terminar: "))
                                if numero>=0:
                                    break                                
                                else:
                                    print("Debes ingresar un entero positivo")
                            except:
                                print("Debes ingresar solo enteros positivos")
                        if numero>0:
                            tabla=Metodos([numero]).tablas()
                            for t in tabla:
                                print(t)
                        else:
                            break

                elif punto=='2':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número o 0 para terminar: "))
                                if numero>=0:
                                    break
                                else:
                                    print("Debes ingresar enteros positivos")
                            except:
                                print("Debes ingresar solo enteros positivos")
                        if numero>0:
                            print(f"El número {numero} si es un entero positivo")
                        else:
                            break                    
                elif punto=='3':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número o 0 para terminar: "))
                                if numero==0 or (numero>0 and len(str(numero)))==3:
                                    break
                                else:
                                    print("Debes ingresar un número positivo de 3 cifras")
                            except:
                                print("Debes ingresar un número positivo de 3 cifras")
                        if numero!=0:
                            print(f"Excelente el número {numero} si es un entero positivo de 3 cifras")
                        else:
                            break
                elif punto=='4':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número o 0 para terminar: "))
                                if numero>=0:
                                    break
                                else:
                                    print("Ingrese un entero positivo")
                            except:
                                print("Debes ingresar solo enteros positivos")
                        if numero!=0:
                            suma=0
                            divisores=Metodos([numero]).primo()[1]
                            print(divisores)
                            for div in divisores:
                                if div!=numero:
                                    suma+=div
                            if numero==suma:
                                print(f"El número {numero} es entero positivo y es PERFECTO!")
                            else:
                                print(f"El número {numero} es simplemente un entero positivo")
                        else:
                            break

                    
                elif punto=='5':
                    while True:
                        palabra=input("Ingrese una palabra o 0 para terminar: ")
                        if palabra!='0':
                            for i in range(1,11):
                                print(f"{i} {palabra}")
                        else:
                            break

                elif punto=='6':
                    while True:
                        while True:
                            try:
                                edad=int(input("Ingresa tu edad o 0 para terminar: "))
                                if edad>=0:
                                    break
                                else:
                                    print("Debes ingresar obviamente un entero positivo") 
                            except:
                                print("Debes ingresar solo valores positivos")
                        añoA=int(Metodos([]).año())
                        añoI=añoA-edad
                        if edad!=0:
                            for a in range(añoI,añoA+1):
                                print(a)
                        else:
                            break

                elif punto=='7':        
                    tabla=Metodos([1]).tablas()
                    for t in tabla:
                        print(t)
                    input()
                    
                elif punto=='8':                    
                        while True:
                            try:                                
                                h=int(input("Ingrese cantidad de horas: "))
                                m=int(input("Ingrese cantidad de minutos: "))
                                s=int(input("Ingrese cantidad de segundos: "))
                                if (h>=0 and h<=24) and (m>=0 and m<=60) and (s>=0 and s<=60):
                                    break
                                else:
                                    print("Debes ingresar valores dentro del rango de tiempo")
                            except:
                                print("Debes ingresar horas, minutos y segundos")
                        
                        for i in range(s,0,-1):
                            print("\rSegundos: ",i, end="", flush=True)
                            time.sleep(1)
                        for j in range(m,0,-1):
                            print("\rMinutos: ",j, end="", flush=True)
                            time.sleep(60)
                        for k in range(h,0,-1):
                            print("\rHoras: ",k,  end="", flush=True)
                            time.sleep(3600)
                        print("Tiempo concluido!")
                        
                elif punto=='9':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número o 0 para terminar: "))
                                if numero>=0:
                                    break
                                else:
                                    print("Debes ingresar solo enteros positivos")
                            except:
                                print("Debes ingresar solo valores enteros positivos")
                        if numero!=0:
                            linea=""
                            for i in range(-1,numero,2):
                                linea=f"{i+2} {linea}"
                                print(linea)                                
                        else:
                            break
                    
                elif punto=='10':
                    while True:
                        while True:
                            try:
                                numero=int(input("Ingrese número o 0 para terminar: "))
                                if numero>=0:
                                    break
                                else:
                                    print("Debes ingresar solo enteros positivos")
                            except:
                                print("Debes ingresar solo valores enteros positivos")
                        if numero!=0:
                            linea=""
                            for i in range(1,numero+1,1):
                                linea=f"* {linea}"
                                print(linea)                                
                        else:
                            break
            else:
                break



            
    