import datetime

class Metodos:     
    def __init__(self,datos):
        self.datos=datos
          
    def multiplo(self):            
        es=False            
        if self.datos[0]%self.datos[1]==0:
            es=True
        return es
    
    def entero(self):        
        try:            
            int_valor=int(self.datos[0])
            return True
        except:
            return False
    
    def ppt(self):
        if self.datos[0]!=self.datos[1]:
            ganador=self.datos[0]
            if self.datos[0]+self.datos[1]==3:
                if self.datos[0]==1:
                    ganador=self.datos[1]
            elif self.datos[0]+self.datos[1]==4:
                if self.datos[0]==3:
                    ganador=self.datos[1]
            elif self.datos[0]+self.datos[1]==5:
                if self.datos[0]==2:
                    ganador=self.datos[1]
            if ganador==self.datos[0]:
                return ["Ganaste !!!",1,0]
            else:
                return ["Upss! Perdiste",0,1]
        else:
            return ["Empate!",1,1]
    
    def vinos(self):
        vino=""
        if self.datos[0]=='1':
            vino="Vino Tinto"
        elif self.datos[0]=='2':
            vino="Vino blanco"
        elif self.datos[0]=='3':
            vino="Agua"        
        else:
            vino="Elija carne, pescado o Ensalada"
        return vino
    
    def primo(self):
        ceros=0
        divisores=[]
        for divisor in range(1,self.datos[0]+1):
            if self.datos[0]%divisor==0:
                ceros+=1
                divisores.append(divisor)
        if ceros==2:
            return [True,divisores]
        else:
            return [False,divisores]
    
    def calificacion(self):
        estado=""
        if self.datos[1]==0:
            if self.datos[0]>0.0 and self.datos[0]<=0.9:                
                estado="Reprobado"
            elif self.datos[0]>0.9 and self.datos[0]<=2.5:
                estado="Habilitación"
            elif self.datos[0]>2.5 and self.datos[0]<=2.9:
                estado="Habilitación"
            elif self.datos[0]>2.9 and self.datos[0]<=3.5:
                estado="Aprobado Aceptable"
            elif self.datos[0]>3.5 and self.datos[0]<=3.9:
                estado="Aprobado Sigue Mejorando"
            elif self.datos[0]>3.9 and self.datos[0]<=4.5:
                estado="Aprobado Excelente"
            elif self.datos[0]>4.5 and self.datos[0]<=5:
                estado="Aprobado Tienes un gran futuro"
            else:
                estado="Nota fuera de rango"
        elif self.datos[1]==1:
            if self.datos[0]>=4:
                estado="Habilitación Aprobada"
            else:
                estado="Habilitación Reprobada"
        elif self.datos[1]==2:
            if self.datos[0]>=3:
                estado="Habilitación Aprobada"
            else:
                estado="Habilitación Reprobada"
        return estado
    
    def calculoSalarial(self):
        salario=self.datos[0]
        auxTporte=0
        if salario<=1160000:
            auxTporte=140606
        cesantias=((salario+auxTporte)*8.33)/100
        interesCesantias=(cesantias*1)/100
        vacaciones=(salario*4.16)/100
        primaservicio=cesantias
        salud=(salario*12.5)/100
        pension=(salario*16)/100
        riesgosPles=(salario*0.522)/100
        pfiscales=(salario*9)/100
        return [salario,{"Salario":salario,"Auxilio de Tporte":auxTporte,"Cesantías":cesantias,"Intereses Cesantias":interesCesantias,"Vacaciones":vacaciones,"Prima de servecio":primaservicio,"Salud":salud,"Pensión":pension,"Riesgos Profesionales":riesgosPles,"Parafiscales":pfiscales},salario+auxTporte+cesantias+interesCesantias+vacaciones+primaservicio+salud+pension+riesgosPles+pfiscales]

    def tablas(self):
        tabla=[]
        numero=self.datos[0]
        for i in range(1,11):
            tabla.append(f"{numero} x {i} = {numero*i}")
        return tabla
    
    def año(self):        
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year
        
    

    
     