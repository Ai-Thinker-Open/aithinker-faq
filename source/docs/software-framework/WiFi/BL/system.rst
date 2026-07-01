系统
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

CPU架构，运行频率以及RAM
--------------
BL602是基于RISC-V处理器芯片，最高运行频率是160MHz,特殊情况下允许超频到192M，芯片可用RAM。

模组从上电到运行程序最快需要多长时间？
--------------
约3ms。

模组掉电的时候，数据存储在哪里？
--------------
完全掉电时，芯片内ram上的数据均会丢失。PDS、HBN模式不同level下ram区域掉电情况各不相同，需要case by case。

为什么模块默认支持Cli串口通讯，在哪设置不开启这个选型？
--------------------------------
我们移植了命令行交互工具cli（command-line interface），已经将其移植到我们到系统中，在对应的工程目录的 proj_config.mk 文件把 CONFIG_SYS_AOS_CLI_ENABLE:=0，如果没有，则添加这个设置。

为什么我写的组件或代码，无法开启LOG打印日志？
-------------------------------------
日志管理组件blog开关需在相应的 proj_config.mk 文件目录下，LOG_ENABLED_COMPONENTS配置上增加对应组件的名字 例如这里需要增加blog_testa blog_testb blog_testc 的日志输出：LOG_ENABLED_COMPONENTS:=blog_testa blog_testb blog_testc 
其他组件默认关闭，组件名字就是其文件夹名字。



