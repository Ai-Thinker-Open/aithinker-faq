雷达模组系列
======

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>


Rd-01模组的上位机以及搭建环境在哪儿获取？
--------------------
资料获取链接：
`参考链接  <https://docs.ai-thinker.com/radar>`__
开发环境以及上位机使用见博文：
`参考链接  <https://blog.csdn.net/Boantong_/article/details/130235376>`__

Rd-01模组二次开发资料中，哪些是蓝牙那边的资料？
----------------------
SDK中的Ai-Thinker-WB2子模块中application下Bluetooth即为蓝牙相关用例。

Rd-01模组能接入天猫精灵平台么？
----------------
不能。

请问：Rd-01模组可以用arduino做开发吗？
--------------
不支持。

Rd-01雷达模组可以监测出空间中人的数量吗，最多可以监测到几个人
----------------------
可以监测人的数量，需做二次开发实现，最多能监测到多少个人得看代码处理逻辑

Rd-01模块探测角度可调吗
-------------------------
模块不可以调整探测角度
