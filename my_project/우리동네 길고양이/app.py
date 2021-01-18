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
    date = datetime.datetime.utcnow()
    comment_receive = request.form['comment_give']
    board = db.boards.find_one(sort=[("uid", -1)])
    index = 1
    if board is not None:
        index = board['idx'] + 1


    post = {

        'title' : title_receive,
        'author' : author_receive,
        'comment' : comment_receive,
        'date' : date,
        'idx' : index
    }

    db.boards.insert_one(post)



    return jsonify({'result': 'success','msg': '글이 성공적으로 작성되었습니다'})

@app.route('/catInfo',methods=['POST'])
def cat_Info():
    name_receive = request.form['name_give']
    info_receive = request.form['info_give']
    la_receive = request.form['la_give']
    ma_receive = request.form['ma_give']

    cat_infomation = {
        'name' : name_receive,
        'info' : info_receive,
        'la' : la_receive,
        'ma' : ma_receive
    }

    db.catsinfo.insert_one(cat_infomation)

    return jsonify({'result': 'success', 'msg': '등록되었습니다'})

@app.route('/delete',methods=['POST'])
def delete_board():
    idx_receive = request.form['idx_give']
    db.boards.delete_one({'idx': int(idx_receive)})
    return jsonify({'result' : 'success','msg' : '글이 삭제됨' })

@app.route('/boards',methods=['GET'])
def read_board():
    boards = list(db.boards.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'boards': boards })

@app.route('/read',methods=['GET'])
def read_board_detail():
    idx = request.args.get('idx')
    board = db.boards.find_one({'idx': int(idx)}, {'_id': 0})
    return jsonify({'result': 'success', 'board': board })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
