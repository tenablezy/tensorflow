import tensorflow as tf

# 宣告常數 A = 50
A = tf.constant(50)

# 宣告常數 B = 100
B = tf.constant(100)

# 相加
C = A + B

# 啟動計算圖
with tf.Session() as sess:
	print(sess.run(C))
