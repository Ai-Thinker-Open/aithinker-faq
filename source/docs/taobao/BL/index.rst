1.ComboAT固件
==================

1.1 最新版ComboAT固件(固件号2235)
~~~~~~~~~~~~~~~~

**说明：**

  当前版本为V4.18_P2.5.1，以下是针对上个版本固件号1923，版本号 V4.18_P1.4.4(comboV4.18_P2.19.1)更新内容。

 .. list-table::
    :header-rows: 1

    * - 版本号
      - 更新内容
    * - V4.18_P2.5.1
      - 1.适配 AI_HalWifiOff() 接口 
    * - V4.18_P2.5.0
      - 1.更新flash保存方法
        
        2.更新 AI_ComboSDK

    * - V4.18_P2.31.1
      - 1.透传模式禁止 EVENT 打印
    * - V4.18_P2.31.0
      - 1.添加DNS相关指令

        AT+WDOMAIN

        AT+WDNS

    * - V4.18_P2.30.0
      - 1.添加wifi重连
    * - V4.18_P2.29.5
      - 1.取消 AI_SocketSslMalloc() static修饰
    * - V4.18_P2.4.2
      - 1.修复wifi直接断电时没有触发wifi断开事件导致的异常
    * - V4.18_P2.4.1
      - 1.修改低功耗宏定义，使之和文档保持一致

        2.修复低功耗设置普通模式时没有返回OK的问题

        3.修复低功耗GPIO唤醒设置失败问题

    * - V4.18_P2.4.0
      - 1.MQTT添加无证书校验的SSL连接
    * - V4.18_P2.3.2
      - 1.消告警
    * - V4.18_P2.3.1
      - 1.http添加没有Content-Length时通过结束符判断请求结束
    * - V4.18_P2.3.0
      - 1.更新 AI_ComboSDK  
    * - V4.18_P2.27.2
      - 1.MQTT 密码长度改为最大255字节
    * - V4.18_P2.28.0
      - 1.添加SNTP相关指令

        AT+SNTPTIME

        AT+SNTPTIMECFG

        AT+SNTPINTV

        2.适配SNTP接口
  
    * - V4.18_P2.2.3
      - 1.更新 AI_ComboSDK
    * - V4.18_P2.27.1
      - 1.将mqtt收发buf默认值改为2K
    * - V4.18_P2.27.0
      - 1.tcp client 添加断线自动重连功能    
    * - V4.18_P2.26.1
      - 1.修复 UDPServer自动接收数据卡死问题
    * - V4.18_P2.26.0
      - 1.添加wifi关闭API接口 AI_HalWifiOff()
    * - V4.18_P2.25.1
      - 1.修复不连接设置wifi自动连接不生效问题
    * - V4.18_P2.24.2
      - 1.添加 int Ai_IOMapGetICPinByIndex(uint8_t modePin) 接口
        
        2.AT+SLEEP增加没有初始化IOMAP的判断
    * - V4.18_P2.25.0
      - 1.tcp keep alive 参数实现
        
    * - V4.18_P2.24.1
      - 1.修复socket的accept参数错误

        2.增加AI_HalWifiSetMac()接口

    * - V4.18_P2.24.0
      - 1.开机自动重连添加不校验直接保存wifi参数的选项
    * - V4.18_P2.23.2
      - 1.修复wifi上电自动进入透传模式失败问题
    * - V4.18_P2.23.1
      - 1.添加 AI_TakePrintLock(),AI_GivePrintLock(),AI_DataPrintNoLock()接口

        2.修复socket通信时主动打印数据时多线程打印乱序问题     
    * - V4.18_P2.2.2
      - 1.剥离 AI_HalSetWifiConfigName() 接口

        2.适配 AI_HalSetWifiConfigName() 接口

        3.修复wifi连接失败后wifi扫描失败问题
    * - V4.18_P2.2.1
      - 1.修改wifi名称和密码最大支持63字节

    * - V4.18_P2.2.0
      - 1.睡眠模式增加配置唤醒源的参数

        2.适配深睡眠功能
        
    * - V4.18_P2.1.0
      - 1.esp BluFi 蓝牙配网增加自定义名称功能

        2.修复 esp BluFi 蓝牙配网成功后无法查询wifi连接信息问题

    * - V4.18_P2.0.1
      - 1.更新 AI_ComboSDK
    * - V4.18_P2.0.2
      - 1.更新mqtt clinent ID/账号/密码 长度为127  
    * - V4.18_P2.0.0
      - 1.更新 AI_ComboSDK

        2.适配 AI_HalWifiGetRssi() 接口

    * - V4.18_P2.19.3
      - 修复蓝牙透传大文件时咬狗问题
    * - V4.18_P2.19.3
      - 1.修复wifi扫描输出信息的兼容问题

        2.新增指令AT+WRSSI获取连接后的信号强度

        3.AT+WSCAN参数1输入改为全字匹配
    * - V4.18_P2.20.0
      - 1.抽象读取rssi接口

        2.udp server添加发送功能，发送对象为第一次收到数据时的对象

    * - V4.18_P1.4.6
      - 1.修复蓝牙配网后没有自动保存配网信息问题
        
        2.适配 axk_hal_blufi_sava_wifi_info_flash

    * - V4.18_P1.4.5
      - 1.去掉延时减小socket异常时无法断开的情况
        
        2.修改蓝牙默认UUID（与旧版本不兼容）

   
