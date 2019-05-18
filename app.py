from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
from blood.model import BloodModel
from gradient_descent.controller import  GradientDescentController
from iris.controller import IrisController
from cabbage.controller import CabbageController
from kospi.controller import KospiController
from stock_ticker.controller import StockTickerController
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():

    userid = request.form['userid']
    password = request.form['password']
    print('로그인 들어온 아이디 {}, 비번 {}'.format(userid, password))
    c = MemberController()
    view = c.login(userid, password)
    return render_template(view)

@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))



@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else :
        print('넘어온 식 {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자 {}'.format(op))
        nums = stmt.split(op)
        result = 0
        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '-':
            result = int(nums[0]) + int(nums[1])
        elif op == '*':
            result = int(nums[0]) + int(nums[1])
        elif op == '/':
            result = int(nums[0]) + int(nums[1])

    return jsonify(result= result)



# /ai_calc
# print('계산기에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))
@app.route('/ai_calc', methods=['POST'])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    print('계산기에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))
    c = CalcController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = result
    return render_template('ai_calc.html', **render_params)


@app.route('/blood', methods=['POST'])
def blood():
    weight = request.form['weight']
    age = request.form['age']
    print('몸무게 : {}, 나이 : {}'.format(weight,  age))
    model = BloodModel('blood/data/data.txt')
    raw_data = model.create_raw_data()
    render_params = {}
    value = model.create_model(raw_data,weight,age)
    render_params['result'] = value
    return render_template('blood.html', **render_params)

@app.route('/gradient_descent', methods=['GET','POST'])
def gradient_descent():
    ctrl = GradientDescentController()
    name = ctrl.service_model()
    return render_template('gradient_descent.html',name = name)

@app.route('/iris', methods=['GET','POST'])
def iris():
    ctrl = IrisController()
    result = ctrl.service_model()
    return render_template('iris.html', result=result)

@app.route('/cabbage', methods=['GET','POST'])
def cabbage():
    ctrl = CabbageController()
    result = ctrl.service_model()
    render_params = {}
    render_params['result'] = result
    return render_template('cabbage.html', **render_params)

@app.route('/kospi',methods=['GET','POST'])
def kospi():
    ctrl = KospiController()
    kospi = ctrl.service()
    render_params = {}
    render_params['result'] = kospi
    return render_template('kospi.html', **render_params)

@app.route('/stock_ticker',methods=['GET','POST'])
def stock_ticker():
    ctrl = StockTickerController()
    price = ctrl.service()
    render_params = {}
    render_params['result'] = price
    return render_template('stock_ticker.html', **render_params)

if __name__ == '__main__':
    app.run()
