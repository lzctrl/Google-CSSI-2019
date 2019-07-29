import time

class Transaction(object):

    def __init__(self, time, type, amount, dest_account = ""):
        self.time = time
        self.type = type
        self.amount = amount
        self.dest_account = dest_account

    def __str__(self):
        if self.type == "withdraw" or self.type == "deposit":
            return "%s: %s %s" % (self.time, self.type, self.amount)
        elif self.type == "transfer":
            return "%s: %s $%s to account '%s'" % (self.time, self.type, self.amount, self.dest_account)
