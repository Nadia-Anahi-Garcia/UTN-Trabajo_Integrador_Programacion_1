# GESTIÓN DE DATOS DE PAÍSES
# Este programa permite administrar información de países:
# agregar, actualizar, buscar, filtrar, ordenar y mostrar estadísticas.
# ------------------------------------------------------------

import csv  # módulo para leer/escribir CSV
import os   # módulo para operaciones del sistema de archivos

# Constantes
# ----------------------------------------------------------------
FILE_NAME = "gestion.paises.csv"  # nombre del archivo donde se guardan los datos
ENCODING = "utf-8"                # codificación del archivo CSV

# Constantes que representan las columnas del archivo CSV
# Se utilizan índices para facilitar el acceso a los datos
COL_NOMBRE_PAIS = "NOMBRE"        # clave para el nombre del país en los diccionarios
COL_POBLACION = "POBLACION"       # clave para la población
COL_SUPERFICIE = "SUPERFICIE"     # clave para la superficie
COL_CONTINENTE = "CONTINENTE"     # clave para el continente


# Funciones auxiliares
# ----------------------------------------------------------------
def mostrar_listado_paises(paises):
    """ Muestra el catálogo de paises."""
    if len(paises) > 0:                        #verifica si hay elementos en la lista
        mostrar_catalogo_titulo()              # muestra el encabezado del catálogo
        for pais in paises:                    # recorre cada país en la lista
            # imprime cada campo con formato: nombre, población, superficie, continente
            print("{:<25} {:>10} {:>17} {:>12}".format(
                pais[COL_NOMBRE_PAIS].capitalize(), 
                pais[COL_POBLACION],
                pais[COL_SUPERFICIE], 
                pais[COL_CONTINENTE].capitalize()))
    else:
        print("No existen resultados.")         # mensaje si no hay países
    
    mostrar_y_esperar_tecla()                   # pausa para que el usuario vea el listado

def validar_entero_mayor_que_cero(valor):
    """ Valida que el valor sea un entero mayor que cero. """
    return valor.isdigit() and int(valor) > 0   

def validar_entero_mayor_igual_que_cero(valor):
    """ Valida que el valor sea un entero mayor o igual que cero. """
    return valor.isdigit() and int(valor) >= 0  

def dibujar_linea(separador="-", longitud=70):
    """ Dibuja una línea en pantalla con el separador y longitud indicados. """
    print(separador * longitud)                  

def mostrar_y_esperar_tecla(mensaje=""):
    """ Muestra un mensaje y espera a que el usuario presione Enter. """
    print(mensaje)                               
    input("Presione Enter para continuar...")    

def mostrar_titulo_opcion(mensaje):
    """ Muestra un título de opción en pantalla. """
    print("\n"*2)                                
    dibujar_linea()                              
    print(mensaje)                               
    dibujar_linea()                              
    
def mostrar_catalogo_titulo():
    """ Muestra el encabezado del catálogo. """
    print("\n\n{:<25} {:>10} {:>17} {:>12}".format(
        COL_NOMBRE_PAIS, COL_POBLACION, f"{COL_SUPERFICIE}(km²)", COL_CONTINENTE))
    dibujar_linea()                              
            
