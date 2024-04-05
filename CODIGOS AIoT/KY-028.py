from machine import Pin, ADC
import time

# Configurar el pin del sensor KY-028 Digital Temperature
pin_analogico = 34  # Pin AO del sensor conectado al pin 34 del ESP32
pin_digital = 35  # Pin DO del sensor conectado al pin 35 del ESP32

# Configurar el pin DO como entrada
pin_digital = Pin(pin_digital, Pin.IN)

def read_temperature(pin_analogico):
    adc = ADC(Pin(pin_analogico))
    valor_adc = adc.read()
    voltage = valor_adc * 3.3 / 1024  # Convertir valor ADC a voltaje (3.3V en ESP32)
    temperatura = (voltage - 0.5) * 100  # Calcular temperatura en grados Celsius
    return temperatura

try:
    while True:
        # Leer la salida digital para determinar si el sensor está listo
        if pin_digital.value() == 1:
            temperatura = read_temperature(pin_analogico)
            print("Temperatura: {:.2f}°C".format(temperatura))
        else:
            print("Sensor no listo...")
        time.sleep(2)

except KeyboardInterrupt:
    pass
