import tensorflow as tf
import matplotlib.pyplot as plt
class GradientDescentController:
    def __init__(self):
        pass

    def service_model(self):
        X = [1., 2., 3.]
        Y = [1., 2., 3.]
        m = n_samples = len(X)
        W = tf.placeholder(tf.float32)
        hypothesis = tf.multiply(X, W)
        cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2)) / m
        W_val = []
        cost_val = []
        with  tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(-30, 50):
                W_val.append(i * 0.1)
                cost_val.append(sess.run(cost, {W: i * 0.1}))
        plt.plot(W_val, cost_val, 'ro')
        plt.ylabel('cost')
        plt.xlabel('W')
        plt.savefig('static/img/gradient_descent.svg')
        return "경사하강법(gradient descent)"
