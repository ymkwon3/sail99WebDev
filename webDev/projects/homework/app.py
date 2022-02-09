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
    # /, 즉 기본경로에서 index.html을 렌더링 해줌
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_recv = request.form['name_give']
    comment_recv = request.form['comment_give']

    doc = {
        'name' : name_recv,
        'comment' : comment_recv
    }

    # homework 테이블에 위에서 지정한 객체를 저장
    db.homework.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    # 데이터베이스 homework 테이블에서 아이디를 제외한 데이터들을 불러와 리스트로 저장
    post_list = list(db.homework.find({}, {'_id': False}))
    return jsonify({'posts':post_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)