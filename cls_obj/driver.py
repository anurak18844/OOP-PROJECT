from cls_old.account import Account

class Driver(Account):
    def __init__(self, email, phone, password, first_name, last_name, user_type, bus_driver):
        super().__init__(email, phone, password, first_name, last_name, user_type)
        self.__buss_driver = bus_driver
        self.__id = None

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def bus_driver(self):
        return self.__bus_driver
    
    @bus_driver.setter
    def bus_driver(self, new_bus_driver):
        self.__bus_driver = new_bus_driver

    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, first_name : {self.__first_name}, last_name : {self.__last_name}, user_type : {self.__user_type}, bus_driver : {self.__bus_driver}"