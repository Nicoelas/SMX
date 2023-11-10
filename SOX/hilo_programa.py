import subprocess
import time

def start_program():
    while True:
        print("Programa ejecutando...")
        time.sleep(1)

if __name__ == "__main__":
    subprocess.run(["/usr/bin/python3", "hilo_proceso.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

    print("Proceso en segundo plano")
