import machine
import time

BUTTON_PIN = 14  # Pin al que está conectado el botón KY-004
RELAY_PIN = 22  # Pin al que está conectado el relé

# Configuración de los pines
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
relay = machine.Pin(RELAY_PIN, machine.Pin.OUT)

while True:
    # Lectura del estado del botón
    button_state = button.value()

    # Si el botón está presionado, enciende el relé
    if button_state == 0:  # El botón está presionado cuando el estado es 0
        relay.on()
    else:
        relay.off()

    time.sleep(0.1)  # Espera para evitar la lectura continua del botón