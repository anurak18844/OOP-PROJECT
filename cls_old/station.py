class Stations:
    def __init__(self, station_name, take_time_to_arrive):
        self.__station_name = station_name
        self.__take_time_to_arrive = take_time_to_arrive

    @property
    def station_name(self):
        return self.__station_name
    
    @station_name.setter
    def station_name(self, new_station_name):
        self.__station_name = new_station_name

    @property
    def take_time_to_arrive(self):
        return self.__take_time_to_arrive
    
    @station_name.setter
    def take_time_to_arrive(self, new_take_time_to_arrive):
        self.__take_time_to_arrive = new_take_time_to_arrive

    def create_departure_docs(self):
        docs = {
            "station_name" : self.__station_name,
            "take_time_to_arrive" : self.__take_time_to_arrive
        }

        return docs
