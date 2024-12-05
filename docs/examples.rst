Simple test
------------

Ensure your device works with this simple test.

.. literalinclude:: ../examples/vl53l0x_simpletest.py
    :caption: examples/vl53l0x_simpletest.py
    :linenos:

Multiple VL53L0X on Same I2C Bus
--------------------------------

Copy "../examples/vl53l0x_multiple_sensors.py" to your "CIRCUITPY" drive, then run the script with ``from vl53l0x_multiple_sensors import *``

.. literalinclude:: ../examples/vl53l0x_multiple_sensors.py
    :caption: examples/vl53l0x_multiple_sensors.py
    :linenos:

Continuous mode
----------------

Simple demo of the VL53L0X distance sensor with continuous mode.

.. literalinclude:: ../examples/vl53l0x_simplecontinuous.py
    :caption: examples/vl53l0x_simplecontinuous.py
    :linenos:

Multiple VL53L0X on Same I2C Bus and with continuous mode
-----------------------------------------------------------

Example of how to change the assigned address of multiple VL53L0X sensors on the same I2C bus and use

.. literalinclude:: ../examples/vl53l0x_multiple_sensors_continuous.py
    :caption: examples/vl53l0x_multiple_sensors_continuous.py
    :linenos:

DisplayIO Simpletest
---------------------

This is a simple test for boards with built-in display.

.. literalinclude:: ../examples/vl53l0x_displayio_simpletest.py
    :caption: examples/vl53l0x_displayio_simpletest.py
    :linenos:
