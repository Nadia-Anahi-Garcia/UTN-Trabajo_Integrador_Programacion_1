# Gestión de Datos de Países

## Universidad Tecnológica Nacional (UTN)
**Carrera:** Tecnicatura Universitaria en Programación  
**Materia:** Programación I  
**Modalidad:** A Distancia  
**Año lectivo:** 2025  

**Profesores:**  
- Cinthia Rigoni 
- Brian Lara (comision 3)
- Matias Torres (comision 5)

---

## Integrantes
- **Elisabeth Cordero Campero** – Comisión 3  
- **Nadia Anahi García** – Comisión 5  

---

## Descripción del Proyecto
Este proyecto corresponde al **Trabajo Práctico Integrador (TPI)** de la materia **Programación I** de la **Tecnicatura Universitaria en Programación – UTN**.  
El sistema fue desarrollado en **Python** y tiene como objetivo principal la **gestión de información de países** a partir de un archivo CSV.  

El programa permite realizar operaciones como:
- Cargar nuevos registros.  
- Buscar países por nombre (coincidencia exacta o parcial).  
- Filtrar por continente, población o superficie.  
- Ordenar datos mediante el método de **Burbuja (Bubble Sort)**.  
- Calcular estadísticas básicas del conjunto de datos.

El trabajo busca integrar los principales conceptos teóricos de la materia: **listas, diccionarios, funciones, condicionales, ordenamientos y manejo de archivos.**

---

## Funcionalidades Principales
- **Carga y modificación de países.**  
- **Búsqueda exacta o parcial.**  
- **Filtros personalizados.**  
- **Ordenamientos por nombre, población o superficie (asc/desc).**  
- **Cálculo de estadísticas:** país con mayor/menor población, promedio de población total y cantidad por continente.  
- **Formato visual mejorado:** uso de separadores de miles y presentación tabular.  

---

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

- **GestionDatosPaises.py** → Código principal del sistema.  
  Contiene las funciones para carga, búsqueda, filtrado, ordenamiento y estadísticas.  

- **gestion.paises.csv** → Archivo de datos con la información de los países.  
  Es utilizado para almacenar y recuperar la información del programa.  

- **README.md** → Documento descriptivo del proyecto, con información técnica y académica.  


---

## Instrucciones de Ejecución
1. Asegurarse de tener instalado **Python 3.10 o superior**.  
2. Clonar o descargar este repositorio.  
   ```bash
   git clone https://github.com/usuario/gestion-paises.git
Colocar el archivo gestion.paises.csv en la misma carpeta del programa.

Ejecutar el sistema desde la terminal o un entorno de desarrollo:

bash
Copiar código
python GestionDatosPaises.py
Seguir las opciones del menú interactivo para utilizar las distintas funciones.

Librerías de Terceros
El programa utiliza solo librerías estándar de Python, por lo que no requiere instalación de paquetes externos.
Se emplean módulos incorporados como:

csv → para lectura y escritura de archivos.

os → para limpieza de pantalla y manejo de rutas.

Enlaces Importantes
Video de presentación del proyecto: https://youtu.be/fuh3kSpegFo

Repositorio del proyecto en GitHub: https://github.com/usuario/gestion-paises

## Ejemplo de Entrada y Salida

### Ejemplo de archivo de entrada (`gestion.paises.csv`)
```csv
NOMBRE,POBLACION,SUPERFICIE,CONTINENTE
Argentina,45000051,2780400,America
Brasil,212559417,8515767,America
India,1400000000,3287263,Asia
Francia,67390000,551695,Europa

-----------------------------------------------
Nombre                 Población       Superficie     Continente
-----------------------------------------------
Argentina              45.000.051      2.780.400      America
Brasil                212.559.417      8.515.767      America
Francia                67.390.000        551.695      Europa
India               1.400.000.000      3.287.263      Asia
-----------------------------------------------
Total de países registrados: 4
Promedio de población: 431.987.617
País con mayor población: India
País con menor población: Francia
```


### Metodología de Ordenamiento
El sistema implementa el **método de burbuja (Bubble Sort)** para ordenar la lista de países según distintos criterios.  
Este algoritmo compara pares de elementos adyacentes e intercambia sus posiciones hasta que toda la lista queda ordenada.  
El usuario puede seleccionar si desea un **orden ascendente o descendente**, aplicable a nombre, población o superficie.

### Estadísticas Calculadas
El programa permite obtener información resumida del conjunto de datos, entre ellas:
- País con **mayor** y **menor población**.  
- **Promedio general** de población.  
- **Superficie total y promedio** de los países registrados.  
- **Cantidad de países por continente.**

### Bibliografía y Fuentes
- Material teórico de la cátedra *Programación I – UTN FRBA* (Unidades 4 y 5).  
- Documentación oficial de Python: [https://docs.python.org/3/](https://docs.python.org/3/)  
- CSV File Reading and Writing – Python Docs.  
- W3Schools – *Python Tutorial*.  
- Programiz – *Python Lists and Dictionaries*.  



