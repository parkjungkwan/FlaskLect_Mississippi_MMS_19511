from ai_calc.model import CalcModel
import tensorflow as tf

class CalcController:

    def __init__(self, num1, num2, opcode):
        self._calc = CalcModel()
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    @property
    def calc(self):
        num1 = self._num1
        num2 = self._num2
        opcode = self._opcode

        print('컨트롤러에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))

        sess = tf.Session()
        saver = tf.train.import_meta_graph('ai_calc/saved_'+opcode+'/model-1000.meta')
        saver.restore(sess, tf.train.latest_checkpoint('ai_calc/saved_'+opcode+'/'))

        graph = tf.get_default_graph()
        w1 = graph.get_tensor_by_name('w1:0')
        w2 = graph.get_tensor_by_name('w2:0')
        print('num1 >>> {}'.format(float(num1)))
        print('num2 >>> {}'.format( float(num2)))
        feed_dict = {w1: float(num1), w2: float(num2)}

        op_to_restore = graph.get_tensor_by_name("op_"+opcode+":0")
        result = sess.run(op_to_restore, feed_dict)
        print('최종결과 : {}'.format(result))
        return result







