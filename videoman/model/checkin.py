from marshmallow import post_load

from videoman.model.transaction import Transaction, TransactionSchema
from videoman.model.transaction_type import TransactionType

class Checkin(Transaction):
    def __init__(self, videoname, renterid, transactionid, transactiondate):
        super(Checkin, self).__init__(videoname, renterid, transactionid, transactiondate ,TransactionType.CHECKIN)

    def __repr__(self):
        return '<Checkin(name={self.description!r})>'.format(self=self)
    
class CheckinSchema(TransactionSchema):
    @post_load
    def make_checkin(self, data, **kwargs):
        return Checkin(**data)
    