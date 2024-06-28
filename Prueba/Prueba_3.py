import os
import json

#https://github.com/Tomarts2020/Pruba-3-D-.git

#Agregar Categoría

def agregar_nueva_categoria(nombre:str):
    with open("biblioteca.json", "r") as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        nueva_categoria = (

            "IDcategoria": len(LEER_JSON["categoria"])+1
            "nombre" = nombre
        )
        
    LEER_JSON["categoria"].append(nueva_categoria)
    with open("biblioteca.json", "w") as ESCRITURA_JSON:
        json.dump(LEER_JSON, ESCRITURA_JSON,indent=4)

#Editar Categoría

def Editar_Categoría(id_categoria:int):
    with open ("biblioteca.json", "r") as LECTURA_JSON:
        LEER_JSON =json.load(LECTURA_JSON)
    contador = 0
    for i in LEER_JSON["categoria_id"] == id_categoria:
        print(1) 
        break
    contador = contador+1
    LEER_JSON["categoria"][contador]["nombre"]= input("Ingrese un nombre para categoría")
    with open("biblioteca.json", "w") as ESCRITURA_JSON:
        json.dump (LEER_JSON, ESCRITURA_JSON, ident=4)

#Eliminar categorias

def eliminar_categoria(eliminar_categoria:int):
    with open("biblioteca.json", "w") as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        contador = 0
        for i in LEER_JSON["categoria"]:
            if i ["categoria_id"]: eliminar_categoria
            print(1)
            break
        contador = contador +1
        del LEER_JSON["categoria_id"][contador]
    with open("biblioteca.json", "w") as ESCRITURA_JSON:
        json.dump(LEER_JSON, LECTURA_JSON, indent=4)

#Buscar categorias
        
def buscar_categorias(buscar_categoria:int):
    with open("biblioteca.json", "w") as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        for i in LEER_JSON["categoria"]:
            print(1)

        
print("*******************")
print("*** MUNDO LIBRO ***")
print("*******************")

print("[1] - Mantenedor de categorias")
print("[2] - Reportes")
print("[3] - Salir")

opc = int(input("Ingresar una opcion:"))
    
if opc == 1:
    print("***************************")
    print("** MANTENEDOR CATEGORIAS **")
    print("***************************")
    print("[1] - Agregar categoria")
    print("[2] - Editar categoria")
    print("[3] - Eliminar categoria")
    print("[4] - Buscar categoria")
    print("[5] - Volver")
    opc_categoria = int(input("Ingrese una opcion"))     
elif opc == 2:
    print("************************************************")
    print("** LIBRO           CANTIDAD DE VECES PRESTADO **")
    print("************************************************")
    print("La Casa de Bernarda Alba         2")
    print("La fiesta del Chivo             11")
    print("Don Quijote de la Mancha         2")
    print("La Ciudad y los Perros           5")
elif opc == 3:
    print("Bye :D")

if opc_categoria == 1:
    agregar_nueva_categoria = input("Nombre de la nueva categoria: ")
    function.agregar_nueva_categoria(nombre = agregar_nueva_categoria)

        





 