def mostrar_menu():
    """ Muestra el menú principal y gestiona las opciones del usuario. """
    while True:                                  # bucle principal del menú
        print("\n===================================")
        print("     Gestión de Datos de Países     ")
        print("===================================")
        print("Menú de opciones:")
        print("1. Ingresar país")
        print("2. Actualizar población y superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")
          
        opcion = input("Seleccione una opción (1-7): ").strip()  
        match opcion:
            case "1":
                ingresar_paises()                  
            case "2":
                actualizar_poblacion_y_superficie() 
            case "3":
                buscar_pais_por_nombre()            
            case "4":
                filtrar_paises()                   
            case "5":
                ordenar_paises()                    
            case "6":
                mostrar_estadisticas()              
            case "7":
                print("Saliendo del programa. Gracias por usar nuestro gestor de países en Linea!")
                break                              # rompe el bucle y sale
            case _:
                mostrar_y_esperar_tecla("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

def buscar_pais(paises, pais_a_buscar):
    """Busca un pais en la lista de paises. Devuelve el pais si lo encuentra, o None si no. """
    busqueda = pais_a_buscar.lower()
    for pais in paises:                         # recorre lista de diccionarios
        if busqueda == pais[COL_NOMBRE_PAIS].lower():
            return pais
        
    return None                                 # devuelve None si no encontró

def buscar_paises(paises, texto_a_buscar):
    """Busca un pais en la lista de paises. Devuelve el pais si lo encuentra, o None si no. """
    busqueda = texto_a_buscar.lower()
    resultados = []
    for pais in paises:                         
        if  busqueda == pais[COL_NOMBRE_PAIS].lower() or \
            busqueda in pais[COL_NOMBRE_PAIS].lower():
            resultados.append(pais)
        
    return resultados

def filtrar_paises_por_continente():
    """ Filtra los países por continente. """
    mostrar_titulo_opcion("Filtar paises por continente")
    continente_a_filtrar = input("Ingrese el continente para filtrar: ").strip()  
    paises = leer_paises_desde_archivo()         # carga todos los países desde el archivo
    
    paises_filtrados = []
    for pais in paises:                           # compara continente (case-insensitive)
        if pais[COL_CONTINENTE].lower() == continente_a_filtrar.lower():
            paises_filtrados.append(pais)         # añade a la lista filtrada
            
    mostrar_listado_paises(paises_filtrados)      # muestra resultados
    
def filtrar_paises_por_rango_poblacion():
    """ Filtra los países por rango de poblacion. """
    mostrar_titulo_opcion("Filtar paises por rango de poblacion")
    desde = input("Ingrese el valor mínimo de población: ").strip()  # valor mínimo
    hasta = input("Ingrese el valor máximo de población: ").strip()  # valor máximo
    
    # valida que ambos sean enteros >= 0
    if not (validar_entero_mayor_igual_que_cero(desde) and validar_entero_mayor_igual_que_cero(hasta)):
        mostrar_y_esperar_tecla("Valores inválidos. Deben ser números enteros positivos.\n")
        return
    
    desde = int(desde)                            # convierte a entero
    hasta = int(hasta)
    
    if desde > hasta:                             # valida rango lógico
        mostrar_y_esperar_tecla("El valor mínimo no puede ser mayor que el máximo.\n")
        return
    
    paises = leer_paises_desde_archivo()          # carga datos
    
    paises_filtrados = []
    for pais in paises:
        if pais[COL_POBLACION] >= desde and pais[COL_POBLACION] <= hasta:
            paises_filtrados.append(pais)         # añade si está en el rango
            
    mostrar_listado_paises(paises_filtrados)      # muestra resultados
    
def filtrar_paises_por_rango_superficie():
    """ Filtra los países por rango de superficie. """
    mostrar_titulo_opcion("Filtar paises por rango de superficie")
    desde = input("Ingrese el valor mínimo de superficie: ").strip()  # mínimo superficie
    hasta = input("Ingrese el valor máximo de superficie: ").strip()  # máximo superficie
    
    # validar valores numéricos
    if not (validar_entero_mayor_igual_que_cero(desde) and validar_entero_mayor_igual_que_cero(hasta)):
        mostrar_y_esperar_tecla("Valores inválidos. Deben ser números enteros positivos.\n")
        return
    
    desde = int(desde)                            # convertir a entero
    hasta = int(hasta)
    
    if desde > hasta:                             # validar rango lógico
        mostrar_y_esperar_tecla("El valor mínimo no puede ser mayor que el máximo.\n")
        return
    
    paises = leer_paises_desde_archivo()          # leer archivo
    
    paises_filtrados = []
    for pais in paises:
        if pais[COL_SUPERFICIE] >= desde and pais[COL_SUPERFICIE] <= hasta:
            paises_filtrados.append(pais)         # agrega si cumple rango
            
    mostrar_listado_paises(paises_filtrados)      # mostrar lista filtrada
    
def ordenamiento_burbuja(lista, columna, desc=False):
    """ Ordena la lista usando el algoritmo burbuja según la columna indicada. """
    lista_ordenada = lista.copy()             # copia para no modificar original
    n = len(lista_ordenada)                   # longitud de la lista
    
    for i in range(n):
        for j in range(0, n - i - 1):
            a = lista_ordenada[j][columna]            # valor actual
            b = lista_ordenada[j + 1][columna]        # siguiente valor
            
            if a is None:                             # saltea si valor es None
                continue
            
            condicion_orden = a < b if desc else a > b  # decide comparación según orden
            if b is None or condicion_orden:
                # intercambia elementos si están fuera de orden
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                
    return lista_ordenada                             # devuelve lista ordenada


# ----------------------------------------------------------------
# Funciones de manejo de archivos
# ----------------------------------------------------------------

def verificar_archivo():
    """ Verifica si el archivo existe; si no, lo crea con el encabezado adecuado. """
    try:
        if not os.path.exists(FILE_NAME):         
            with open(FILE_NAME, mode='w', encoding=ENCODING, newline='') as file:
                # crea un escritor con los campos definidos y escribe el encabezado
                writer = csv.DictWriter(file, fieldnames=[COL_NOMBRE_PAIS, COL_POBLACION, COL_SUPERFICIE, COL_CONTINENTE])
                writer.writeheader()
    except (OSError, IOError) as e:
        # lanza excepción con detalle si hay error en disco o sistema de archivos
        raise Exception(f"Ocurrió un error al verificar o crear el archivo: {e}")

def leer_paises_desde_archivo():
    """ Lee los paises desde el archivo y los devuelve como una lista de diccionarios. """
    try:
        verificar_archivo()                        # asegura que el archivo exista
        with open(FILE_NAME, newline="", encoding=ENCODING) as file:
            lector = csv.DictReader(file)          # lector que devuelve diccionarios
            
            paises = []
            for fila in lector:                   # recorre cada fila del CSV
                paises.append({
                    COL_NOMBRE_PAIS: fila[COL_NOMBRE_PAIS],
                    COL_POBLACION: int(fila[COL_POBLACION]),    # convierte población a entero
                    COL_SUPERFICIE: int(fila[COL_SUPERFICIE]),  # convierte superficie a entero
                    COL_CONTINENTE: fila[COL_CONTINENTE]        # continente como string               
                })
                
            return paises                           # devuelve lista de diccionarios
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")  # mensaje si no existe (no debería ocurrir)
    except ValueError as e:
        print(f"Error de formato en los datos: {e}")# mensaje si hay datos mal formateados
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}") # captura otros errores
    
    return []                                       # devuelve lista vacía ante fallo
    
