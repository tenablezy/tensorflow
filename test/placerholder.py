# -*- coding: utf-8 -*-

import tensorflow as tf

# 宣告占位符
C = tf.placeholder(dtype=tf.int64)

with tf.Session() as sess:
    for i in range(5):
        result = sess.run(C, feed_dict={C:i})
        print(result)
