# Flask로 서버를 열어줌
# render_template으로 html파일(tempplates)을 불러와줌
# request로 요청을 관리해줌?
# jsonify로 json 형식의 데이터를 내보냄
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


# /test로 GET방식 요청이 왔을 경우
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

# /test로 POST방식 요청이 왔을 경우
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)