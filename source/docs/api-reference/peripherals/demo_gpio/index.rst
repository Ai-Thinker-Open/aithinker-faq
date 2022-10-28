安信可 GPIO 示例参考
=============

***********
Example 
***********
Ai-WB2 Series SoC Module GPIO usage


Hardware Setup and Wiring
::::::::::

+---------------------------------+--------------------------------------------+
| Ai-WB2 Series SoC Module Pinout |Peripheral Pinout                           |
+=================================+============================================+
| IO14                            |  LED                                       | 
+---------------------------------+--------------------------------------------+
| IO8                             |  Button                                    |
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


Troubleshooting
:::::::::

For any technical queries, please open an [issue](https://github.com/Ai-Thinker-Open/Ai-Thinker-WB2/issues) on GitHub. We will get back to you soon.