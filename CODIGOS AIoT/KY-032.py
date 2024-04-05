#KY032  AVIODANCE 

from machine import Pin, SoftI2C
from time import sleep
import ssd1306

# Definimos el número de pin para el sensor KY-032
pin_ky032 = 15
pin_ENA = 2

# Configuramos el pin del sensor KY-032 como entrada digital
ky032 = Pin(pin_ky032, Pin.IN)
ena = Pin(pin_ENA, Pin.OUT)
ena.value(1)

# Declaramos un objeto con los pines utilizados para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Rangos de valores del sensor
rango_actual_ky032 = 0

while True:
    # Limpiamos el display
    display.fill(0)

    # Leemos el valor digital del sensor KY-032
    valor_ky032 = ky032.value()

    # Determinamos el rango actual del sensor
    if valor_ky032 == 0:  # Si se detecta un objeto
        rango_actual_ky032 = 0  # Reiniciamos la cuenta
    else:
        rango_actual_ky032 += 1

    # Mostrar mensaje en el display basado en el rango actual
    if rango_actual_ky032 == 0:
        display.text("Objeto detectado", 0, 0)
    elif rango_actual_ky032 > 0 and rango_actual_ky032 <= 10:
        display.text("Rango 1: {}".format(rango_actual_ky032), 0, 0)
    elif rango_actual_ky032 > 10 and rango_actual_ky032 <= 20:
        display.text("Rango 2: {}".format(rango_actual_ky032), 0, 0)
    else:
        display.text("Rango 3: {}".format(rango_actual_ky032), 0, 0)

    # Mostramos el mensaje en el display
    display.show()

    sleep(0.5)  # Espera 0.5 segundos antes de realizar nuevamente el proceso
