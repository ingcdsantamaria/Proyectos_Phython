#Mi primer CRUD

tareas={
    '01':{
        'descripcion':'ir a mercar',
        'estado':'pendiente',
        'tiempo':60           
    },
    '02':{
        'descripcion':'Estudiar',
        'estado':'pendiente',
        'tiempo':180           
    },
    '03':{
        'descripcion':'Hacer ejercicio',
        'estado':'pendiente',
        'tiempo':50           
    }
    
}

opcion=0
while opcion>=0 and opcion<5:
    
    print("1-Adicionar tareas")
    print("2-Consultar tareas")
    print("3-Actualizar tarea")
    print("4-Eliminar tarea")
    print("5-Salir")
    opcion=int(input("Ingrese una opcion:"))


    def create(tareas,identificador,tareaNueva):
        tareas[identificador]=tareaNueva
    #tareas=create(tareas,identificador,tareaNueva)
        return(tareas)   

    def read(tareas):
            for identificador, tarea in tareas.items():
                print(identificador,'- ',end='')  
                for nombre_atriuto, atributo in tarea.items():
                    print(atributo, ', ', end='')
                    print()


    if opcion==1:
        print()
        print("--->Adicionando tarea")
        identificador=str(input("Ingrese el identificador de la tarea: "))
        descripcion=str(input("Ingrese descripcion de la tarea: "))
        estado=str(input("Ingrese el estado inicial de la tarea: "))
        tiempo=int(input("Ingrese el tiempo de realizacion: "))
        
        tareaNueva={
            'descripcion':descripcion,
            'estado':estado,
            'tiempo':tiempo   
        }

        tareas=create(tareas,identificador,tareaNueva)
        

        #print(create(tareas,identificador,tareaNueva))
    elif opcion==2:
        print() 
        print("-> Listar Tareas")
        print() 
        read(tareas)
    elif  opcion==5:
        
        print("El programa ha finalizado")
    

 



