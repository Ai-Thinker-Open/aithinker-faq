1. ESP8266系列
==================

1.1 通用AT固件
~~~~~~~~~~~~~~~~

**说明：**

- 特性：操作简单，任何mcu均可直接接入
- UART 默认配置: RX16，TX17，波特率：115200
- 更新时间：2019年12月22日
- 更新说明：v1.7.1.0 AT Firmware，内含 8Mbit 和 32Mbit 两个版本，请客户根据自己产品的flash大小来烧录，串口引脚为TXD,RXD

**固件下载：** `1MB固件(固件号：0884) <https://axk.coding.net/s/34c8a493-8a50-4f70-9fdc-633b4e632504>`__

**固件下载：** `4MB固件(固件号：0883)  <https://axk.coding.net/s/dcd2cba7-a235-4e0a-bea5-88fadcac9ec3>`__

1.2 直连腾讯云AT固件
~~~~~~~~~~~~~~~~~~~

**说明:**

- 特性：可连接腾讯开发平台，Flash 至少2MB才可以烧录
- 更新说明：2020年02月28日更新，串口引脚为 TXD=GPIO15, RXD=GPIO13
- 固件大小：2MB
- UART 默认配置: RX16，TX17，波特率：115200

**固件下载：** `安信可腾讯云固件(固件号：1027) <https://axk.coding.net/s/71c2ad1b-b995-435d-991f-ec4478044fe4>`__

1.3 MQTT透传固件
~~~~~~~~~~~~~~~~

**说明：**

- 特性：支持TLS连接，务必注意通讯引脚为（ txd=GPIO15, rxd=GPIO13），Flash 至少2MB才可以烧录
- 使用说明： `使用指导 <https://docs.ai-thinker.com/_media/esp8266/mqtt%E5%9B%BA%E4%BB%B6%E4%BD%BF%E7%94%A8%E6%8C%87%E5%AF%BC.rar>`__
- 更新时间：2020年2月21日
- 固件大小：2MB
- 更新说明：串口引脚为 TXD=GPIO15, RXD=GPIO13,串口1作为log串口，默认波特率为115200

**点我下载：** `MQTT透传固件(固件号：1030) <https://axk.coding.net/s/7264452d-ac0a-4241-917a-85052ded2e3a>`__

2. ESP32系列
================

2.1 ESP32-S 出厂AT固件
~~~~~~~~~~~~~~~~~~

**说明：**

- 特性：支持MQTT，支持BLE
- 更新时间：2020年2月14日
- 固件大小：4MB
- UART 默认配置: RX16，TX17，波特率：115200

**固件下载：** `ESP32-S默认出厂固件(固件号：1029) <https://axk.coding.net/s/dc381137-542c-436e-a225-de015ff65a3d>`__

2.2 ESP32-SL 出厂AT固件
~~~~~~~~~~~~~~~~~~~~~~~

**说明：**

- 特性：支持MQTT,不支持BLE
- 更新时间：2020年04月20日
- 固件大小：4MB
- UART默认配置：RX16，TX17，波特率：115200

**固件下载：** `ESP32-SL默认出厂固件(固件号：1084) <https://axk.coding.net/s/b43a7c4d-280b-4336-9bc5-c5b1e2695765>`__

2.3 ESP32-S 开发板出厂固件
~~~~~~~~~~~~~~~~~~~~~

**说明：** 
2-S开发板固件 <https://axk.coding.net/s/aa00d771-55d0-4ce0-b6a4-3e54e09f3b0e>`__

3. ESP32-S2系列
================

**说明：**

- 特性：只适用于NodeMCU-32S开发板，非AT固件
- 更新时间：2017年07月05日
- 固件大小：4MB
  
**固件下载：** `ESP3
- 特性：适用于ESP-12K和ESP-12H，
- 固件大小：4MB
- UART 默认配置：RX16，TX17，波特率：115200

**08固件下载：** `ESP32-S2 出厂固件(固件号：1204) <https://axk.coding.net/s/2dc4b06a-f834-44e8-8268-f39b8e4f9beb>`__ (带PSRAM)

**00固件下载：** `ESP32-S2 出厂固件(固件号：1205) <https://axk.coding.net/s/82ce0d42-709e-4b7b-afd7-fee7da666839>`__ (不带PSRAM)

4. ESP-C3系列
===============

**说明：**

- 特性：单WiFi，不支持BLE
- 更新时间：2021年7月31日
- 固件大小：2MB、4MB
- UART 默认配置：RX20，TX21，波特率：115200
  
**2MB固件下载：** `ESPC3 出厂固件 <https://axk.coding.net/s/7aa7a14e-e8f5-46a7-8b90-0428ab190dc5>`__

**4MB固件下载：** `ESPC3 出厂固件 <https://axk.coding.net/s/95b5f9af-d167-4de1-83d7-3fb45402dd7e>`__
