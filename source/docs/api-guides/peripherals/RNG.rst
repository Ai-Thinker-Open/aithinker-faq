RNG API指南
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


RNG API
------------

概述
~~~~~~~~~~~~~~~~

随机数生成器(Random number generation),可以生成指定长度的随机数。

API参考
~~~~~~~~~~~~~~~~

Header File
:::::::
- components/platform/hosal/include/hosal_rng.h

Functions
:::::::

.. code-block:: c

   int hosal_rng_init(void)
init rng
   
   ``return``
  - 0 : success
  - other: fail


.. code-block:: c

   int hosal_random_num_read(void *buf, uint32_t bytes)

Fill in a memory buffer with random data.

    ``return``
  - 0 : success
  - other: fail
    
    ``Parameters``
  - buf: Point to a valid memory buffer, this function will fill in this memory with random numbers after executed
  - bytes: Length of the memory buffer (bytes)