**启动信息:**

::

 ################################################

 arch:BL602,NULL
 company:Ai-Thinker|B&T
 ble_mac:b4e842c7b843
 wifi_mac:b4e842c7b842
 sdk_version:release/release_bl_iot_sdk_1.6.36
 firmware_version:Release-V4.18_P2.5.1-b90d62b
 compile_time:Jul 17 2023 14:33:20

 ready

 ################################################

**固件下载：** `(固件号：2235)  <https://axk.coding.net/s/add8b1ea-92ea-4ac0-b3d1-8a49f2aee1e6>`__



1.2  ComboAT固件(固件号1923)
~~~~~~~~~~~~~~~~

**说明：**
   
   当前版本为V4.18_P1.4.4，以下是针对上一个版本号V4.18_P1.1.0更新内容。

 .. list-table::
    :header-rows: 1


    * - 版本号
      - 更新内容
    * - V4.18_P1.4.4
      - 1.socket添加自动删除功能

        2. 新增指令AT+WSCANOPT,用于选择AT+WSCAN的输出信息

    * - V4.18_P1.4.3
      - 修复esp touch配网连接较慢的问题
        
    * - V4.18_P1.4.2
      - 1.修复BLUFI配网init/deinit导致程序奔溃问题

        2.修改WIFI不允许多次配网init

    * - V4.18_P1.4.1
      - 1.修复ssl证书长度计算错误问题

        2.添加蓝牙配网，添加获取ip事件

        3.修复当ble被连接后关闭ble导致程序奔溃

        4.修复ble连接参数无请求

        5.修复ble从机广播数据长度不正确

        6.修复ble主机上电自动连接失效

    * - V4.18_P1.4.0
      - 1.修改读写flash接口修改可以读写超过4K的数据

        2.更新 AI_ComboSDK 到 V4.18_P2.18.0
    * - V4.18_P1.3.4
      - 1.SSL 客户端连接支持证书校验功能(服务器证书可以设置，但是不会校验合法性)

        2.修改默认socket线程堆栈大小(之前太小，server端不够用会失败)

        3.添加SSL证书查询和设置指令

    * - V4.18_P1.3.3
      - 1.修复ble

        2.修复BLE主机模式连接信号差的设备可能crash的问题

    * - V4.18_P1.3.2
      - 1.更新 ai_ota

        2.修复协议头长度不一致导致最后一帧数据解析时间长的问题

    * - V4.18_P1.3.1
      - 1.更新 AI_ComboSDK 到 V4.18_P2.17.1

        2.延长socket自动连接延时(等待网络初始化完成)

    * - V4.18_P1.3.0
      - 1.更新 AI_ComboSDK 到 V4.18_P2.17.0

        2.添加自动进入透传模式的指令 AT+SOCKETAUTOTT

    * - V4.18_P1.2.0
      - 1.BL602 SDK更新

        2.modify ble adv interval:max interval equal min interval add 10ms fix ble master cant write long data

        3.ble master request max mtu default

        4.添加esp touch 和 AirKiss 配网功能

    * - V4.18_P1.1.1
      - 1.修复恢复出厂设置后开启蓝牙从机复位问题

**启动信息:**

::

  ################################################

  arch:BL602,NULL
  company:Ai-Thinker|B&T
  ble_mac:7cb94c1dd632
  wifi_mac:7cb94c1dd631
  sdk_version:release/release_bl_iot_sdk_1.6.36
  firmware_version:V4.18_P1.4.4-e15d67b
  compile_time:Nov 25 2022 11:22:39

  ready

  ################################################

**固件下载：** `(固件号：1923)  <https://docs.ai-thinker.com/_media/bl602_combo_v4.18_p1.4.4_combov4.18_p2.19.1_-2m.zip>`__

1.3  最初版Combo AT出厂固件
~~~~~~~~~~~~~~~~

**说明：**

- Ai-WB2系列出厂AT固件 版本号V4.18_P1.1.0

**固件下载：** `<https://docs.ai-thinker.com/_media/wb2.zip>`__


**启动信息：**
::

  ################################################

  arch:BL602,NULL
  company:Ai-Thinker|B&T
  ble_mac:b40ecf1ce2d4
  wifi_mac:b40ecf1ce2d3
  sdk_version:release/release_bl_iot_sdk_1.6.36
  firmware_version:V4.18_P1.1.0-1fa41c3
  compile_time:Oct 11 2022 15:43:40

  ready

  ################################################




2.兼容ESP-12F AT固件（不维护）
==================

**说明：**

- 固件版本号：(V4.18_P2.3.3-179784b)
- 启动方式：自定义
- 固件大小：2MB
- 日志串口|波特率：UART1(IO4、-) | 921600
- 命令串口|波特率：UART0(IO7、IO16) | 115200
- 支持升级：否

**启动信息：**
::

  ################################################
  AT version:2.2.0
  SDK version:release_bl_iot_sdk_1.6.40-11-gf4c8dac01
  compile_time:Mar 29 2023 13:53:46
  Bin version:V4.18_P2.3.3-179784b
  ################################################

  ready

**固件下载：** `(点击下载)  <https://docs.ai-thinker.com/_media/bl_esp_v2.3.3-2mb.zip>`__