import tensorflow as tf

class GradientDescentModel:
    def __init__(self):
        pass
    def create_model(self):
        X = [1., 2., 3.]
        Y = [1., 2., 3.]
        m = n_samples = len(X)
        W = tf.placeholder(tf.float32)
        hypothesis = tf.multiply(X, W)
        cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2)) / m
        W_val = []
        cost_val = []
        save_file = 'saved_model/model.ckpt'
        _ = tf.Variable(initial_value='fake_variable')
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(-30, 50):
                W_val.append(i * 0.1)
                cost_val.append(sess.run(cost, feed_dict={W: i* 0.1}))
            saver.save(sess, save_file)
        print('Model Saved !!')


