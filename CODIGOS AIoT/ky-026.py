from machine import Pin
from time import sleep

# Configurar los pines para el motor paso a paso
IN1_PIN = 21
IN2_PIN = 22
IN3_PIN = 23
IN4_PIN = 19

# Configurar los pasos para cada dirección (horario y antihorario)
pasos_horario = [1, 2, 3, 4]
pasos_antihorario = [4, 3, 2, 1]

# Configurar el pin para el sensor de llama KY-026
pin_flame = 34
flame_sensor = Pin(pin_flame, Pin.IN)

while True:
    # Leer el valor del sensor de llama
    valor_sensor = flame_sensor.value()
    print("Valor del sensor de llama:", valor_sensor)
    
    if valor_sensor == 1:  # Si se detecta llama, hacer que el motor avance
        print("Moviendo motor en sentido horario")
        for i in range(512):  # Mover 512 pasos en sentido horario (90 grados)
            for paso in pasos_horario:
                Pin(IN1_PIN, value=paso&1)
                Pin(IN2_PIN, value=paso&2)
                Pin(IN3_PIN, value=paso&4)
                Pin(IN4_PIN, value=paso&8)
                sleep(0.01)
    else:  # Si no se detecta llama, hacer que el motor retroceda
        print("Moviendo motor en sentido anti-horario")
        for i in range(512):  # Mover 512 pasos en sentido antihorario (90 grados)
            for paso in pasos_antihorario:
                Pin(IN1_PIN, value=paso&1)
                Pin(IN2_PIN, value=paso&2)
                Pin(IN3_PIN, value=paso&4)
                Pin(IN4_PIN, value=paso&8)
                sleep(0.01)
    
    sleep(1)  # Esperar un segundo antes de volver a leer el sensor
