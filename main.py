import os

from funciones import actualizarAlumno, agregarAlumno, buscarAlumno, eliminarAlumno, menu, mostrarAlumnos, salir, diferente

def inicio():
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

if __name__ == "__main__":
    inicio()