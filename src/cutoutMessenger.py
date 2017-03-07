
""" Messenger module for abstracting function communication.

Currently this is good old fashioned observer pattern stuff. It may be replaced or
extended with pub sub in the future.
"""

from abc import ABCMeta, abstractmethod

class Observable(object):
    """Create an observable instance.
 
    Register, unregister and update observers. This is where we put the onus of 
    maintaining which observers should be updated.
    """
    def __init__(self, object):
        self.observers = []


    def register(self, observer):
        #TODO: Either convert this to a set, since no duplicate observers, or list comprehension. 
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        self.observers = [observer for observer in observers if observer != observer]    #Lulz


    def update_observers(self, dupdate):
        """I don't know much about 'dem observers, but I know they got a .update() method!
        
        Args:
            Param1 (dict) : They probably want a dict.
        Returns:
            None
        """
        #print "observableArgs: %s" % dupdate	 
        for observer in self.observers:
            observer.update(dupdate)


class Observer(object):
    """Inherit the observer, implement the abstract.

    Python has a nice abstract base class module, use it here. Objects 
    which are Observers must implement the update method, however they see fit.
    """ 
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, kwargs):
        """Abstract must do nothing.
   
        The abstract defines WHAT must be done, the concrete defines HOW it is done.
        """
        pass 


