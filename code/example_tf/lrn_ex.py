import tensorflow as tf

a = tf.constant([
    [[1.0, 2.0, 3.0, 5.0],
     [7.0, 11.0, 13.0, 17.0],
     [17.0, 13.0, 11.0, 7.0],
     [5.0, 3.0, 2.0, 1.0]],
    [[5.0, 3.0, 2.0, 1.0],
     [17.0, 13.0, 11.0, 7.0],
     [1.0, 2.0, 3.0, 5.0],
     [7.0, 11.0, 13.0, 17.0]]
])
#reshape a,get the feature map [batch:1 height:2 width:2 channels:8]
a = tf.reshape(a, [1, 2, 2, 8])

normal_a=tf.nn.local_response_normalization(a,2,0,1,1)
with tf.Session() as sess:
    print("feature map:")
    image = sess.run(a)
    print (image)
    print("normalized feature map:")
    normal = sess.run(normal_a)
    print (normal)
