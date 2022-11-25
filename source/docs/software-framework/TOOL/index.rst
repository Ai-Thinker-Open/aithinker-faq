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
