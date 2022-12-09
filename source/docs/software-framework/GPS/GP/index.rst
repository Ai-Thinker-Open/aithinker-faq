安信可 GPS系列模块 FAQ
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

GP-02出货配的天线是无源天线还是有源天线
--------------
无源天线

GP-02开发板上的圆形器件是什么？实际电路设计能否不接？型号是什么？
--------------
圆形器件是法拉电容，不是纽扣电池，型号为XH414H。实际电路设计可以不接

GP-01和GP-02有什么区别
----------------------
只是封装不同，其他软件功能都一样

GPS模组上的VCC_RF引脚是做什么用途使用
-------------
给有源天线引脚进行供电

GP-02和BG-02有什么区别
--------------------
芯片厂商不同

GP-01的串口有两个吗
------------------
没有两个，只有一个串口