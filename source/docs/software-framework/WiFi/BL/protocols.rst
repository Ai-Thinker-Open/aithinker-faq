协议
====

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>

--------------


请问WB2-12F模组可以实现网页配网功能并实现数据传输么？
----------------------------------------------
没有现成的代码，需要用户自行设计。

请问一秒发送5个包，一个包200bytes，传输200个设备，则为40Kbyte每秒，请问那个模组支持呢？
-----------------
WB2系列模块。