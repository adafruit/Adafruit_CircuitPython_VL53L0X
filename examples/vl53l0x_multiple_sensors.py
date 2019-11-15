"""
Example of how to use the adafruit_vl53l0x library to change the assigned address of
multiple VL53L0X sensors on the same I2C bus. This example only focuses on 2 VL53L0X
sensors, but can be modified for more. BE AWARE: a multitude of sensors may require
more current than the on-board 3V regulator can output (typical current consumption during
active range readings is about 19 mA per sensor).
"""
import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X

#  declare the singleton variable for the default I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor (this
# pin is labeled "XSHUT" on non-Adafruit breakout boards). Default behavior upon
# instantiation is (direction=INPUT) + (pull=None) = LOW output signal
x_shut = [
    DigitalInOut(board.D7),
    DigitalInOut(board.D9)
    ]
# idealy you might want to use an IO extender as these pins are only used to control the
# VL53L0X's power state.

for power_pin in x_shut:
    # make sure these pins are an digital output, not a digital input
    power_pin.switch_to_output(value=False)
    # These pins are active when Low, meaning:
    #   if the output signal is LOW, then the VL53L0X sensor is off.
    #   if the output signal is HIGH, then the VL53L0X sensor is on.
    # (value=False) = LOW output signal; LOW output disables/shutsdown the VL53L0X
# all VL53L0X sensors are now off

# initialize a list to be used for the array of VL53L0X sensors
vl53 = []

# now change the addresses of the VL53L0X sensors
for i, power_pin in enumerate(x_shut):
    # turn on the sensor to allow hardware check
    power_pin.value = True
    # instantiate the VL53L0X sensors on the I2C bus & insert it into the "vl53" list
    vl53.insert(i, VL53L0X(i2c)) # also performs hardware check
    # don't need to change the address of the last VL53L0X sensor
    if i < len(x_shut) - 1:
        # default address is 0x29. Change that to something else
        vl53[i].set_address(i + 0x30) # address assigned should not be already in use
# there is a helpful list of pre-designated I2C addresses for various I2C devices at
# https://learn.adafruit.com/i2c-addresses/the-list
# According to this list 0x30-0x34 are available although the list may be outdated/incomplete.
# you can scan for all I2C devices and detirmine their addresses using:
#   "i2cdetect 1 -y" (without quotes) on a Raspberry Pi terminal or
#   In the python REPR, execute the following commands:
#   >>> import busio
#   >>> i2c = busio.I2C(board.SCL, board.SDA)
#   >>> i2c.try_lock() # if False is returned: something else is using the i2c bus
#   >>> [hex(x) for x in i2c.scan()]
#   >>> i2c.unlock() # free up the bus for something else to use it

def detect_range(count=5):
    """ take count=5 samples """
    while count:
        for index, sensor in enumerate(vl53):
            print('Sensor {} Range: {}mm'.format(index + 1, sensor.range))
        time.sleep(1.0)
        count -= 1

print("""\
    multiple VL53L0X sensors' addresses are assigned properly\n\
    execute detect_range() to read each sensors range readings""")
