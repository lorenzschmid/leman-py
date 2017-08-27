import pyb
from ds18x20 import DS18X20
from rn2483 import LoRa


print("Set up DS1820...")

gnd = pyb.Pin('Y11', pyb.Pin.OUT_PP)
gnd.low()
vcc = pyb.Pin('Y9', pyb.Pin.OUT_PP)
vcc.high()

d = DS18X20(pyb.Pin('Y10'))

temperature_read = d.read_temps()

print("Measured Temperature: {}".format(temperature_read))
pyb.LED(1).on()

print("Set up LoRa..."),
debug = False
serial_port = 1
timeout = 5000
tx_data = "Hello!"

lora = LoRa(serial_port, timeout, timeout, debug)
print("Done")
pyb.LED(2).on()


while(1):
    pyb.LED(2).toggle()
    temperature_read = d.read_temps()
    print("Temperature = " + str(temperature_read))
    lora.send_str(str(temperature_read))
    pyb.delay(500)
