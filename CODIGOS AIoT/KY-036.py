from machine import Pin
import time

# Configuración de los pines del sensor KY-036 Touch
pin_do = 35  # Pin DO del sensor conectado al pin 35 del ESP32

# Configuración del pin DO como entrada
do_pin = Pin(pin_do, Pin.IN)

try:
    while True:
        # Leer el estado del pin DO (tacto detectado)
        estado_do = do_pin.value()

        # Mostrar el estado DO en la consola
        if estado_do == 1:
            print("Tacto detectado")
        else:
            print("No se detecta tacto")

        # Esperar un breve tiempo antes de volver a leer el estado
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
