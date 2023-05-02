from cls_old.account import Account

class Admin(Account):
    def __init__(self, email, phone, password, first_name, last_name, user_type):
        super().__init__(email, phone, password, first_name, last_name, user_type)