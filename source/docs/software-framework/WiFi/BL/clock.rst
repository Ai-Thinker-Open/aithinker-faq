时钟
======

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

如果想给某个外设配置一个时钟，需要调用哪些函数？
------------------------------------------------------------------------

GLB_Set_System_CLK() --> 设置整个系统的时钟，
部分外设时钟也来源于此 GLB_Set_......_CLK() --> 设置目标外设时钟 GLB_AHB_Slave1_Clock_Gate() --> 部分外设时钟默认被gate，
使用该外设时需要主动ungate 其它外设 --> 目标外设内相关时钟配置

PDS、HBN的工作机制是什么？如何实现唤醒？
------------------------------------------------------------------------

将芯片划分为多个电源域，通过不同电源域掉电与否的组合来实现不同级别的低功耗模式，详情参见低RM功耗章节。 不同级别的低功耗模式唤醒源均不相同。


芯片的功耗是多少？
------------------------------------------------------------------------

低负荷运行时电流在10mA左右，高负荷运行时电流40mA以上，低功耗模式最低可达2uA左右。
