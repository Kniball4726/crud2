import os
import time

alumnos:list=[]
opcion:int=0
alumno:str=""
numeracion:int=1
editado:str=""
indice:int=0


def borrarPantalla():
    os.system("cls") if os.name == "nt" else os.system("clear")

def agregarAlumno():
    print("\nAgregar alumno\n")
    alumno=input("\nIndique nombre del alumno a guardar\n").capitalize()
    if alumno in alumnos:
        input("\nAlumno existente\nPresione una tecla para continuar\n")
    else:
        alumnos.append(alumno)
        input("\nAlumno agregado\nPresiona una tecla para continuar . . .\n ")

def mostrarAlumnos():
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
    print("\nBuscar alumno\n")
    alumno=input("\nIndique el alumno a buscar\n").capitalize()
    if alumno in alumnos:
        input("\nAlumno existente en la lista\nPresione una tecla para continuar . . . .\n")
    else:
        input("\nAlumno no encontrado\nPresione una tecla para continuar . . . .\n")

def actualizarAlumno():
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
    input("\nSaliendo . . . .\nPresione una tecla para continuar")
    borrarPantalla()
    print("Gracias por usar el programa\n")
    print("Creado por: Gregory Rodriguez\n")
    time.sleep(3)
    borrarPantalla()

def menu():
    print("**********Menú*************\n1.- Agregar alumno\n2.- Mostrar lista\n3.- Buscar articulo\n4.- Actualizar articulo\n5.- Eliminar articulo\n6.- Salir\nIndique su opción:\n")

def borrarPantalla():
    os.system("cls") if os.name == "nt" else os.system("clear")


borrarPantalla()
print("Bienvenido a lista de alumnos\n")

opcion:int=0

while opcion != 6:
    
    try:
        borrarPantalla()
        menu()
        opcion=int(input("\nIndique una opción\n"))

        match opcion:
            case 1:
                borrarPantalla()
                agregarAlumno()
            case 2:
                borrarPantalla()
                mostrarAlumnos()
            case 3:
                borrarPantalla()
                buscarAlumno()
            case 4:
                borrarPantalla()
                actualizarAlumno()
            case 5:
                borrarPantalla()
                eliminarAlumno()
            case 6:
                borrarPantalla()
                salir()
            case _:
                input("\nOpción no existente\nPresione una tecla para continuar . . .\n")
    except ValueError:
        input("\nDebe introducir un dato valido por teclado\nPresione una tecla para continuar . . .\n") 
    except Exception as e:
        input(f"\nOcurrió un error: {e}\nPresione una tecla para continuar . . .\n")


