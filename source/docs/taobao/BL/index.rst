Ai-WB2系列
==================


1.1  Ai-WB2系列出厂AT固件(最新版) 版本号 V4.18_P1.4.4
~~~~~~~~~~~~~~~~

**说明：**

- V4.18_P1.4.4
1. 更新 AT_ComboSDK 到 V4.18_P2.19.1
2. socket添加自动删除功能
3. 新增指令AT+WSCANOPT,用于选择AT+WSCAN的输出信息

- V4.18_P1.4.3
 修复esp touch配网连接较慢的问题

- V4.18_P1.4.2
1. 修复BLUFI配网init/deinit导致程序奔溃问题
2. 修改WIFI不允许多次配网init

- V4.18_P1.4.1
1. 修复ssl证书长度计算错误问题
2. 添加蓝牙配网，添加获取ip事件
3. 修复当ble被连接后关闭ble导致程序奔溃
4. 修复ble连接参数无请求
5. 修复ble从机广播数据长度不正确
6. 修复ble主机上电自动连接失效

- V4.18_P1.4.0
1. 修改读写flash接口修改可以读写超过4K的数据
2. 更新 AI_ComboSDK 到 V4.18_P2.18.0
3. SSL 客户端连接支持证书校验功能(服务器证书可以设置，但是不会校验合法性)
4. 修改默认socket线程堆栈大小(之前太小，server端不够用会失败)
5. 添加SSL证书查询和设置指令

- V4.18_P1.3.3
1. 修复ble
2. 修复BLE主机模式连接信号差的设备可能crash的问题

- V4.18_P1.3.2
1. 更新 ai_ota
2. 修复协议头长度不一致导致最后一帧数据解析时间长的问题

- V4.18_P1.3.1
1. 更新 AI_ComboSDK 到 V4.18_P2.17.1
2. 延长socket自动连接延时(等待网络初始化完成)

- V4.18_P1.3.0
1. 更新 AI_ComboSDK 到 V4.18_P2.17.0
2. 添加自动进入透传模式的指令 AT+SOCKETAUTOTT
3. fix ble master first connection will be disconnected

- V4.18_P1.2.0
1. 修复了wifi扫描时信标发送失败的问题
2. 修改ble adv间隔:最大间隔等于最小间隔增加10ms修正ble master不能写长数据
3. Ble master request最大mtu默认值
4. 添加esp touch 和 AirKiss 配网功能

- V4.18_P1.1.1
1. 修复恢复出厂设置后开启蓝牙从机复位问题

**启动信息**

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

1.2  出厂AT固件
~~~~~~~~~~~~~~~~

**说明：**

- Ai-WB2系列出厂AT固件 版本号V4.18_P1.1.0

**固件下载：** `(固件号：1923)  <https://docs.ai-thinker.com/_media/wb2.zip>`__


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

2.ComboAT固件指令集
~~~~~~~~~~~~~~~~~~

**Ai-WB2系列模组Combo-AT_V4.18版本指令集** `（适用固件号1923） <https://docs.ai-thinker.com/_media/combo_at_v1.8.0.pdf>`__
