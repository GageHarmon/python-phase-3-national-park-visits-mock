# from .trip import Trip for my version
# from statistics import mode

class NationalPark:
    def __init__(self,name):
        if type(name) is str:
            self._name = name
        pass
    def get_name(self):
        return self._name
    
    def set_name(self,newname):
        print("Cannot change")
        
    name = property(get_name,set_name)

    def trips(self):
        from .trip import Trip
        triplist = []
        for trip in Trip.all:
            if trip.national_park == self:
                triplist.append(trip)
        return triplist

    def visitors(self):
        from .trip import Trip
        vislist = []
        for trip in Trip.all:
            if trip.national_park == self:
                vislist.append(trip.visitor)
        return list(set(vislist))
    
    def total_visits(self):
        from .trip import Trip
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count
    
    def best_visitor(self):
        from .trip import Trip
        countobject = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in countobject:
                    countobject[trip.visitor] = 1
                else:
                    countobject[trip.visitor] += 1
        max_key = max(countobject, key = countobject.get)
        return max_key
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # def __init__(self, name):
    #     self.set_name(name)
    
    # def get_name(self):
    #     return self._name

    # def set_name(self, name):
    #     if hasattr(self, "_name"):
    #         print ("Cannot change Park name!")
    #     elif (type(name) is str):
    #         self._name = name
    #         self.natparks_trips = []
    #         self.visitorlist = []
            
    # name = property(get_name, set_name)
            
    # def trips(self):
    #     self.natpark_trips = []
    #     for trip in Trip.all:
    #         if trip.national_park == self:
    #             self.natpark_trips.append(trip)
    #     return self.natpark_trips
    
    # def visitors(self):
    #     self.trips()
    #     self.visitor_list = []
    #     for trip in self.natpark_trips:
    #         if trip.visitor not in self.visitor_list:
    #             self.visitor_list.append(trip.visitor)
    #     return self.visitor_list
    
    # def total_visits(self):
    #     self.trips()
    #     return len(self.natpark_trips)
    
    # def best_visitor(self):
    #     self.visitors()
    #     return(mode(self.visitor_list))