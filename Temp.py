from w1thermsensor import W1ThermSensor
def temp_get():
    sensor = W1ThermSensor()
    cel = sensor.get_temperature()
    far = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    kel = sensor.get_temperature(W1ThermSensor.KELVIN)
    
    return cel, far, kel
print(list(temp_get()))

#print("Temp in Celsius:",cel)
#print("Temp in Fahrenheit:",far)
#print("Temp in Kelvin:",kel)