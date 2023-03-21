class Visitor:

    def __init__(self,name):
        if type(name) is str:
            if len(name) <= 15 and len(name) > 0:
                self._name = name

    def get_name(self):
        return self._name
    def set_name(self,newname):
        print("Can't change")
    
    name = property(get_name,set_name)

    def trips(self):
        from .trip import Trip
        vislist = []
        for trip in Trip.all:
            if trip.visitor == self:
                vislist.append(trip)
        return vislist
    def nationalparks(self):
        from .trip import Trip
        parklist = []
        for trip in Trip.all:
            if trip.visitor == self:
                parklist.append(trip.national_park)
        return list(set(parklist))
    def create_trip(self, national_park, start_date, end_date):
        from .trip import Trip
        return Trip(self,national_park,start_date,end_date)
    
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # def __init__(self, name):
    #     self.set_name(name)
    
    # def get_name(self):
    #     return self._name

    # def set_name(self, name):
    #     if hasattr(self, "_name"):
    #         print ("Cannot change Visitor name!")
    #     elif (type(name) is str) and (1 <= len(name) <= 15):
    #         self._name = name
    #         self.visitor_trips = []
    
    # name = property(get_name, set_name)
    
    # def trips(self):
    #     self.visitor_trips = []
    #     for trip in Trip.all:
    #         if trip.visitor == self:
    #             self.visitor_trips.append(trip)
    #     return self.visitor_trips
    
    # def nationalparks(self):
    #     self.trips()
    #     self.natparks = []
    #     for trip in self.visitor_trips:
    #         if trip.national_park not in self.natparks:
    #             self.natparks.append(trip.national_park)
    #     return self.natparks          
    
    # def create_trip(self, national_park, start_date, end_date):
    #     Trip(self, national_park, start_date, end_date)