from machine import Pin, ADC, PWM
import time

# Configurar el pin para el sensor de frecuencia cardíaca
pin_heartbeat = 34
sensor_heartbeat = ADC(Pin(pin_heartbeat))

# Configurar el pin para el servo
pin_servo = 15
servo = PWM(Pin(pin_servo), freq=50)

def controlar_servo(valor_sensor):
    # Mapear el valor del sensor al rango de movimiento del servo
    angulo = int(valor_sensor / 4)  # Se supone que el valor del sensor está entre 0 y 1023
    # Limitar el ángulo a un rango seguro para el servo (por ejemplo, 0-180 grados)
    angulo = min(max(angulo, 0), 180)
    # Configurar el ángulo del servo
    duty_cycle = int(50 + (angulo / 180) * 90)  # Calcular el ciclo de trabajo para el ángulo
    servo.duty(duty_cycle)  # Establecer el ciclo de trabajo del servo

while True:
    valor_sensor = sensor_heartbeat.read()
    print("Valor del sensor de frecuencia cardíaca:", valor_sensor)
    
    if valor_sensor > 1000:  # Si el valor del sensor es mayor a 500, abrir el servo
        print("Abriendo servo...")
        controlar_servo(180)  # Abrir el servo a 180 grados
    else:  # Si el valor del sensor es menor o igual a 500, cerrar el servo
        print("Cerrando servo...")
        controlar_servo(0)  # Cerrar el servo a 0 grados
    
    time.sleep(0.5)  # Esperar medio segundo antes de leer nuevamente

