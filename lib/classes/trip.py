from .visitor import Visitor
from .national_park import NationalPark

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        pass
    def get_national_park(self):
        return self._national_park
    def set_national_park(self,input):
        if type(input) == NationalPark:
            self._national_park = input
        else:
            print("Not valid park")
    national_park = property(get_national_park,set_national_park)

    def get_visitor(self):
        return self._visitor
    def set_visitor(self,input):
        if type(input) == Visitor:
            self._visitor = input
        else:
            print("Not valid visitor")
    visitor = property(get_visitor,set_visitor)
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    # def __init__(self, visitor, national_park, start_date, end_date):
    #     self.visitor = visitor
    #     self.national_park = national_park
    #     self.set_start_date(start_date)
    #     self.set_end_date(end_date)
    #     Trip.all.append(self)
        
        
    # def get_start_date(self):
    #     return self._start_date

    # def set_start_date(self, start_date):
    #     if (type(start_date) is str):
    #         self._start_date = start_date
    
    # start_date = property(get_start_date, set_start_date)
        
    
    # def get_end_date(self):
    #     return self._end_date

    # def set_end_date(self, end_date):
    #     if (type(end_date) is str):
    #         self._end_date = end_date
    
    # end_date = property(get_end_date, set_end_date)