#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    # print("HELLO! :) let's debug :vibing_potato:")
    bob = Visitor("Bob")
    sarah = Visitor("Sarah")
    rockymountains = NationalPark("Rocky Mountains")
    canada = NationalPark("Canada")
    # rockymountains.name = "Canada"
    newtrip = Trip(bob, rockymountains, "May 1st", "May 10th")
    newtrip2 = Trip(bob, rockymountains, "May 11th", "May 30th")
    newtrip3 = Trip(bob, canada, "June 5th", "June 10th")
    newtrip4 = Trip(sarah, canada, "May 11th", "May 30th")
    canadatrip = bob.create_trip(canada, "March", "December")
    print(rockymountains.best_visitor())
    
    # print(bob.trips())
    # print(len(bob.nationalparks()))
    # print(newtrip.national_park)
    # print(rockymountains.visitors())
    # ipdb.set_trace()
