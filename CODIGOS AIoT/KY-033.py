from machine import Pin, SoftI2C
from time import sleep
import ssd1306

# Definimos el número de pin para el sensor KY
pin_ky = 15

# Configuramos el pin del sensor KY como entrada digital
ky = Pin(pin_ky, Pin.IN)

# Declaramos un objeto con los pines utilizados para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Rangos de valores del sensor
rango_actual = 0
valor_simulado = 0

while True:
    # Limpiamos el display
    display.fill(0)

    # Leemos el valor digital del sensor KY
    valor = ky.value()

    if valor == 0:  # Si hay obstáculo, reiniciar rango y valor simulado
        rango_actual = 0
        valor_simulado = 0
    else:
        # Incrementar valor simulado y actualizar rango
        valor_simulado += 1
        if valor_simulado > 0 and valor_simulado <= 10:
            rango_actual = 1
        elif valor_simulado > 10 and valor_simulado <= 20:
            rango_actual = 2
        elif valor_simulado > 20:
            rango_actual = 3

    # Mostrar mensaje en el display basado en el rango actual
    if rango_actual == 0:
        display.text("Obstáculo!!", 0, 0)
    elif rango_actual == 1:
        display.text("Rango 1: {}".format(valor_simulado), 0, 0)
    elif rango_actual == 2:
        display.text("Rango 2: {}".format(valor_simulado), 0, 0)
    elif rango_actual == 3:
        display.text("Rango 3: {}".format(valor_simulado), 0, 0)

    # Mostramos el mensaje en el display
    display.show()

    sleep(0.5)  # Espera 0.5 segundos antes de realizar nuevamente el proceso
