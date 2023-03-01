Wi-Fi
=======

:link_to_translation:`en:[English]`

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>



**安信可Ai-WB2系列SDK和API参考链接：** `参考链接 <https://wb2-api-web.readthedocs.io/en/latest/docs/api-guides/index.html>`__ 

目前WB2系列模组支持esptouch v2版本吗
---------------------------------
不支持

WB2系列模组支持MQTT开发吗
--------------
支持

请问WB2系列模组支持接入中文名称的WIFI么？
-------------------
支持UTF-8格式的中文

请问WB2系列模组内置TCP是么？
-------------
固件中包含TCP协议栈；

请问ESP-01S模组以及WB2系列模组支持接入onenet平台么？
--------------------
两款模组均支持；

请问WB2系列模组有RJ45接口么？
-------------------
WB2系列模组没有以太网（RJ45）接口；

上电之后我直接连接wifi，设置的默认密码，但为何都连接失败了
-----------------------
热点需要手动配置开启

请问combo固件中 “ AT+MQTTPUBRAW ” 指令一次性最多可以发送多长的数据？
---------------------
最多支持发送的数据长度为1014Bytes。

请问博流1823号固件中 “ AT+MQTTPUBRAW ” 指令一次性最多可以发送多长的数据？
--------------------
可发送的数据长度没有限制，由模组剩余内存大小决定，可通过指令“AT+SYSRAM”实时查询模组剩余内存大小

请问，combo固件订阅或者发布的主题长度有限制么，最长多少个字节？
------------------------
主题最长支持1008个字节；

请问Ai-WB2系列模组烧录用的是哪种接口，JTAG还是UART？
----------------------------
用的是串口烧录的方式；

请问用于wifi系列模组做TCP透传测试的网页有么？
-----------------------------
用这个链接：http://tt.ai-thinker.com:8000/ttcloud

请问WB2的wifi跟蓝牙功能的使用是否用的同一个串口？
--------------------------
是的

WB2-32S写的最大连接数5个是什么意思
---------------
模块当热点使用的时候，可以接入5个设备

请问有支ipv6的模组么？
------------------------
目前没有出厂固件支持ipv6的模组，WB2系列模组支持ipv6，但是需要用户二次开发实现；