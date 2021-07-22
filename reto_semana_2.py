
def cliente(informacion:dict)->dict:
    edad = informacion["edad"]
    primer_ingreso = informacion["primer_ingreso"]
    if primer_ingreso == True:
        if edad > 18:
            atraccion:str = str("X-Treme")
            total_boleta = (20000-(20000*0.05))
            apto = bool(True)
        elif edad >= 15 and edad <= 18:
            atraccion:str = str("Carros chocones")
            total_boleta = (5000-(5000*0.07))
            apto = bool(True)
        elif edad >= 7 and edad < 15:
            atraccion:str = str("Sillas voladoras")
            total_boleta = (10000-(10000*0.05))
            apto = bool(True)
        else:
            atraccion:str = str("N/A")
            total_boleta:str = str("N/A")
            apto = bool(False)
    elif primer_ingreso == False:
        if edad > 18:
            atraccion:str = str("X-Treme")
            total_boleta = (20000)
            apto = bool(True)
        elif edad >= 15 and edad <= 18:
            atraccion:str = str("Carros chocones")
            total_boleta = (5000)
            apto = bool(True)
        elif edad >= 7 and edad < 15:
            atraccion:str = str("Sillas voladoras")
            total_boleta = (10000)
            apto = bool(True)
        else:
            atraccion:str = str("N/A")
            total_boleta:str = str("N/A")
            apto = bool(False)
    persona={
        "nombre" : informacion["nombre"],
        "edad" : informacion["edad"],
        "atraccion" : atraccion,
        "apto" : apto,
        "primer_ingreso" : informacion["primer_ingreso"],
        "total_boleta" : total_boleta
    }
    return persona

informacion = {
    'id_cliente':1,
    'nombre':'Johana Fernandez',
    'edad':20,
    'primer_ingreso':True

}

print(cliente(informacion))

def calcular_sueldo(empleado):
      nombre=empleado['nombre']
      tipo=empleado['tipo'] 
      if tipo=='A':
          sueldo=2500000 
      elif tipo=='D':
          sueldo=3000000 
      else:
          sueldo='N/A'
      
      sueldo_empleado={
          'nombre':nombre,
          'sueldo':sueldo,
          'tipo':tipo
          
                    } 
      return sueldo_empleado           
    
   
    
empleado={
    'id_empleado':1,
    'nombre':'Luis Ojeda',
    'tipo':'D'
}    

print(calcular_sueldo(empleado))
