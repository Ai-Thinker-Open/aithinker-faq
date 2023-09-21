RTL87XX系列
==================

1.1 BW16最新版Combo-AT固件(固件号2179)
~~~~~~~~~~~~~~~~

当前版本为V4.18_P5.6.4，以下是针对上个版本固件号1879，版本号v4.9.2 更新内容。

**说明：**

.. list-table::
    :header-rows: 1

    * - 版本号
      - 更新内容
    * - V4.18_P5.6.4
      - 1.添加 AI_HalWifiOn() 接口 

        2.适配 AI_HalWifiOn() 接口，修复wifi关闭后无法重连问题
    * - V4.18_P5.6.3
      - 1.flash 保存兼容配置保存和普通保存
    * - V4.18_P5.6.2
      - 1.更新 AI_ComboSDK V4.18_P2.29.1,优化 flash 存储，减少 flash 擦写次数 
        
        2 .修复 flash 保存报错
    * - V4.18_P5.6.1
      - 1.修改 flash 保存，改为 config 专用保存方式，避免写入时断电导致的异常
    * - V4.18_P5.6.0
      - 1.更新 AI_ComboSDK V4.18_P2.29.0,MQTT 添加无证书校验的 SSL 连接
    * - V4.18_P5.5.1
      - 1.修复malloc失败卡死问题(关闭了malloc失败的回调函数)

        2.修复编译错误
    * - V4.18_P5.5.0
      - 1.更新 AI_ComboSDK
    * - V4.18_P2.28.2
      - 1.消告警
    * - V4.18_P2.28.1
      - 1.http添加没有Content-Length时通过结束符判断请求结束
    * - V4.18_P2.28.0
      - 1.添加SNTP相关指令
        AT+SNTPTIME
        AT+SNTPTIMECFG
        AT+SNTPINTV
    * - V4.18_P5.4.2
      - 1.更新 AI_ComboSDK
    * - V4.18_P2.27.2
      - 1.MQTT 密码长度改为最大255字节
    * - V4.18_P2.27.1
      - 1.将mqtt收发buf默认值改为2K
    * - V4.18_P5.4.1
      - 1.更新原厂SDK补丁 6.2_patch_integrated_221206_bf3b2a72(94571)
    * - V4.18_P5.4.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.27.0，tcp client 添加断线自动重连功能
    * - V4.18_P5.3.2
      - 1.修复wifi重连和蓝牙配网成功后wifi状态显示没有获取IP问题
    * - V4.18_P5.3.1
      - 1.更新 AI_ComboSDK 到 V4.18_P2.26.1，修复 UDPServer自动接收数据卡死问题
    * - V4.18_P5.3.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.26.0，1.添加wifi关闭API接口 AI_HalWifiOff()

        2.适配 AI_HalWifiOff() 接口
    * - V4.18_P5.2.1
      - 1.更新 AI_ComboSDK 到 V4.18_P2.25.1，修复不连接设置wifi自动连接不生效问题
    * - V4.18_P5.2.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.24.2，添加 int Ai_IOMapGetICPinByIndex(uint8_t modePin) 接口
        2.AT+SLEEP增加没有初始化IOMAP的判断，适配深睡眠接口
    * - V4.18_P5.2.0
      - 1. tcp keep alive 参数实现
    * - V4.18_P5.1.1
      - 1.更新 AI_ComboSDK 到 V4.18_P2.24.1， 修复socket的accept参数错误

        2.增加AI_HalWifiSetMac()接口
    * - V4.18_P5.1.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.24.0，开机自动重连添加不校验直接保存wifi参数的选项
    * - V4.18_P5.0.3
      - 1.更新 AI_ComboSDK 到 V4.18_P2.23.2，修复wifi上电自动进入透传模式失败问题
    * - V4.18_P5.0.2
      - 1.更新 AI_ComboSDK 到 V4.18_P2.23.1，添加 AI_TakePrintLock(),AI_GivePrintLock(),AI_DataPrintNoLock()接口

        2.修复socket通信时主动打印数据时多线程打印乱序问题
    * - V4.18_P5.0.1
      - 1.更新 AI_ComboSDK
    * - V4.18_P2.23.0
      - 1.剥离 AI_HalSetWifiConfigName() 接口
    * - V4.18_P2.22.1
      - 1.修改wifi名称和密码最大支持63字节
    * - V4.18_P2.22.0
      - 1.睡眠模式增加配置唤醒源的参数
    * - V4.18_P2.21.0
      - 1.esp BluFi 蓝牙配网增加自定义名称功能
    * - V4.18_P2.20.2
      - 1.更新mqtt clinent ID/账号/密码 长度为127
    * - V4.18_P2.20.1
      - 1.修复蓝牙配网后没有自动保存配网信息问题
       
        2.适配 AI_HalSetPowerMode()接口
    * - V4.18_P5.0.0
      - 1.更新 AI_ComboSDK V4.18_P2.20.0，抽象读取rssi接口
        
        2.udp server添加发送功能，发送对象为第一次收到数据时的对象
    * - V4.18_P4.14.3
      - 1.更新 AI_ComboSDK 到V4.18_P2.19.3，修复蓝牙透传大文件时咬狗问题

        2.修复wifi扫描输出信息的兼容问题.

        3.新增指令AT+WRSSI获取连接后的信号强度.

        4.AT+WSCAN参数1输入改为全字匹配
    * - V4.18_P4.14.2
      - 1.更新 AI_ComboSDK 到V4.18_P2.19.2，去掉延时减小socket异常时无法断开的情况

        2.修改蓝牙默认UUID
    * - V4.18_P4.14.1
      - 1.更新 AI_ComboSDK 到V4.18_P2.19.1，socket添加自动删除功能
    * - V4.18_P4.14.0
      - 1.更新 AI_ComboSDK 到V4.18_P2.19.0，1.添加蓝牙配网
     
        2.修复ping卡死

        3.新增指令AT+WSCANOPT,用于选择AT+WSCAN的输出信息，适配AI_HalSystemIsrunning函数
    * - V4.18_P4.13.2
      - 1.更新 AI_ComboSDK 到V4.18_P2.15.2，设置默认IOMap容量为48个

        2.修复ble从机notify导致重启问题
    * - V4.18_P4.13.1
      - 1.更新 AI_ComboSDK 到 V4.18_P2.15.1，修复 AI_ParseParam 指令第一个参数为空是没有解析到的问题
    * - V4.18_P4.13.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.15.0，AT+MQTT添加重连功能

        2.添加取消订阅指令 AT+MQTTUNSUB

        3.添加STA MAC查询指令 AT+CIPSTAMAC_DEF
    * - V4.18_P4.12.0
      - 1.AI_ComboSDK更新到V4.18_P2.14.0，修改socket和蓝牙透传分包逻辑,使分包更完整

        2.修改透传模式退出逻辑，减少误退出，蓝牙发送适配长数据发送
    * - V4.18_P4.11.3
      - 1.更新AI_ComboSDK到 V4.18_P2.13.6，添加新指令 AT+HTTPCLIENTLINE （原指令 AT+HTTTPCLIENTLINE 为了兼容性代码保存，但是手册不再体现）

        2.优化蓝牙MAC获取，优先从flash加载，从hal加载失败则打开蓝牙重新获取一次

        3.取消开启蓝牙前设置MAC(会导致iphone 无法扫描到 BW16)

        4.修复socket读取大数据时咬狗问题
    * - v4.11.2
      - 1.更新AI_ComboSDK到]v2.13.2，修复HTTP请求带参数时数据发送长度错误问题

        2.修复任务创建堆栈深度设置错误问题
    * - v4.11.1
      - 1.更新AI_ComboSDK到v2.13.1，添加手机配网完成后保存配网信息的回调函数 ai_Callbacks.wifiCfgCallback()

        2.将socket默认分包大小改为1024byte，适配 ai_Callbacks.wifiCfgCallback()
    * - v4.11.0
      - 1.AI_ComboSDK 更新到  v2.13.0，1.修改 AI_HalGetApClientList() API接口

        2.修复获取AP客户端列表空间作用域错误问题
    
        3.修复MQTT订阅超时资源释放错误
        
        4.AI_DataPrint 打印函数添加信号量互斥，避免打印乱序
        
        5.AT+SOCKET 添加指定 conid选项，修复 AI_HalxTaskCreate 获取句柄错误问题导致的内存泄露
    * - v4.10.1
      - 1.AI_ComboSDK 到 v2.12.2，修复蓝牙自动进入透传错误
    * - v4.10.0
      - 1.开启蓝牙配网指令

        2.更新 submodule/RealtekAmebadSDK 合入补丁，6.2_patch_integrated_220507_7a3045e0(72412)，6.2_patch_integrated_220728_48de91fa(81022)

        3.合入 patch/fix-OTA-power.patch 补丁,修复出厂固件OTA测试功率不足问题

        4.更新 AI_ComboSDK 到 v2.12.0
        
        4.1.修复GPIO读取时需要打印错误(系统内部引脚从0开始，AT指令的序号从1开始)
       
        4.2.重命名自己引入的内核链表，函数和宏定义添加AI头，避免和SDK冲突
        
        4.3.编译消告警
        
        4.4.添加 AI_CONFIG_HAVE_OTA 宏定义
        
        4.5.修复之前部分书写错误
        
        4.6.MQTT添加AI_MQTT_RETURN_SUCCESS枚举
        
        4.7.修改任务创建和删除任务API参数
        
        4.8.修复弱定义 AI_HalxSemaphoreTakeAuto 中调用和返回值错误
        
        4.9.添加API接口返回值描述


**启动信息**

::

   #calibration_ok:[2:19:11] 

   at version:release/V4.18_P2.29.2 sdk version:amebad_v6.2C firmware version:release/V4.18_P5.6.4(May 30 2023-10:28:28)



**固件下载：** `固件号2179  <https://docs.ai-thinker.com/_media/2179_bw16_combo_soft_v4.18_p5.6.4_combov4.18_p2.29.2_.zip>`__


1.2 BW16 Combo-AT固件(固件号1879)
~~~~~~~~~~~~~~~~

**启动信息**

::

   #calibration_ok:[2:19:11] 

   at version:release/v2.11.2 sdk version:amebad_v6.2C firmware version:release/v4.9.2(Jul  8 2022-16:18:01)



**固件下载：** `固件号1879  <https://docs.ai-thinker.com/_media/1879_bw16_combo_soft_v4.9.2_combov2.11.2_.rar>`__

