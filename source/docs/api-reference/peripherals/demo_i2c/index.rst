安信可 I2C示例参考
=============

***********
Example 
***********
Ai-WB2 Series SoC Module Reads SHT30 Temperature and Humidity Sensor via I²C Bus

Hardware Setup and Wiring
::::::::::

+---------------------------------+--------------------------------------------+
| Ai-WB2 Series SoC Module Pinout |Peripheral Pinout                           |
+=================================+============================================+
| IO12                            |  SCL                                       | 
+---------------------------------+--------------------------------------------+
| IO3                             |  SDA                                       |
+---------------------------------+--------------------------------------------+
|3V3                              |  VCC                                       |
+---------------------------------+--------------------------------------------+
|GND                              |  GND                                       |
+---------------------------------+--------------------------------------------+

Build and Flash
::::::::::
``shell``

``make -j``

``make flash``


Run
::::::

.. image:: img/demo.jpg


Logic Analyzer Output
::::::

.. image:: img/logic_analyzer.jpg


Troubleshooting
:::::::::

For any technical queries, please open an [issue](https://github.com/Ai-Thinker-Open/Ai-Thinker-WB2/issues) on GitHub. We will get back to you soon.