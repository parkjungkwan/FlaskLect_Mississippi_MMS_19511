from ai_calc.model import CalcModel
import tensorflow as tf

class CalcController:

    def __init__(self, num1, num2, opcode):
        self._calc = CalcModel()
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    def calc(self):
        num1 = self._num1
        num2 = self._num2
        opcode = self._opcode

        print('컨트롤러에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))

        sess = tf.Session()
        saver = tf.train.import_meta_graph('ai_calc/saved_add/model-1000.meta')
        saver.restore(sess, tf.train.latest_checkpoint('ai_calc/saved_add/'))

