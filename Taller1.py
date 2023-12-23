import xml.etree.ElementTree as ET
import random
from menus import Menu
from metodos import Metodos

class Taller_uno:       
    def __init__(self):
        self.Menu=Menu()
        

    def iniciar(self):
        while True:
            self.Menu.items("Taller1.xml","Ejercicios de decisión")        
            self.Menu.crear()
            root=ET.parse(f"./Talleres/Taller1.xml")
            punto=input("Ingrese ejercicio u 11 para Salir: ")
            if punto!='11':
                enunciado=root.find(f'.//ejercicio[@num="{punto}"]/enun').text
                print(enunciado)    
                if punto=='1':
                    while True:
                        numero=int(input("Ingrese numero o 0 para terminar: "))   
                        if numero!=0:     
                            respupar="No"
                            respuseis="No"
                            respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 6"
                            if Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 6"
                            if Metodos([numero,6]).multiplo():
                                respuseis="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 6"
                            print(respuesta)
                        else:
                            break
                elif punto=='2':
                    while True:
                        numero=int(input("Ingrese numero o 0 para terminar: ")) 
                        if numero!=0:       
                            respupar="No"
                            respuseis="No"
                            respuesta=f"El número {numero} {respupar} es impar y {respuseis} es múltiplo de 5"
                            if not Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es impar y {respuseis} es múltiplo de 5"
                            if Metodos([numero,5]).multiplo():
                                respuseis="Si"
                                respuesta=f"El número {numero} {respupar} es impar y {respuseis} es múltiplo de 5"
                            print(respuesta)
                        else:
                            break
                elif punto=='3':
                    while True:
                        numero=input("Ingrese número o 0 para terminar: ")
                        if numero!='0':
                            while not Metodos([numero]).entero():
                                numero=input("Ingrese número o 0 para terminar: ")
                            print(f"Bienvenido el número {numero} que acabaste de ingresar es entero!!!")
                        else:
                            break
                elif punto=='4':
                    while True:
                        numero=int(input("Ingrese numero o 0 para terminar: ")) 
                        if numero!=0:       
                            respupar="No"
                            respuseis="No"
                            respuesta=f"El número {numero} {respupar} es par y {respuseis} es negativo"
                            if Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es negativo"
                            if numero<0:
                                respuseis="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es negativo"
                            print(respuesta)
                        else:
                            break
                elif punto=='5':
                    while True:
                        numero=int(input("Ingrese numero o 0 para terminar: "))        
                        if numero!=0:
                            respupar="No"
                            respuseis="No"
                            respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 3"
                            if Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 3"
                            if Metodos([numero,3]).multiplo():
                                respuseis="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 3"
                            print(respuesta)
                        else:
                            break
                elif punto=='6':
                    while True:
                        numero=int(input("Ingrese numero o 0 para terminar: "))        
                        if numero!=0:
                            respupar="No"
                            respuseis="No"
                            respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 7"
                            if Metodos([numero,2]).multiplo():
                                respupar="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 7"
                            if Metodos([numero,7]).multiplo():
                                respuseis="Si"
                                respuesta=f"El número {numero} {respupar} es par y {respuseis} es múltiplo de 7"
                            print(respuesta)
                        else:
                            break
                elif punto=='7':        
                    self.Menu.items("ppt.xml","Opciones juego")
                    self.Menu.crear()
                    opciones={1:"Piedra",2:"Papel",3:"Tijeras"}  
                    j1=1
                    j2=0      
                    pts=[0,0]        
                    while j1>0 and j1<4:
                        try:
                            j1=int(input("Ingresa opción: "))
                            j2=random.randint(1,3) 
                            if j1>0 and j1<4:           
                                print(f"Tu: {opciones[j1]} VS Sistema: {opciones[j2]}")            
                                pts[0]+=Metodos([j1,j2]).ppt()[1]
                                pts[1]+=Metodos([j1,j2]).ppt()[2]
                                print(Metodos([j1,j2]).ppt()[0])
                        except:
                            print("Debes ingresar un número")            
                    print(f"Tu puntaje: {pts[0]}")
                    print(f"Puntaje sistema: {pts[1]}")
                    sx=input()
                elif punto=='8':
                    self.Menu.items("combos.xml","Nuestros Combos")
                    self.Menu.crear()
                    rootm=ET.parse("./Talleres/combos.xml")
                    menuop=int(input("Ingrese su combo: "))
                    while menuop>0 and menuop<5:
                        try:
                            enunciadop=rootm.find(f'.//ejercicio[@num="{menuop}"]/enun').text
                            print(enunciadop)
                            menuop=int(input("Ingrese su combo: "))
                        except:
                            print("Debes ingresar un valor entre 1 y 5")
                elif punto=='9':
                    comida={'1':"Carne",'2':"Pescado",'3':"Ensalada"}
                    while True:
                        print(comida)
                        pedido=input("Ingrese opción de pedido o 0 para terminar: ")
                        if pedido!='0':
                            while pedido!='1' and pedido!='2' and pedido!='3':
                                print(Metodos([pedido]).vinos())
                                pedido=input("Ingrese opción de pedido: ")
                            print(f"Su pedido de {comida[pedido]} estará acompañado de {Metodos([pedido]).vinos()}")
                        else:
                            break
                elif punto=='10':
                    itemsalas={1:"Consola", 2:"Juegos 2D", 3:"Juegos 3D", 4:"Realidad Virtual"}
                    rootg=ET.parse("./Talleres/gamer.xml")
                    rootg_node=rootg.getroot()
                    email=rootg_node.find('.//gamer').get('email')
                    password=rootg_node.find('.//gamer').get('password')
                    creditos=rootg_node.find('.//gamer/creditos').text
                    accesos=rootg_node.find('.//gamer/accesos')
                    salas=accesos.findall('sala')
                    nombre=rootg_node.find('.//gamer/nombre').text        
                    while True:
                        ingreso=input("Ya estas registrado? s/n o 0 para terminar: ")
                        if ingreso!='0':
                            if ingreso=='s':            
                                emaili=input("Ingrese su emial: ")
                                passwordi=input("Ingrese su password: ")
                                if email==emaili and password==passwordi:
                                    print(f"** Bienvenido {nombre} **")                
                                    print(f"Tus créditos son: {creditos}")
                                    print("Tiene acceso a las siguientes salas: ")
                                    for sala in salas:                        
                                        print(sala.text)
                                    print("**********************")
                                    print("1.Acceder a sala")
                                    print("2.Adquirir créditos")
                                    op=input("Ingresa op: ")
                                    if op=='1':
                                        opsala=input("Ingresa numero de sala: ")
                                        print(f"{nombre} que gusto verte, la sala {itemsalas[int(opsala)]} te da la bienvenida")
                                    elif op=='2':
                                        if int(creditos)<4:
                                            adcreditos=input("Ingresa cantidad de créditos: ")
                                            while int(creditos)+int(adcreditos)>4:
                                                print("Imposible el limite de creditos es 4")
                                                adcreditos=input("Ingresa cantidad de créditos: ")
                                            newcreditos=int(creditos)+int(adcreditos)
                                            rootg_node.find('.//gamer/creditos').text=str(newcreditos)                        
                                            for clave, valor in itemsalas.items():
                                                if clave>int(creditos) and clave<=newcreditos:
                                                    sala_element = ET.Element('sala')
                                                    sala_element.text = f"{str(clave)}.{valor}"
                                                    sala_element.set('id', str(clave))                            
                                                    accesos.append(sala_element)
                                            rootg.write('./Talleres/gamer.xml')
                                        else:
                                            print("Tienes todos los créditos y puedes acceder a todas nuestras salas")

                                else:
                                    print("Usuario no registrado")
                        else:
                            break
            else:
                break



            
    