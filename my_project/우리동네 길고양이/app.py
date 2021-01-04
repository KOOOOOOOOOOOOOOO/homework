from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/board', methods=['POST'])
def insert_board():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    #date = datetime.datetime.today()
    comment_receive = request.form['comment_give']

    post = {
        'title' : title_receive,
        'author' : author_receive,
        'comment' : comment_receive
        #"date" : date
    }

    db.boards.insert_one(post)
    return jsonify({'result': 'success','msg': '글이 성공적으로 작성되었습니다'})

@app.route('/board',methods=['GET'])
def read_board():
    boards = list(db.boards.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'boards': boards })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
