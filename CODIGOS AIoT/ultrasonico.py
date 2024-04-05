from hcsr04 import HCSR04
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from time import sleep

# Configura el sensor HCSR04
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=24000)

# Configura el objeto para la pantalla OLED (Ajusta estos pines y dirección I2C según tu hardware)
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Datos personales
nombre = "Laura"
edad = "19"
telefono = "4151880678"
grupo = "GDS0552"

# Ciclo infinito
while True:
    # Obtiene la distancia
    distancia = sensor.distance_cm()

    # Limpia la pantalla OLED
    oled.fill(0)

    # Muestra los datos personales y la distancia en la pantalla OLED
    oled.text("Nombre: " + nombre, 0, 0)
    oled.text("Edad: " + edad, 0, 10)
    oled.text("Teléfono: " + telefono, 0, 20)
    oled.text("Grupo: " + grupo, 0, 30)
    oled.text("Distancia:", 0, 40)
    oled.text(str(distancia) + " cm", 0, 50)

    # Actualiza la pantalla OLED
    oled.show()

    # Espera antes de tomar otra medición
    sleep(1)