def agregar_pais_a_archivo(pais, poblacion, superficie, continente):
    """ Agrega un nuevo título al archivo. """
    verificar_archivo()                             # asegura existencia del archivo
    with open(FILE_NAME, mode='a', encoding=ENCODING, newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=[COL_NOMBRE_PAIS, COL_POBLACION, COL_SUPERFICIE, COL_CONTINENTE])
        escritor.writerow({
            COL_NOMBRE_PAIS: pais,                  # escribe nombre
            COL_POBLACION: poblacion,               # escribe población
            COL_SUPERFICIE: superficie,             # escribe superficie
            COL_CONTINENTE: continente              # escribe continente
        })
        
def guardar_paises_en_archivo(paises):
    """ Guarda la lista de títulos en el archivo, sobrescribiendo el contenido existente. """
    verificar_archivo()                             
    with open(FILE_NAME, mode="w", newline="", encoding=ENCODING) as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=[COL_NOMBRE_PAIS, COL_POBLACION, COL_SUPERFICIE, COL_CONTINENTE])
        escritor.writeheader()                     # reescribe encabezado
        escritor.writerows(paises)                 # escribe todas las filas desde la lista


# ----------------------------------------------------------------
# Funciones principales del programa
# ----------------------------------------------------------------  

def ingresar_paises():
    """ Permite ingresar paises al catálogo. """
    mostrar_titulo_opcion("Ingresar países al catálogo")  # título de la opción
    cantidad = input("Ingrese la cantidad de países: ")   # lee cantidad a ingresar
    if not validar_entero_mayor_que_cero(cantidad): # valida que sea entero > 0
        mostrar_y_esperar_tecla("Cantidad inválida. Debe ser un número entero positivo.\n")
        return

    cantidad = int(cantidad)                              # convierte a entero el numero ingresado por el usuario

    paises_existentes = leer_paises_desde_archivo()       # carga países actuales

    for i in range(cantidad):                             # bucle para cada país a ingresar
        
        nombre_pais = input(f"Ingrese el nombre del país ({i+1}/{cantidad}): ").strip()  # lee nombre
        if nombre_pais == "":                            # nombre no puede quedar vacío
            mostrar_y_esperar_tecla("El nombre no puede estar vacío.\n")
            return

        if buscar_pais(paises_existentes, nombre_pais) is not None:  # verifica duplicado
            mostrar_y_esperar_tecla(f"El país '{nombre_pais}' ya existe en el catálogo.\n")
            return

        poblacion = input("Ingrese la población del país: ").strip()  # lee población
        if not validar_entero_mayor_que_cero(poblacion):        # valida población
            mostrar_y_esperar_tecla("Población inválida. Debe ser un número entero positivo.\n")
            return

        superficie = input("Ingrese la superficie del país (km²): ").strip() # lee superficie
        if not validar_entero_mayor_que_cero(superficie):       # valida superficie
            mostrar_y_esperar_tecla("Superficie inválida. Debe ser un número entero positivo.\n")
            return

        continente = input("Ingrese el continente del país: ").strip() # lee continente
        if continente == "":                                           # continente no vacío
            mostrar_y_esperar_tecla("Continente no puede estar vacío.\n")
            return
        
        if (continente.lower() not in ["america", "europa", "asia", "africa", "oceania"]):
            mostrar_y_esperar_tecla("Debes ingresar un continente valido.\n")
            return

        try:
            # guarda en archivo y agrega a la lista en memoria
            agregar_pais_a_archivo(nombre_pais.capitalize(), int(poblacion), int(superficie), continente.capitalize())
            paises_existentes.append({
                COL_NOMBRE_PAIS: nombre_pais,
                COL_POBLACION: int(poblacion),
                COL_SUPERFICIE: int(superficie),
                COL_CONTINENTE: continente
            })

            print(f"País '{nombre_pais}' agregado exitosamente.\n")  # confirma agregado
        except Exception as e:
            print(f"Ocurrio un error al guardar País '{nombre_pais}': {e}")  # muestra error
            
    mostrar_y_esperar_tecla()                                      # pausa final

