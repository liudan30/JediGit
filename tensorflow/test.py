import tensorflow as tf

sess = tf.Session()
with sess.as_default():
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    print((tf.shape(W)).eval())
    b = tf.Variable(tf.zeros([10]))
    print((tf.shape(b)).eval())
    y = tf.matmul(x, W) + b
    print((tf.shape(y)).eval())
