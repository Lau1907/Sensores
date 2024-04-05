import machine
import time

POTE_PIN = 14
RELAY_PIN = 22

# Configuración de los pines
pote = machine.ADC(machine.Pin(POTE_PIN))
relay = machine.Pin(RELAY_PIN, machine.Pin.OUT)

while True:
    # Lectura del potenciómetro
    val = pote.read()

    # Si el valor del potenciómetro supera el 50% del rango, enciende el relé
    if val > 512:  # 50% de 1024 (rango completo del ADC)
        relay.on()
    else:
        relay.off()

    time.sleep(0.1)  # Espera para evitar la lectura continua del potenciómetro