def actualizar_poblacion_y_superficie():
    """ Actualiza la población y superficie de un pais. """
    mostrar_titulo_opcion("Actualizar población y superficie de un país")  # título
    pais_buscado = input(("Ingrese el pais a actualizar:"))                # nombre a buscar
    paises = leer_paises_desde_archivo()                                   # cargar lista
    pais_encontrado = buscar_pais(paises, pais_buscado)         # busca en lista
    if pais_encontrado is None:                                            # mensaje si no existe
        mostrar_y_esperar_tecla("El país no existe en el catálogo.\n")
        return
    
    poblacion = input("Ingrese la población del país: ").strip()           # nueva población
    if not validar_entero_mayor_que_cero(poblacion):                 # validar
        mostrar_y_esperar_tecla("Población inválida. Debe ser un número entero positivo.\n")
        return

    superficie = input("Ingrese la superficie del país (km²): ").strip()   # nueva superficie
    if not validar_entero_mayor_que_cero(superficie):                # validar
        mostrar_y_esperar_tecla("Superficie inválida. Debe ser un número entero positivo.\n")
        return
    
    pais_encontrado[COL_POBLACION] = int(poblacion)                        # actualizar diccionario
    pais_encontrado[COL_SUPERFICIE] = int(superficie)
    
    try:
        guardar_paises_en_archivo(paises)                                  # guarda cambios en archivo
        mostrar_y_esperar_tecla("Población y Superficie actualizadas exitosamente!\n")
    except Exception as e:
        print(f"Ocurrió un error al actualizar Población y Superficie: {e}")  # muestra error
    
def buscar_pais_por_nombre():
    """ Busca un pais por nombre. """
    mostrar_titulo_opcion("Consultar país por nombre")                     # título opción
    pais_consultado = input("Ingrese el país a consultar: ").strip()       # lee nombre
    paises = leer_paises_desde_archivo()                                   # carga lista
    
    paises_encontrados = buscar_paises(paises, pais_consultado)            # busca en lista
    if len(paises_encontrados) > 0:
        mostrar_listado_paises(paises_encontrados)
    else:
        mostrar_y_esperar_tecla(">>> El país consultado no existe en el catálogo. <<<\n")  
        
