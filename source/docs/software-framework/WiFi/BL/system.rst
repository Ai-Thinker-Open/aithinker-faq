系统
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

CPU架构，运行频率以及RAM
--------------
BL602是基于RISC-V处理器芯片，最高运行频率是160MHz,特殊情况下允许超频到192M，芯片可用RAM。

模组从上电到运行程序最快需要多长时间？
--------------
约3ms。

模组掉电的时候，数据存储在哪里？
--------------
完全掉电时，芯片内ram上的数据均会丢失。PDS、HBN模式不同level下ram区域掉电情况各不相同，需要case by case。