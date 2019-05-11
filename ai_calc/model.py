import tensorflow as tf
class CalcModel:
    def __init__(self):
        self._w1 = tf.placeholder(tf.float32, name='w1')
        self._w2 = tf.placeholder(tf.float32, name='w2')
        self._feed_dict = {'w1': 8.0, 'w2':2.0}

    def create_add_model(self):
        w1 = self._w1
        w2 = self._w2
        feed_dict = self._feed_dict

        r = tf.add(w1, w2, name='op_add')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1 : feed_dict['w1'], w2 : feed_dict['w2']})
        print('TF 덧셈결과 {}'.format(result))
        saver.save(sess, './saved_add/model', global_step=1000)

    def create_sub_model(self):
        w1 = self._w1
        w2 = self._w2
        feed_dict = self._feed_dict

        r = tf.subtract(w1, w2, name='op_sub')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 뺄셈결과 {}'.format(result))
        saver.save(sess, './saved_sub/model', global_step=1000)

    def create_mul_model(self):
        w1 = self._w1
        w2 = self._w2
        feed_dict = self._feed_dict

        r = tf.multiply(w1, w2, name='op_mul')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 곱셈결과 {}'.format(result))
        saver.save(sess, './saved_mul/model', global_step=1000)

    def create_div_model(self):
        w1 = self._w1
        w2 = self._w2
        feed_dict = self._feed_dict

        r = tf.math.floordiv(w1, w2, name='op_div')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 나눗셈셈결과 {}'.format(result))
        saver.save(sess, './saved_div/model', global_step=1000)
