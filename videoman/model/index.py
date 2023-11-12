from flask import Flask, jsonify, request
from datetime import datetime
from videoman.model.checkin import Checkin, CheckinSchema
from videoman.model.checkout import Checkout, CheckoutSchema
from videoman.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Checkout('Home Alone - I', '00001', '000010',datetime(2023, 10, 20)),
    Checkout('My Neighbor Totoro', '00002', '000020',datetime(2023, 10, 21)),
    Checkin('Home Alone - I','00001', '000010',datetime(2023, 10, 23)),
    Checkout('Inception', '00003', '000050',datetime(2023, 10, 21)),
    Checkin('Inception','00003', '000050',datetime(2023, 10, 23))
]

@app.route('/checkins')
def get_checkins():
    schema = CheckinSchema(many=True)
    checkins = schema.dump(
        filter(lambda t: t.type == TransactionType.CHECKIN, transactions)
    )
    return jsonify(checkins)


@app.route('/checkins', methods=['POST'])
def add_checkin():
    checkin = CheckinSchema().load(request.get_json())
    transactions.append(checkin)
    return "", 204


@app.route('/checkouts')
def get_checkouts():
    schema = CheckoutSchema(many=True)
    checkouts = schema.dump(
        filter(lambda t: t.type == TransactionType.CHECKOUT, transactions)
    )
    return jsonify(checkouts)


@app.route('/checkouts', methods=['POST'])
def add_checkout():
    checkout = CheckoutSchema().load(request.get_json())
    transactions.append(checkout)
    return "", 204


if __name__ == "__main__":
    app.run()