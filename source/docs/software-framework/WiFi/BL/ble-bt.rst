蓝牙
====

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------

WB2系列支持Bluetooth®LE 5.0 吗？
-----------------------------------------------
支持部分BLE 5.0功能，例如Channel Selection #2，Limited High Duty Cycle Non Connectable Adv，
不支持LE Advertising Extension， 2M PHY，Long Range

--------------
WB2系列能否使用蓝牙进行OTA?
-----------------------------------------------
可以。蓝牙OTA协议为博流自研，支持断点续传，单次写flash大小可配置。


WB2系列的Bluetooth®LE 吞吐量是多少？
-----------------------------------------------
两个模组之间进行吞吐量测试，BLE连接间隔设置为25ms，实测平均速率为570kbps
模组与手机（mate30 pro）之间进行吞吐量测试，手机app使用BLE调试助手，BLE连接间隔设置为25ms，实测平均速率为400kbps

WB2系列的发射功率是多少？
-----------------------------------------------
支持0到15dBm

WB2系列支持多少个客户端连接？
-----------------------------------------------
最大可支持10个蓝牙连接，不局限于蓝牙设备类型（master或slave）。

Ai-WB2-12F模块可以连接手机放音乐吗
--------------------------------
不可以，因为使用的蓝牙是BLE蓝牙，无法传输音频数据。

为什么我写的ble组件，无法正常工作？
-------------------------------
经仔细检查，发现初始化遗漏了bl_sys_init

蓝牙4.0的手机能连上WB2系列模组吗
--------------------
可以，手机端安装BLE蓝牙调试APP即可连接

请问一下Ai-WB2-12F模组的蓝牙是只能用来配网的吗？是否可以蓝牙控制？
--------------------------
该模组的蓝牙可与手机APP中的蓝牙实现数据透传；

请问Ai-WB2-12F-Kit配置蓝牙之后重启是否会保存配置项
----------------------
不会，每次重启需重新配置

WB2系列模块支持蓝牙A2DP功能吗
--------------------
该功能为经典蓝牙功能，目前模块使用为BLE蓝牙，不支持蓝牙A2DP

WB2系列模块可以修改蓝牙MAC地址吗
-------------
可以修改，AT指令和二次开发有相关的教程