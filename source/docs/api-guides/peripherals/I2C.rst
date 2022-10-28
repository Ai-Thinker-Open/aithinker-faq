I2C API指南
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


I2C API
------------

概述
~~~~~~~~~~~~~~~~

I2C (Inter-Intergrated Circuit)是一种串行通讯总线，使用多主从架构，用来连接低速外围装置。 每个器件都有一个唯一的识别地址，并且都可以作为一个发送器或接收器。 如果有两个或多个主机同时初始化，数据传输可以通过冲突检测和仲裁防止数据被破坏。 BL602/BL604包含一个I2C控制器主机，可灵活配置slaveAddr、subAddr以及传输数据，方便与从设备通信，提供2个word深度的fifo，提供中断功能，可搭配DMA使用提高效率，可灵活调整时钟频率。


API参考
~~~~~~~~~~~~~~~~

Header File
:::::::
- components/platform/hosal/include/hosal_i2c.h

Functions
:::::::

.. code-block:: c

   int hosal_i2c_init(hosal_i2c_dev_t *i2c)
Initialises an I2C interface.
   
   ``return``
  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the device for which the i2c port should be initialised


.. code-block:: c

   int hosal_i2c_master_send(hosal_i2c_dev_t *i2c, uint16_t dev_addr, const uint8_t *data, uint16_t size, uint32_t timeout)

I2c master send.

   ``return``

  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device
  - dev_addr: device address
  - data: i2c send data
  - size: i2c send data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever



.. code-block:: c

   int hosal_i2c_master_recv(hosal_i2c_dev_t *i2c, uint16_t dev_addr, uint8_t *data, uint16_t size, uint32_t timeout)

I2c master recv.

   ``return``

  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device
  - dev_addr: device address
  - data: i2c receive data
  - size: i2c receive data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever


.. code-block:: c

  int hosal_i2c_slave_send(hosal_i2c_dev_t *i2c, const uint8_t *data, uint16_t size, uint32_t timeout)

I2c slave send.

   ``return``

  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device
  - data: i2c slave send data
  - size: i2c slave send data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever


.. code-block:: c

 int hosal_i2c_slave_recv(hosal_i2c_dev_t *i2c, uint8_t *data, uint16_t size, uint32_t timeout)

I2c slave receive.

   ``return``
  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: tthe i2c device
  - data: i2c slave receive data
  - size: i2c slave receive data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever

.. code-block:: c

  int hosal_i2c_mem_write(hosal_i2c_dev_t *i2c, uint16_t dev_addr, uint32_t mem_addr, uint16_t mem_addr_size, const uint8_t *data, uint16_t size, uint32_t timeout)

I2c mem write.

   ``return``
  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device
  - dev_addr: device address
  - mem_addr: mem address
  - mem_addr_size: mem address
  - data: i2c master send data
  - size: i2c master send data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever


.. code-block:: c

  int hosal_i2c_mem_read(hosal_i2c_dev_t *i2c, uint16_t dev_addr, uint32_t mem_addr, uint16_t mem_addr_size, uint8_t *data, uint16_t size, uint32_t timeout)

I2c master mem read.
   ``return``
  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device
  - dev_addr: device address
  - mem_addr: mem address
  - mem_addr_size: mem address
  - data: i2c master send data
  - size: i2c master send data size
  - timeout: timeout in milisecond, set this value to HAL_WAIT_FOREVER if you want to wait forever



.. code-block:: c

  int hosal_i2c_finalize(hosal_i2c_dev_t *i2c)

Deinitialises an I2C device.
   ``return``
  - 0 on success
  - EIO if an error occurred with any step
  
   ``Parameters``
  - i2c: the i2c device



Structures
:::::::

.. code-block:: c

  structhosal_i2c_config_t

I2C configuration.

   Public Members

   ``uint32_t address_width``
    Addressing mode: 7 bit or 10 bit.
   ``uint32_t freq``
    CLK freq.
   ``uint8_t scl``
    i2c clk pin
   ``uint8_t sda``
    i2c data pin
   ``uint8_t mode``
    master or slave mode


.. code-block:: c

 structhosal_i2c_dev_t

I2C device type.

   Public Members

   ``uint8_t port``
     i2c port
   ``hosal_i2c_config_t config``
     i2c config
   ``void *priv``
     priv data
   

Macros
:::::::

.. code-block:: c

   HOSAL_WAIT_FOREVER

Define the wait forever timeout macro.

 
.. code-block:: c

   HOSAL_I2C_MODE_MASTER
i2c communication is master mode


.. code-block:: c

   HOSAL_I2C_MODE_SLAVE
i2c communication is slave mode


.. code-block:: c

   HOSAL_I2C_MEM_ADDR_SIZE_8BIT
i2c memory address size 8bit


.. code-block:: c

   HOSAL_I2C_MEM_ADDR_SIZE_16BIT
i2c memory address size 16bit


.. code-block:: c

   HOSAL_I2C_MEM_ADDR_SIZE_24BIT
i2c memory address size 24bit


.. code-block:: c

  HOSAL_I2C_MEM_ADDR_SIZE_32BIT
i2c memory address size 32bit


.. code-block:: c

  HOSAL_I2C_ADDRESS_WIDTH_7BIT
7 bit mode


.. code-block:: c

  HOSAL_I2C_ADDRESS_WIDTH_10BIT
10 bit mode