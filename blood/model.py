import tensorflow as tf
import numpy as np

class BloodModel:
    def __init__(self, fname):
        self.fname = fname

    def create_raw_data(self):
        tf.set_random_seed(777)
        raw_data = np.genfromtxt(self.fname, skip_header=36)
        return raw_data

    @staticmethod
    def create_model(raw_data, weight, age):
        x_data = np.array(raw_data[:, 2:4], dtype=np.float32)
        y_data = np.array(raw_data[:, 4], dtype=np.float32)
        y_data = y_data.reshape(25, 1)

        X = tf.placeholder(tf.float32, shape=[None, 2], name='x-input')
        Y = tf.placeholder(tf.float32, shape=[None, 1], name='y-input')
        W = tf.Variable(tf.random_normal([2,1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')

        hypothesis = tf.matmul(X, W) + b

        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        cost_history = []
        for step in range(2000):
            cost_val, hy_val, _ = sess.run([
                cost,
                hypothesis,
                train
            ], feed_dict={X: x_data, Y: y_data})
            if step % 10 == 0:
                print(step, "Cost : ", cost_val)
                cost_history.append(sess.run(cost, feed_dict={X: x_data, Y: y_data}))
        val = sess.run(hypothesis, feed_dict={X: [[weight, age]]})

        print('혈중 지방농도: {}'.format(val))

        result = ''
        if val < 150:
            result = '정상'
        elif 150 <= val < 200:
            result = '경계역 중성지방혈증'
        elif 200<= val < 500:
            result = '고 중성지방혈증'
        elif 500 <= val < 1000:
            result = '초고 중성지방혈증'
        elif 1000 <= val:
            result = '췌장염 발병 가능성 고도화'

        return result







