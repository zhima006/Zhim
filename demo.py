from abc import ABC, abstractclassmethod
class Observer(ABC):
     def update(self, event):...

class Subject():
     def __init__(self):
        self._observers=[]

     def attach(self, observer):
      self._observers.append(observer)

     def detach(self, observer):
         self._observers.remove(observer)

     def notify(self):
      for o in self._observers:
        o.update(self)

class Event(Subject):
     def __init__(self,title,
                 status= "scheduled"):
        super(). __init__()
        self.title=title
        self._status=status
     def get_state(self):
          return self._status

     def set_state(self, new_state):
        self._status=new_state
        self.notify()

class DashboardObs(Observer):
     def update(self, event):
          print("Dashboard state for the event:", event  .title, "has the state", event.get_state())
class EmailObs(Observer):
     def update(self, event):
          print("Dashboard state for the event:", event  .title, "has the state", event.get_state())

introparty=Event("intro party")
introparty.attach(DashboardObs())
introparty.attach(EmailObs())
introparty.set_state("Completed")
