# -*- coding: utf-8 -*-

import tensorflow as tf

# 宣告變數    
B = tf.Variable(0, dtype=tf.int64)
with tf.Session() as sess:
    # 變數需要初始化
    sess.run( tf.global_variables_initializer() )

    # 使用 assign 更改變數值
    for i in range(5):
        print( sess.run(B.assign(i)) )
    
    '''
    執行結果：
    0
    1
    2
    3
    4
    '''
