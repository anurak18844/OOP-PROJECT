class Seat():
    def __init__(self, seat_no, show):
        self.__seate_no = seat_no
        self.__show = show

    @property
    def seat_no(self):
        return self.__seate_no

    @property
    def show(self):
        return self.__show
    
    @seat_no.setter
    def seat_no(self, new_seat_no):
        self.__seate_no = new_seat_no

    @show.setter
    def show(self, new_show):
        self.__show = new_show

    def __str__(self):
        return f"seat_no : {self.__seate_no}, show : {self.__show}"