def filtrar_paises():
    """ Filtra los países por continente, por rango de población o superficie. """
    mostrar_titulo_opcion("Filtrar países por continente, población o superficie")  
    
    print("1. Filtrar por continente")
    print("2. Filtrar por rango de población")
    print("3. Filtrar por rango de superficie")
    opcion = input("Seleccione una opción (1-3): ").strip()         # opción de filtrado
    
    match opcion:
        case "1":
            filtrar_paises_por_continente()                         # filtrar por continente
        case "2":
            filtrar_paises_por_rango_poblacion()                    # por rango de población
        case "3":       
            filtrar_paises_por_rango_superficie()                   # por rango de superficie
        case _:
            mostrar_y_esperar_tecla("Opción no válida.")            # opción inválida

def ordenar_paises():
    """ Ordena países por: Nombre, Población y Superficie (ascendente o descendente)  """
    mostrar_titulo_opcion ("Ordenar Países")   # título opción
    paises = leer_paises_desde_archivo()      # lee datos del archivo
    if not paises:
        mostrar_y_esperar_tecla("No hay países registrados para ordenar.\n")  # sin datos
        return

    print("Seleccione la columna por la que desea ordenar:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion_col = input("Opción (1-3): ").strip()  # lee columna a ordenar

    columnas = {
        "1": COL_NOMBRE_PAIS,
        "2": COL_POBLACION,
        "3": COL_SUPERFICIE
    }
    if opcion_col not in columnas:
        mostrar_y_esperar_tecla("Opción de columna inválida.")  # columna inválida
        return

    print("\nSeleccione el orden:")
    print("1. Ascendente")
    print("2. Descendente")
    opcion_orden = input("Opción (1-2): ").strip()  # lee dirección de orden
    if opcion_orden not in ("1", "2"):
        mostrar_y_esperar_tecla("Opción de orden inválida.")    # orden inválido
        return

    columna = columnas[opcion_col]          # columna seleccionada
    desc = opcion_orden == "2"              # True si descendente

    paises_ordenados = ordenamiento_burbuja(paises, columna, desc)  # ordena
    mostrar_listado_paises(paises_ordenados)                        # muestra resultado

def mostrar_estadisticas():
    """Muestra estadísticas sobre los países"""
    mostrar_titulo_opcion("Estadísticas de Países")  # título sección
    paises = leer_paises_desde_archivo()             # carga datos desde archivo
    
    if not paises:
        mostrar_y_esperar_tecla("No hay países registrados para mostrar estadísticas.\n")
        return
    
    # País con mayor y menor población
    pais_mayor_pob = max(paises, key=lambda x: x[COL_POBLACION])  # usa max por población
    pais_menor_pob = min(paises, key=lambda x: x[COL_POBLACION])  # usa min por población
    
    # Cálculo de promedios
    total_poblacion = sum(pais[COL_POBLACION] for pais in paises)
    total_superficie = sum(pais[COL_SUPERFICIE] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)            # promedio población
    promedio_superficie = total_superficie / len(paises)         # promedio superficie
    
    # Cantidad de países por continente
    paises_por_continente = {}
    for pais in paises:
        continente = pais[COL_CONTINENTE]
        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1
    
    # Mostrar resultados
    print("\nMAYOR Y MENOR POBLACIÓN:")
    print(f"- País con mayor población: {pais_mayor_pob[COL_NOMBRE_PAIS]} ({pais_mayor_pob[COL_POBLACION]:,} habitantes)")
    print(f"- País con menor población: {pais_menor_pob[COL_NOMBRE_PAIS]} ({pais_menor_pob[COL_POBLACION]:,} habitantes)")
    
    print("\nPROMEDIOS:")
    print(f"- Promedio de población: {promedio_poblacion:,.2f} habitantes")
    print(f"- Promedio de superficie: {promedio_superficie:,.2f} km²")
    
    print("\nCANTIDAD DE PAÍSES POR CONTINENTE:")
    for continente, cantidad in paises_por_continente.items():
        print(f"- {continente}: {cantidad} países")
    
    mostrar_y_esperar_tecla("\n") 


# ----------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------
if __name__ == "__main__":
    mostrar_menu()  # inicia la aplicación mostrando el menú

