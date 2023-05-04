from .userType import UserType
from cryptography.fernet import Fernet

class Account():
    def __init__(self, email, phone, password, fullname, user_type):
        self.__id = None
        self.__email = email
        self.__phone = phone
        self.__password = password
        self.__fullname = fullname
        self.__user_type = UserType(user_type).name

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def email(self):
        return self.__email
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def password(self):
        return self.__password
    
    @property
    def fullname(self):
        return self.__fullname
    
    @property
    def user_type(self):
        return self.__user_type

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @fullname.setter
    def fullname(self, new_fullname):
        self.__fullname = new_fullname

    @user_type.setter
    def user_type(self, new_user_type):
        self.__user_type = UserType(new_user_type).name

    def get_encrypt(self, message):
        fernet = Fernet(Fernet.generate_key())
        return fernet.encrypt(message.encode())

    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, fullname: {self.__fullname},user_type : {self.__user_type}"
    