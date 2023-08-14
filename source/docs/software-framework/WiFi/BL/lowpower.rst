低功耗
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

进入低功耗模式后电流异常是什么原因？
----------------------------
当正常进入PDS时电流一般100uA~200uA，正常进入HBN时电流一般<5uA，
如果电流在几百uA则说明有power domain未关，如果电流超过10mA则一般是程序跑飞所导致的。


电流未能如期降低，为什么直接升高到mA级别？
----------------------------
当发现电流未能降低至uA级别就直接上升到10mA以上时，一般是程序跑飞导致，
出现此问题优先考虑是否在PDS_Mode_Enter中关闭flash之后又访问了flash的地址0x23xxxxxx，可以通过反汇编对此进行确认，PDS_Mode_Enter内关flash与开flash之间绝不应该出现0x23xxxxxx地址。如果是此问题导致，则优先确认链接脚本中是否没把ATTR_CLOCK_SECTION、ATTR_CLOCK_CONST_SECTION、ATTR_TCM_SECTION、ATTR_TCM_CONST_SECTION、ATTR_DTCM_SECTION等放到TCM区域，其次确认此过程中是否有变量在flash上。
还有可能是代码中所使用到的某些API没使用这些链接属性修饰。

能正常进入低功耗，但无法正常唤醒，如何解决？
----------------------------
需要确认所需中断是否正常配置（低功耗中断需要配置，相应外设中断也需要配置），查找问题时可以考虑使用PDS/HBN自身的timer唤醒来做对比验证，
确认是没正确配置唤醒源还是确实PDS/HBN模式配置错误，然后继续查找原因。

为什么在IOT_SDK运行异常，在MCU_SDK运行正常？
----------------------------
MCU_SDK平台相对简单，一般不会出现进出PDS/HBN异常的情况。IOT_SDK平台较为复杂，
不过一般是因为其所使用的stddriver没有更新到最新版本所导致，因此IOT_SDK跑低功耗的case时需要优先更新stddriver到最新。


低功耗模式下电流比预期大了几十uA，如何解决？
----------------------------
flash pad floating会导致漏电（50uA~100+uA）。faraday memory进行读写后无法正常进入retension模式会导致电流偏大（20uA左右）。
进入低功耗后某些GPIO没有HighZ会导致电流增大。为了从低功耗模式唤醒所打开的外设会导致电流偏大（如HBN模式使用acomp唤醒）。


注意事项
----------------------------
1.进入PDS前若关闭了flash，则需要保证关flash后的代码都不在flash上，否则跑飞。

2.若需要使用JLINK调试，则JLINK所用的GPIO不能被HighZ。

3.602使用的是faraday的memory，其特性为程序在将TCM/OCRAM设置为retension模式后如果又对TCM/OCRAM区域进行了写操作，则会导致这些区域自行退出retension模式，继而使得电流稍大（20uA级别）。

4.sram有idle、retension、sleep三种模式，正常读写sram时其处于idle模式，idle模式电流较大，retension模式下不能对sram进行读写但此时进入低功耗后数据可以保留，retension模式电流较小，sleep模式下sram掉电所有数据全部丢失，sleep模式电流最小。

5.PDS模式需要37个clock（32K）的时间来warm up，因此存在最小睡眠时间的限制37，软件结构体中的睡眠时间必须超过此数值。

6.当使用PDS的qon pad唤醒时，需要注意，由于ro_pds_irq_in中断会同时受到多个irq的影响而置一，因此在清此标志位之前，需要确保其所包含的多个irq都已经被clear掉，否则即使设置了cr_pds_int_clr，也会由于“hbn_irq_out | (gpio_irq) | irrx_int | ble_slp_irq | reg_en_platform_wakeup & platform_wake_up”而使得ro_pds_irq_in再次被置一（尤其是HBN内GPIO7/8的IRQ标志位），因此需要在设置aon pad唤醒PDS时，先清一下这些标志位。

7.只要唤醒源在(hbn_wakeup)，就没办法hbn sleep。所以当唤醒源标志位未清时，0x4000F000[7]置一并不会进入hbn，程序会继续向下运行。

8.为了避免因flash pad floating而导致的漏电，需要正确设置相应pad的pull，建议全部上拉。

9.在进入PDS/HBN之前需要确保相应低功耗模式下有效的唤醒源中断全都被清除过，否则有可能无法正常进入PDS/HBN。

10.在测试PDS/HBN时遇到异常现象时，建议优先接上电流表，可以方便排查问题。


请问WB2-12F模组进入深睡模式之后，能否收到WiFi消息？
---------------------
WB2系列模组进入深睡之后均无法收到WiFi消息；