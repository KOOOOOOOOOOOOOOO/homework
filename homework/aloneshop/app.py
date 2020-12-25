from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 클라이언트가 준 name,count,address,phone 가져오기
    # DB에 정보 삽입하기
    # 성공여부 & 성공 메시지 반환해보기...
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.shoplist.insert_one(doc)

    return jsonify({'result': 'success','msg' : '주문이 완료되었습니다.'})

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.shoplist.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)