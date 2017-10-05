
from datetime import datetime
import itertools

class Call(object):

    id = itertools.count().next
    
    def __init__(self, name, phone, reason):
        self.id = "call" + str(Call.id())
        self.time = datetime.now().strftime("%H:%M")
        self.name = name
        self.phone = phone
        self.reason = reason
        self.info = [
            self.id,
            self.time,
            self.name,
            self.phone,
            self.reason
        ]

    def display(self):
        print "---"
        print "ID:", self.id
        print "Time", self.time
        print "Name:", self.name
        print "Phone:", self.phone
        print "Reason:", self.reason
        print "---"


class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue = int
    
    def add(self, id):
        self.calls.append(id.info)
        self.queue = len(self.calls)
        return self
    
    def remove(self):
        self.calls.remove(self.calls[0])
        self.queue = len(self.calls)
        return self

    def info(self):
        for call in self.calls:
            print call[2], "-", call[3]
        print "---"
        print "Queue:", self.queue, "calls"
        print "---"


cc = CallCenter()

call0 = Call("Adnan","123-456-7890","Complaint")
cc.add(call0)

call1 = Call("Olu","123-456-7890","Feedback")
cc.add(call1)

call2 = Call("Motuma","123-456-7890","Feedback")
cc.add(call2)

call3 = Call("Andrea","123-456-7890","Appreciation")
cc.add(call3)

call4 = Call("Jon","123-456-7890","Request")
cc.add(call4)

call5 = Call("Eduardo","555-555-5555","Prank")
cc.add(call5)

call0.display()

cc.info()

cc.remove()

cc.info()