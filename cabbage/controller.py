import tensorflow as tf
import numpy as np
from flask_restful import reqparse

class CabbageController:
    def __init__(self):
        pass
    def service_model(self):

        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b
        saver = tf.train.Saver()
        model = tf.global_variables_initializer()

        parser = reqparse.RequestParser()
        parser.add_argument('avg_temp', required=True, type=float)
        parser.add_argument('min_temp', required=True, type=float)
        parser.add_argument('max_temp', required=True, type=float)
        parser.add_argument('rain_fall', required=True, type=float)
        args = parser.parse_args()
        avg_temp = float(args['avg_temp'])
        min_temp = float(args['min_temp'])
        max_temp = float(args['max_temp'])
        rain_fall = float(args['rain_fall'])

        with tf.Session() as sess:
            sess.run(model)
            save_path = 'cabbage/saved_model/model.ckpt'
            saver.restore(sess, save_path)
            data = ((avg_temp, min_temp, max_temp, rain_fall),)
            arr = np.array(data, dtype=np.float32)
            x_data = arr[0:4]
            dict = sess.run(hypothesis, feed_dict={X: x_data})
            print(dict[0])
        result = int(dict[0])
        return result








