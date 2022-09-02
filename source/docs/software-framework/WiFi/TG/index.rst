安信可 平头哥TG系列模块 FAQ
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

TG-12F模块，只要在天猫精灵注册相关信息就可以直接连接实现天猫精灵控制么
--------------
是的

TG-12F需要自己烧录嘛？有直接连天猫精灵的嘛？
--------------
不需要您自己烧录，出厂的AT固件就能连接天猫精灵

TG-12F 里面的默认固件控制有相关文档说明么？
--------------
https://aithinker.blog.csdn.net/article/details/109451425

TG-12F可以直接替换12S不？
--------------
可以替换

TG-12F-Kit开发板是不是用IDE开发
--------------
只能用liunx

TG-12F能直连天猫精灵的？
--------------
可以的，https://aithinker.blog.csdn.net/article/details/109451425

TG-12F开发板能接入小米吗？
--------------
目前暂不支持

TG-12F理想距离多远
--------------
300米

TG-12F 模块支持二次开发吗？是不是阿里的license也在里面了
--------------
支持，https://aithinker.blog.csdn.net/article/details/110559410.在里面
TG-12F开发源码
github.com/Ai-Thinker-Open/Ai-Thinker-Open-TG7100C_SDK

TG-12F模块接天猫精灵，可以控制多少引脚呢？
--------------
可以控制13个引脚

tg12f的蓝牙现在能独立使用吗
--------------
不能独立使用

TG-12F开发板可以同时接入天猫精灵和app吗
--------------
可以接入天猫精灵和app

TG-12F能监控用不
--------------
可以的

TG-12F开发板的开发资料
--------------
https://blog.csdn.net/Boantong_/article/details/110559410


TG-12F 开发板固件接入iot平台还需要自己开发吗
--------------
AT固件可以对接，连接TCP服务器；

TG-12F开发板对接阿里云iot平台需要烧录其他的软件吗
--------------
不需要哦，出厂AT固件就支持连接

TG-12F开发板上电在调试时发现有个问题 用AT指令 发送任和数据 返回的都是OK，是怎么回事
--------------
使用时候需要将IO8拉低，拉低后再重新上电才能正常使用


TG-12F模组可以跑micropython程序吗
--------------------------------
不可以，目前没有适配的程序