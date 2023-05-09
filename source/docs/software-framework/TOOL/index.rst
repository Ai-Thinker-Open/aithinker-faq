其它
======

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

MAC OS上如何查询串口号？
------------------------------------------------
通过指令“ls /dev/cu.*”查询。

CH340以及CP2102驱动获取链接：
------------------------------------------------
https://docs.ai-thinker.com/%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B72

你们USB转TTL（cp2102芯片）不支持2M速率么？
-----------------------------------
该工具最大支持1M速率

请问CP2102模块与CH340模块是否兼容？
---------------------
均是串口模块，使用方法一样，只是驱动不同；

有SDIO接口的数据透传模组么？
-------------------------
没有

有支持研发电台的模块吗
---------------------
目前没有支持研发电台的模组

请问：AiThinkerIDE_V1.5.2软件为什么老是安装失败？
-------------------
建议换一个开发环境，该软件已经不再维护了。这是开发环境搭建指导文档：
`参考链接  <https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/windows-setup.html>`__