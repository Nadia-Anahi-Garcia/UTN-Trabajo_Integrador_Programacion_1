Gestión de Datos de Países
Descripción General

Este proyecto corresponde al Trabajo Práctico Integrador (TPI) de la materia Programación I de la Tecnicatura Universitaria en Programación – UTN.
El sistema fue desarrollado en Python y permite la gestión de información de países a través de operaciones de carga, búsqueda, filtrado, ordenamiento y análisis estadístico.
Los datos se almacenan y manipulan en un archivo CSV, utilizando estructuras de datos como listas y diccionarios.

Objetivos del Proyecto

Aplicar los conceptos teóricos de programación estructurada.

Implementar funciones modulares, condicionales y validaciones de entrada.

Practicar el manejo de archivos (lectura y escritura CSV).

Organizar y analizar información mediante algoritmos de ordenamiento y cálculos estadísticos.

Características Principales

Carga de países: ingreso de datos con validaciones (nombre, población, superficie, continente).

Actualización: modificación de población y superficie existentes.

Búsqueda: localización de países por nombre (coincidencia exacta o parcial).

Filtros: por continente, rango de población o superficie.

Ordenamiento: mediante el método de burbuja, con posibilidad de elegir columna y orden (asc/desc).

Estadísticas: cálculo del país con mayor/menor población, promedios y cantidad por continente.

Estructura del Proyecto
├── GestionDatosPaises.py     # Código principal del sistema
├── gestion.paises.csv        # Archivo de datos (persistencia)
├── README.md                 # Documentación del proyecto

Ejecución

Asegurarse de tener Python 3.10+ instalado.

Descargar los archivos del repositorio.

Ejecutar el programa desde la terminal:

python GestionDatosPaises.py


Seguir las opciones del menú interactivo.

Ejemplo de Datos (CSV)
NOMBRE,POBLACION,SUPERFICIE,CONTINENTE
Chile,6554,2547,America
India,84000041,9541,Asia
Francia,4558,1587,Europa
Argentina,45000051,5487,America

Metodología de Ordenamiento

El sistema implementa el método de burbuja (Bubble Sort), que compara pares de elementos adyacentes y los intercambia hasta ordenar completamente la lista según el criterio seleccionado (nombre, población o superficie).

Estadísticas Calculadas

País con mayor y menor población.

Promedio de población y superficie total.

Cantidad de países por continente.

Integrantes

Elisabeth Cordero Campero (Comisión 3)

Nadia García (Comisión 5)

Bibliografía y Fuentes

Material teórico de la cátedra Programación I – UTN FRBA (Unidades 4 y 5).

Documentación oficial de Python: https://docs.python.org/3/

CSV File Reading and Writing – Python Docs.

Guía de Estructuras de Datos: Listas y Diccionarios (UTN Virtual).
