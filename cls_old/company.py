from cls_old.userType import UserType
class Company():
    def __init__(self, email, phone, password, img, company_name, user_type):
        self.__email = email
        self.__phone = phone
        self.__password = password
        self.__img = img
        self.__company_name = company_name
        self.__user_type = UserType(user_type).name

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
    def img(self):
        return self.__img
        
    @property
    def company_name(self):
        return self.__company_name
        
    @property
    def user_type(self):
        return self.__user_type
        

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @img.setter
    def img(self, new_img):
        self.__img = new_img

    @company_name.setter
    def companany_name(self, new_company_name):
        self.__company_name = new_company_name

    @user_type.setter
    def user_type(self, new_user_type):
        self.__user_type = UserType(new_user_type).name

    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, img : {self.__img}, company_name : {self.__company_name}, user_type : {self.__user_type}"
        
    def create_company_docs(self):
        company_docs = {
            "email" : self.__email,
            "phone" : self.__phone,
            "password" : self.__password,
            "img" : self.__img,
            "company_name" : self.__company_name,
            "user_type" : self.__user_type
        }

        return company_docs