from priority_queue import *
import time

# Event Event --> boolean
# determines which Event comes first
def event_comes_before(event1, event2):
    return event1.time < event2.time

# an EventQueue consists of
# - a Priority Queue
# - 'time'
class EventQueue:
    def __init__(self, pqueue = empty_pqueue(event_comes_before), time = 0):
        self.pqueue = pqueue  # a Priority Queue
        self.time = time  # an int

    def __eq__(self, other):
        return type(other) == EventQueue and self.pqueue == other.pqueue and self.time == other.time

    def __repr__(self):
        return ('EventQueue(%r Time: %r)' %(self.pqueue, self.time))

# an EventClass consists of
# - a function
# - a time delay
class Event:
    def __init__(self, func, time=0):
        self.func = func  # a function that represents an event
        self.time = time  # an int that represents the priority of the event
    def __eq__(self, other):
        return type(other) == Event and self.func == other.func and self.time == other.time
    def __repr__(self):
        return ('EventClass(%r, %r)' % (self.func, self.time))

# EventQueue func time --> EventQueue
# returns an EventQueue with the added event
def add_event(equeue, func, time):
    event = Event(func, time + equeue.time)
    equeue.pqueue = enqueue(equeue.pqueue, event)

# EventQueue --> None
# runs the events in the EventQueue
def run_events(equeue):
    while not is_empty(equeue.pqueue):
        while equeue.time == peek(equeue.pqueue).time:
            event, equeue.pqueue = dequeue(equeue.pqueue)
            event.func(equeue)
        next_time = peek(equeue.pqueue).time - equeue.time
        time.sleep(next_time)
        equeue.time += next_time
