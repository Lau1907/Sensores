from machine import Pin, ADC, PWM
import time

sensorPin = 34  # Pin ADC de la ESP32 para el sensor de luz KY-027
ledPin = 2  # Pin GPIO de la ESP32 para el LED

sensor_luz = ADC(Pin(sensorPin))
servo = PWM(Pin(21), freq=50)  # Pin GPIO de la ESP32 para el servo, frecuencia de 50 Hz

def controlar_servo(valor_sensor):
    if valor_sensor > 150:
        # Abrir el servo (angulo 180)
        servo.duty(135)  # Configurar el ciclo de trabajo para el ángulo 180 (135 para 180 grados)
    else:
        # Cerrar el servo (angulo 0)
        servo.duty(45)  # Configurar el ciclo de trabajo para el ángulo 0 (45 para 0 grados)

while True:
    lightLevel = sensor_luz.read()
    print("Nivel de luz:", lightLevel)  # Imprimir el nivel de luz en la consola
    if lightLevel > 1500:
        Pin(ledPin, Pin.OUT).on()  # Encender el LED si el nivel de luz es alto
    else:
        Pin(ledPin, Pin.OUT).off()  # Apagar el LED si el nivel de luz es bajo

    controlar_servo(lightLevel)
    time.sleep(1)  # Esperar un segundo antes de leer nuevamente el sensor
