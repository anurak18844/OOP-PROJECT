from cls_old.userType import UserType
from cryptograph import Cryptograph
from cryptography.fernet import Fernet
fernet = Fernet(Fernet.generate_key())
class Account():
    def __init__(self, email, phone, password, full_name, user_type):
        self.__id = None
        self.__email = email
        self.__phone = phone
        self.__password = password
        self.__full_name= full_name
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
    def full_name(self):
        return self.__full_name
    
    @property
    def user_type(self):
        return self.__user_type

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = new_full_name

    @user_type.setter
    def user_type(self, new_user_type):
        self.__user_type = UserType(new_user_type).name

    def get_encrypt(self, message):
        return fernet.encrypt(message.encode())

    def get_decrypt(self, message):
        return fernet.decrypt(message).decode()

    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, first_name : {self.__first_name}, last_name : {self.__last_name}, user_type : {self.__user_type}"
    
    def create_account(self):
        docs =   {
        "email" : self.__email,
        "phone" : self.__phone,
        "password" : self.self.__password,
        "full_name" : self.__full_name,
        "user_type" : self.__user_type
        }

        return docs