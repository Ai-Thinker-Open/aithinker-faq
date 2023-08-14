开源硬件-小安派系列
======

.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>


小安派开发板能驱动60pin的屏幕吗
----------------
不能，开发板内部没有这么多引脚接到屏幕上

小安派开发板的屏幕和摄像头能同时使用吗
---------------
不能同时使用，因为这两个外设都占用一些相同的引脚，同时使用会导致外设无法正常工作

小安派-Eyes开发板有语音识别功能吗
----------------
没有，目前该板子没有集成语音识别功能
