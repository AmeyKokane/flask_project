import datetime as dt

from marshmallow import Schema, fields

class Transaction:
    def __init__(self, videoname, renterid, transactionid, transactiondate, type):
        self.videoname = videoname
        self.renterid = renterid
        self.transactionid = transactionid
        self.transactiondate = transactiondate
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.videoname!r})>'.format(self=self)
    
class TransactionSchema(Schema):
    videoname = fields.Str()
    renterid = fields.Str()
    transactionid = fields.Str()
    transactiondate = fields.Date()
    type = fields.Str()
