import matplotlib.pyplot as plt
import numpy as np
import serial
import time

data = []

# Reemplaza "COM5" con el puerto serie correspondiente a tu Arduino.
serialArduino = serial.Serial("COM5", 9600, timeout=1.0)
time.sleep(1)  # Espera 1 segundo para dar tiempo a conectarse

start_time = time.time()
while (time.time() - start_time) < 5:  # Leer datos durante 5 segundos
    try:
        cad = serialArduino.readline().decode('ascii').strip()
        data.append(float(cad))
    except ValueError:
        pass

serialArduino.close()

plt.plot(data)
plt.title('Datos de la función sinusoidal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.show()
