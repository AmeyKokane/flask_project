from marshmallow import post_load

from videoman.model.transaction import Transaction, TransactionSchema
from videoman.model.transaction_type import TransactionType

class Checkout(Transaction):
    def __init__(self, videoname, renterid, transactionid, transactiondate):
        super(Checkout, self).__init__(videoname, renterid, transactionid, transactiondate, TransactionType.CHECKOUT)

    def __repr__(self):
        return '<Checkout(name={self.description!r})>'.format(self=self)
    
class CheckoutSchema(TransactionSchema):
    @post_load
    def make_checkout(self, data, **kwargs):
        return Checkout(**data)