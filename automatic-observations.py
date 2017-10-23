import os
import sys
    
class Meteor:

    def __init__(self, event_type, magnitude, timestamp):
        self.event_type = event_type
        self.magnitude = magnitude
        self.timestamp = timestamp
    
class Lmg:

    def __init__(self, event_type, value):
        self.event_type = event_type
        self.value = value

class Pause:

    def __init__(self, start, end):
        self.start = start
        self.end = end

def process_meteor(log):
    
        print("ovo je meteor")
        print(log.event_type)
        print(log.magnitude)
        print(log.timestamp)

def process_lmg(log):
    
        print("ovo je lmg")
        print(log.event_type)
        print(log.value)    
    
def process_pause(log):
    
        print("ovo je pauza")
        print(log.start)
        print(log.end) 


event_types = [("meteor", process_meteor), ("lmg", process_lmg), ("pause", process_pause)]

object1 = Meteor("meteor", 3, "13:33:45")
object2 = Lmg("lmg", "13:33:45")


observation = [object1, object2]

for log in observation:
    for event in event_types:
        if log.event_type == event[0]:
            event[1](log)
            break
 


