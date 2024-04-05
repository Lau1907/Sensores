from machine import Pin, PWM
import time

# Configuración de los pines del sensor KY-016 RGB LED
pinR = 13  # Pin del LED rojo
pinG = 12  # Pin del LED verde
pinB = 14  # Pin del LED azul

# Configuración de los pines como salidas PWM
ledR = PWM(Pin(pinR, Pin.OUT), freq=5000)  # Frecuencia 5000Hz
ledG = PWM(Pin(pinG, Pin.OUT), freq=5000)
ledB = PWM(Pin(pinB, Pin.OUT), freq=5000)

try:
    while True:
        # Rojo
        print("Rojo")
        ledR.duty(1023)
        ledG.duty(0)
        ledB.duty(0)
        time.sleep(1)
        
        # Verde
        print("Verde")
        ledR.duty(0)
        ledG.duty(1023)
        ledB.duty(0)
        time.sleep(1)

        # Azul
        print("Azul")
        ledR.duty(0)
        ledG.duty(0)
        ledB.duty(1023)
        time.sleep(1)

except KeyboardInterrupt:
    # Apagar el LED y liberar los pines al finalizar
    ledR.duty(0)
    ledG.duty(0)
    ledB.duty(0)
    ledR.deinit()
    ledG.deinit()
    ledB.deinit()
