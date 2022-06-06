安信可 海思系列模块 FAQ
======

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------


海思的模组可以用来传输视频么？
--------------
我司模组适用于数据传输速率较少的场合，对于传输速率较高的，建议去找网卡级别的模组。

海思系列模组用linux开发板驱动的话，是否需要安装驱动？
------------------------
我司模组均通过串口发送指令的方式实现无线功能，非网卡级别，没有安装驱动的说法。

