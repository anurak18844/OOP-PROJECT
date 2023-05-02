class Bus():
    def __init__(self, bus_number, color, owner_id):
        self.__id = None
        self.__bus_number = bus_number
        self.__color = color
        self.__owner_id = owner_id
        self.__seats = []

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def bus_number(self):
        return self.__bus_number
    
    @property
    def color(self):
        return self.__color
    
    @property
    def owner(self):
        return self.__owner_id
    
    @bus_number.setter
    def bus_number(self, new_bus_number):
        self.__bus_number = new_bus_number

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @owner.setter
    def owner(self, new_owner_id):
        self.__owner_id = new_owner_id

    def add_seat(self, seat):
        self.__seats.append(seat)

    def show_seats(self):
        for i in self.__seats:
            print(i)

    def create_bus_docs(self):
        seats = []
        for i in self.__seats:
            doc = {
                "seat_no" : i.seat_no, 
                "show" : i.show
            }
            seats.append(doc)

        docs = {
            "bus_number" : self.__bus_number,
            "color" : self.__color,
            "owner_id" : self.__owner_id,
            "seats" : seats
        }

        return docs

    def __str__(self):
        return f"bus_number : {self.__bus_number}, color : {self.__color}, owener_id : {self.__owner_id}"
    
