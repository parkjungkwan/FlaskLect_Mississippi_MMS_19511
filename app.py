from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    result = c.calc
    render_params = {}
    render_params['result'] = result
    return render_template('ai_calc.html', **render_params)


@app.route('/blood', methods=['POST'])
def blood():
    weight = request.form['weight']
    age = request.form['age']
    print('몸무게 : {}, 나이 : {}'.format(weight,  age))


if __name__ == '__main__':
    app.run()
