class Trip:
    def __init__(self, price, departure_point, destination_pont, rebate_percentage, company):
        self.__id = None
        self.__price = price
        self.__departure_point = departure_point
        self.__destination_pont = destination_pont
        self.__rebate_percentage = rebate_percentage
        self.__company = company

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def departure_point(self):
        return self.__departure_point
    
    @departure_point.setter
    def departure_point(self, new_departure_point):
        self.__departure_point = new_departure_point
    
    @property
    def destination_pont(self):
        return self.__destination_pont
    
    @destination_pont.setter
    def destination_pont(self, new_destination_pont):
        self.__destination_pont = new_destination_pont

    @property
    def rebate_percentage(self):
        return self.__rebate_percentage
    
    @rebate_percentage.setter
    def rebate_percentage(self, new_rebate_percentage):
        self.__rebate_percentage = new_rebate_percentage

    def creat_doc(self):
        docs =   {
        "price" : self.__price,
        "departure_point" : self.__departure_point,
        "destination_pont" : self.__destination_pont,
        "rebate_percentage" : self.__rebate_percentage,
        "company" : self.__company
        }

        return docs
