from machine import Pin
import time

# Configuración del pin del sensor KY-002 Button
pin_sensor = 27  # Pin del sensor conectado al pin 27 del ESP32

# Configuración del pin como entrada con resistencia pull-up interna
sensor_pin = Pin(pin_sensor, Pin.IN, Pin.PULL_UP)

# Variable para almacenar el estado anterior del botón
estado_anterior = 1

try:
    while True:
        # Leer el estado actual del botón
        estado_actual = sensor_pin.value()

        # Verificar si ha habido un cambio de estado y filtrar el rebote
        if estado_actual != estado_anterior:
            time.sleep_ms(10)  # Pequeño retraso para filtrar el rebote
            estado_actual = sensor_pin.value()  # Volver a leer el estado actual

            # Si el estado sigue siendo diferente, mostrar el estado del botón
            if estado_actual != estado_anterior:
                if estado_actual == 0:
                    print("Botón presionado")
                else:
                    print("Botón liberado")

                # Actualizar el estado anterior
                estado_anterior = estado_actual

except KeyboardInterrupt:
    pass
