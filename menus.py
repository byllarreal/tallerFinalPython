import xml.etree.ElementTree as ET

class Menu:
    def items(self,taller, titulo):        
        self.titulo=titulo
        self.taller=taller
    def espacios(self, espas, caracter):
        enblanco=""
        for espa in range(1,espas):
            enblanco+=caracter
        return enblanco       

    
    
    def crear(self):
        root=ET.parse(f"./Talleres/{self.taller}")
        root_node=root.getroot()
        ejercicio=root_node[0]
        max_length = max(len(child.get('num', '') + "." + child.get('nom', '')) for child in ejercicio)
        asteriscos=self.espacios(int((max_length-len(self.titulo))),"*")            
        print(f"***** {self.titulo} {asteriscos}")
        for child in ejercicio:            
            blancos=self.espacios(int((max_length-len(child.get('num', '') + "." + child.get('nom', ''))))," ")            
            if len(blancos)!=0:
                print(f"** {child.get('num','')}.{child.get('nom','')}{blancos}  **")
            else:
                print(f"** {child.get('num','')}.{child.get('nom','')} **")
        

        
    
