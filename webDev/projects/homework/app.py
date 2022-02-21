import json

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi
import requests, xmltodict
from ignore import *

ca = certifi.where()
client = MongoClient('mongodb+srv://'+id+':'+pw+'@cluster0.auvlv.mongodb.net/'+db+'?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    # /, 즉 기본경로에서 index.html을 렌더링 해줌
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

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

@app.route("/homework/delete", methods=["POST"])
def homework_post_delete():
    id_recv = request.form['id_give']

    # homework 테이블에 위에서 지정한 객체를 저장
    db.homework.delete_one({'_id':ObjectId(id_recv)})
    return jsonify({'msg':'삭제 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    # 데이터베이스 homework 테이블에서 아이디를 제외한 데이터들을 불러와 리스트로 저장
    post_list = list(db.homework.find())
    for post in post_list:
        post['_id'] = str(post['_id'])
    return jsonify({'posts':post_list})


# 산정보 api입니다.
@app.route("/mountainInfo", methods=["GET"])
def get_mountainInfo():
    url = 'http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI'
    params = {'serviceKey': 'C1EvS3mDIvVFBeCI85YBjCPyaBYo54kb2xyrzOTz/WpWmx1kEc/7m6L5U9pWb7rJ2vb6VhWL5oQFWytEkHen4Q==', 'searchWrd': '북한산'}

    response = requests.get(url, params=params)
    obj = xmltodict.parse(response.text)
    print(obj)
    return obj['response']

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)