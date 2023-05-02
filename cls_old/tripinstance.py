class TripInStance:
    def __init__(self, departure_date, time_out, has_meal, trip_status, trip):
        self.__id = None
        self.__departure_date = departure_date
        self.__time_out = time_out
        self.__has_meal = has_meal
        self.__trip_status = trip_status
        self.__trip = trip

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def departure_date(self):
        return self.__departure_date
    
    @departure_date.setter
    def departure_date(self, new_departure_date):
        self.__departure_date = new_departure_date

    def time_out(self):
        return self.__time_out
    
    @time_out.setter
    def time_out(self, new_time_out):
        self.__time_out = new_time_out

    @property
    def has_meal(self):
        return self.__has_meal
    
    has_meal.setter
    def has_meal(self, new_has_meal):
        self.__has_meal = new_has_meal

    @property
    def trip_status(self):
        return self.__trip_status
    
    @trip_status.setter
    def trip_status(self, new_trip_status):
        self.__trip_status = new_trip_status

    @property
    def trip(self):
        return self.__trip
    
    @trip.setter
    def trip(self, new_trip):
        self.__trip = new_trip

    def creat_doc(self):
        doc = {
            "departure_date" :  self.__departure_date, 
            "time_out" : self.__time_out,
            "has_meal" : self.__has_meal,
            "trip_status" : self.__trip_status,
            "trip" : self.__trip
        }
        return doc