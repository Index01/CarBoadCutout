

class Observable(object):
    """Boring old observer pattern stuff. I considered using a pubsub pattern here but reasons."""
    def __init__(self, object):
        self.observers = []


    def register(self, observer):
        #TODO: Either convert this to a set, since no duplicate observers, or list comprehension. 
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        self.observers = [observer for observer in observers if observer != observer]    #Lulz


    def update_observers(self, dupdate):
        #print "observableArgs: %s" % dupdate	 
        for observer in self.observers:
            observer.update(dupdate)




