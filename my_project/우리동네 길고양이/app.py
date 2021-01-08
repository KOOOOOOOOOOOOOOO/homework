from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/board_list')
def board_list():
    return render_template('board_list.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/board_create')
def board_create():
    return render_template('board_create.html')

@app.route('/board_read')
def board_read():
    return render_template('board_read.html')

@app.route('/board_insert', methods=['POST'])
def insert_board():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    date = datetime.datetime.today()
    comment_receive = request.form['comment_give']

    post = {
        'title' : title_receive,
        'author' : author_receive,
        'comment' : comment_receive,
        'date' : date
    }

    db.boards.insert_one(post)
    return jsonify({'result': 'success','msg': '글이 성공적으로 작성되었습니다'})

@app.route('/boards',methods=['GET'])
def read_board():
    boards = list(db.boards.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'boards': boards })

@app.route('/read',methods=['GET'])
def read_board_detail():
    boards = list(db.boards.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'boards': boards })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
