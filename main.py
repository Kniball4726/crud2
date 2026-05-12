import os

from funciones import actualizarAlumno, agregarAlumno, buscarAlumno, eliminarAlumno, menu, mostrarAlumnos, salir

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


