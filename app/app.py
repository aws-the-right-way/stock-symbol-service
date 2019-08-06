import os
import uuid

import boto3
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
table = dynamodb.Table('stocks')


@app.route('/api/stocks', methods=['GET'])
def stock_symbol():
    response = table.scan(
        ExclusiveStartKey={"stock_id": str(uuid.uuid1())},
        Limit=1
    )
    stock = response['Items'][0]
    return jsonify({'stock': stock})


@app.route('/api/stocks', methods=['POST'])
def create_stock_symbol():
    stock_id = str(uuid.uuid1())
    stock_name = request.json['name']
    stock = {
        'stock_id': stock_id,
        'name': stock_name
    }
    table.put_item(Item=stock)
    return jsonify({'stock': stock}), 201


@app.route('/api/ping', methods=["GET"])
def ping():
    return 'OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
