from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
from ignore import *
ca = certifi.where()
client = MongoClient('mongodb+srv://'+id+':'+pw+'@cluster0.auvlv.mongodb.net/'+db+'?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    # 받은 값을 DB에 저장
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name':name_receive,
        'address':address_receive,
        'size':size_receive
    }
    db.mars.insert_one(doc)

    return jsonify({'msg': '주문완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    # DB에서 주문 정보를 불러와 클라이언트로 전송
    order_list = list(db.mars.find({}, {'_id':False}));
    return jsonify({'orders':order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
