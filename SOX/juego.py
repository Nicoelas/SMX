import os
import time
import random

class TratamientoFichero():
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        with open(self.nombre_fichero, "a") as f:
            f.write(line_to_write + "\n")

    def read_file(self):
        with open(self.nombre_fichero, "r") as f:
            print(f.read())

class menu():
    @staticmethod
    def ver_menu():
        os.system('cls')
        print("  ························")
        print("  :  1) Iniciar partida  :")
        print("  :  2) Ver ranking      :")
        print("  :  3) Salir            :")
        print("  ························")
        print("")

    @staticmethod
    def seleccionar():
        seleccion = int(input(""))
        if seleccion == 1:
            j = 1
            while j < 3:
                os.system('cls')
                print("La partida se va a iniciar.")
                time.sleep(1)
                os.system('cls')
                print("La partida se va a iniciar..")
                time.sleep(1)
                os.system('cls')
                print("La partida se va a iniciar...")
                time.sleep(1)
                j += 1
            jugar.juego()
        elif seleccion == 2:
            os.system('cls')
            k = 1
            while k < 3:
                os.system('cls')
                print("Cargando ranking.")
                time.sleep(1)
                os.system('cls')
                print("Cargando ranking..")
                time.sleep(1)
                os.system('cls')
                print("Cargando ranking...")
                time.sleep(1)
                os.system('cls')
                k += 1
            TratamientoFichero("juego.txt").read_file()
            print("")
            while True:
                seleccion1 = input("¿Quieres volver al menú? (Y/N): ")
                if seleccion1 == 'Y':
                    menu.ver_menu()
                    menu.seleccionar()
                    break
                elif seleccion1 == 'N':
                    os.system('cls')
                    print("Saliendo...")
                    os.system('exit')
                    break
                else:
                    os.system('cls')
                    print("Opcion no valida ingresa 'Y' o 'N'")
        elif seleccion == 3:
            os.system('cls')
            print("Saliendo...")
            os.system('exit')
        else:
            os.system('cls')
            print("Las opciones son: '1' '2' '3'")
            print(f"{seleccion} no es valido")

class jugar():
    @staticmethod
    def juego():
        os.system('cls')
        nrandom = random.randint(1, 10)

        njugador = input("Introduce tu nombre: ")
        os.system('cls')
        njuego = int(input(f"{njugador} adivina el numero del 1 al 10: "))

        intentos = 0
        i = 0
        while i < 1:
            if njuego == nrandom:
                os.system('cls')
                intentos += 1
                print(f"Has acertado el numero era: {nrandom}!")
                print(f"Has necesitado {intentos} intentos")
                if intentos == 1:
                    TratamientoFichero("juego.txt").write_file(f"El jugador: {njugador} ha necesitado {intentos} intento")
                else:
                    TratamientoFichero("juego.txt").write_file(f"El jugador: {njugador} ha necesitado {intentos} intentos")
                print("")
                i = i + 1
            else:
                os.system('cls')
                intentos += 1
                print(f"Llevas {intentos} intentos")
                njuego = int(input(f"Vuelve a intentar adivinar el numero del 1 al 10: "))
        print("")
        while True:
            seleccion1 = input("¿Quieres volver al menú? (Y/N): ")
            if seleccion1 == 'Y':
                menu.ver_menu()
                menu.seleccionar()
                break
            elif seleccion1 == 'N':
                os.system('cls')
                print("Saliendo...")
                os.system('exit')
                break
            else:
                os.system('cls')
                print("Opcion no valida ingresa 'Y' o 'N'")
        
if __name__ == "__main__":
    menu.ver_menu()
    menu.seleccionar()
