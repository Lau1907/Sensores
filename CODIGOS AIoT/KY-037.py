from machine import ADC, Pin
import time

# Configuración del pin del sensor KY-037 Big Sound
pin_out = 36  # Pin analógico A0 en ESP32

# Inicializar el pin como entrada analógica
adc = ADC(Pin(pin_out))
adc.atten(ADC.ATTN_11DB)  # Configurar atenuación para 11dB

try:
    while True:
        # Leer el valor del sensor
        valor_sensor = adc.read()

        # Imprimir el valor en la consola
        print("Valor del sensor:", valor_sensor)

        # Esperar un breve tiempo antes de volver a leer el valor
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
