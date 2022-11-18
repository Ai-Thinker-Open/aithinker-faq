其他
======

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

Ai-WB2系列模组支持哪些开发方式
---------------------------
AT开发，window环境和liunx环境开发

Ai-WB2-32S模组与ESP32-S模组有什么区别，软硬件能否兼容
--------------------------------------------
Ai-WB2-32模组与ESP32-S模组封装兼容，但是引脚定义不一样；软件上所使用的芯片也不一样，WB2-32S使用的是BL602芯片，ESP32模组使用的是ESP32D0WD芯片

WB2模组支持WAPI协议吗
--------------
支持，不过需要通过二次开发实现