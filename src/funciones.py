import os
import time

alumnos:list=[]
opcion:int=0
alumno:str=""
numeracion:int=1
editado:str=""
indice:int=0


"""
Funciones para el programa de lista de alumnos
Creado por: Gregory Rodriguez
"""
def borrarPantalla():
    """
    Función para limpiar la pantalla de la consola
    """
    os.system("cls") if os.name == "nt" else os.system("clear")

def agregarAlumno():
    """
    Función para agregar un alumno a la lista
    
    Verifica si el alumno ya existe antes de agregarlo

    """
    borrarPantalla()
    print("\nAgregar alumno\n")
    alumno=input("\nIndique nombre del alumno a guardar\n").capitalize()
    if alumno in alumnos:
        input("\nAlumno existente\nPresione una tecla para continuar\n")
    else:
        alumnos.append(alumno)
        input("\nAlumno agregado\nPresiona una tecla para continuar . . .\n ")

def mostrarAlumnos():
    """
    Función para mostrar la lista de alumnos guardados
    Verifica si hay alumnos guardados antes de mostrar la lista
    
    """
    borrarPantalla()
    if len(alumnos) == 0:
        input("\nNo hay alumnos guardados\nPresione una tecla para continuar . . .\n")
    else:
        print("\nAlumnos guardados\n")
        numeracion=1
        for a in alumnos:
            print(numeracion,".-",a)
            numeracion+=1
    input("\nPulse alguna tecla para salir . . .\n")

def buscarAlumno():
    """
    Función para buscar un alumno en la lista
    Verifica si el alumno existe en la lista antes de mostrar el resultado
    
    """
    borrarPantalla()
    print("\nBuscar alumno\n")
    alumno=input("\nIndique el alumno a buscar\n").capitalize()
    if alumno in alumnos:
        input("\nAlumno existente en la lista\nPresione una tecla para continuar . . . .\n")
    else:
        input("\nAlumno no encontrado\nPresione una tecla para continuar . . . .\n")

def actualizarAlumno():
    """
    Función para actualizar el nombre de un alumno en la lista
    Verifica si el alumno existe en la lista antes de permitir la actualización
    """
    borrarPantalla()
    print("\nActualizar alumno\n")
    numeracion=1
    for a in alumnos:
        print(numeracion,".- ",a)
        numeracion+=1
    alumno=input("\nIndica alumno a editar\n").capitalize()
    
    if alumno in alumnos:
        editado=input("\nIndique nuevo nombre del alumno\n").capitalize()
        indice=alumnos.index(alumno)
        alumnos[indice]=editado
        input("\nAlumno actualizado\nPresione una tecla para salir . . .\n")
    else:
        input("\nAlumno no existente\nPresione una tecla para salir . . . .\n")


def eliminarAlumno():
    """
    Función para eliminar un alumno de la lista
    Verifica si el alumno existe en la lista antes de permitir la eliminación
    """
    borrarPantalla()
    print("\nEliminar alumno\n")
    numeracion=1
    for a in alumnos:
        print(numeracion,".- ",a)
        numeracion+=1
    alumno=input("\nIndica alumno a eliminar\n").capitalize()
    
    if alumno in alumnos:
        alumnos.remove(alumno)
        input("\nAlumno eliminado\nPresione una tecla para salir . . .\n")
    else:
        input("\nAlumno no existente\nPresione una tecla para salir . . . .\n")


def salir():
    """
    Función para salir del programa
    Limpia la pantalla y muestra un mensaje de despedida antes de cerrar el programa
    """
    borrarPantalla()
    input("\nSaliendo . . . .\nPresione una tecla para continuar. . . . .\n")
    borrarPantalla()
    print("Gracias por usar el programa\n")
    print("Creado por: Gregory Rodriguez\n")
    time.sleep(3)
    borrarPantalla()

def menu():
   """Función para mostrar el menú de opciones al usuario y obtener su selección
Limpia la pantalla antes de mostrar el menú y devuelve la opción seleccionada por el usuario como un entero

"""
   borrarPantalla()
   opcion = int( input("**********Menú*************\n1.- Agregar alumno\n2.- Mostrar lista\n3.- Buscar articulo\n4.- Actualizar articulo\n5.- Eliminar articulo\n6.- Salir\nIndique su opción:\n"))
   return opcion

def diferente():
    """Función para manejar opciones no válidas en el menú
Muestra un mensaje de error al usuario indicando que la opción seleccionada no es válida y espera a que el usuario presione una tecla para continuar"""
    input("\nOpción no existente\nPresione una tecla para continuar . . .\n")

def inicio():
    """Función principal para iniciar el programa de lista de alumnos
Muestra un mensaje de bienvenida al usuario y luego entra en un bucle que muestra el menú de opciones y maneja la selección del usuario hasta que el usuario elige salir del programa
"""
    print("Bienvenido a lista de alumnos\n")

    opcion:int=0

    while opcion != 6:
        
        try:
            opcion = menu()

            match opcion:
                case 1:
                    agregarAlumno()
                case 2:
                    mostrarAlumnos()
                case 3:
                    buscarAlumno()
                case 4:
                    actualizarAlumno()
                case 5:
                    eliminarAlumno()
                case 6:
                    salir()
                case _:
                    diferente()
        except ValueError :
            input("\nDebe introducir un dato valido por teclado\nPresione una tecla para continuar . . .\n") 
        except Exception as e:
            input(f"\nOcurrió un error: {e}\nPresione una tecla para continuar . . .\n")


