安信可 SPI示例参考
=============

***********
Example 
***********
Ai-WB2 Series SoC Module Drives SSD1306 Monochrome 128x64 Resolution OLED Display via SPI

Hardware Setup and Wiring
::::::::::

+---------------------------------+--------------------------------------------+
| Ai-WB2 Series SoC Module Pinout |LED Pinout                                  |
+=================================+============================================+
| IO4                             |  CS                                        | 
+---------------------------------+--------------------------------------------+
| IO5                             |  DC                                        |
+---------------------------------+--------------------------------------------+
|EN/NC                            |  RST                                       |
+---------------------------------+--------------------------------------------+
|IO12                             |  DI                                        |
+---------------------------------+--------------------------------------------+
|IO3                              |  CLK                                       |
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

.. image::  img/logic_analyzer.jpg

See [data.csv] for complete output.
`data.csv详见链接 <https://github.com/Ai-Thinker-Open/Ai-Thinker-WB2/blob/beta/v1.0.5/applications/peripherals/demo_spi/img/data.csv>`__


Troubleshooting
:::::::::

For any technical queries, please open an [issue](https://github.com/Ai-Thinker-Open/Ai-Thinker-WB2/issues) on GitHub. We will get back to you soon.