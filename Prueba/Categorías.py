import json

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
        LEER_JSON = json.load(LECTURA_JSON)
    contador = 0
    for i in LEER_JSON["categoria"]:
        print(1)       

        