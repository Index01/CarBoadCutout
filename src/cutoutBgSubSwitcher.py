
""" Switch between different background subtraction algorithms

OpenCv and other vision tools support a varity of background subtraction algorithms
which is an important part in isolating regions of interest. This module should 
allow us to switch between several BgSub algorithms and abstract away dependencies.
I want to keep this module to functional programming, from the perspective of the
videoPlayer which will be using these functions, the calling object should just say 
hey awesome funtion here is some value, give me somthing back. Calling objects must 
also call select_bgSub_algorithm() for the algorithm it wants to subesquently apply. 
"""

import cv2


bgSubtractAlg = None

bgSubInstance = None 
check_is_bgInst = lambda instArg: instArg is bgSubInstance


class AlgorithmUndefinedError(Exception):
    def __init__(self):
        Exception.__init__(self, "you specified an undefined BgSub algorithm, brah.")


def check_alg(func):
    """Function decorator to bound bunk background algorithms

    Args:
        Param1 (function): A python function reference. 
    Returns:
        function call
    Exceptions:
        Raises AlgorithmUndefinedError if calling object gives lies.          
        Raises AttributeError if the arg is not a string.

    """
    def check_func(*ogArgs):
        
        try:
            globals()[ogArgs[0]] 
        except KeyError, e:
            raise AlgorithmUndefinedError()
        except AttributeError, e:
            print "BgSub algorithm arg not a string, brah. Exception: %s" % e 
            raise
        except IndexError, e:
            pass 
        return func(*ogArgs) 
    return check_func() 


@check_alg
def select_bgSub_algorithm(*inAlg):
    """Public function for you to choose an algorithm.
    
    It is assumed that you will only call this when switching to a different algorithm,
    otherwise to apply the selected algorithm just call apply_bg_subtract() 
    
    Args:
        Param1 (string): Algorithm name which must match known names. 
    Returns:
        A callable object, thats for darn sure. 
 
     """
 
    global bgSubtractAlg
    try:
        bgSubtractAlg = inAlg[0]
    except IndexError, e:
        bgSubtractAlg = "mog2"
        print "Setting backgound subtraction algorithm..."
    return lambda x : x    # Lulz. I freakin love python. You so silly. 


def apply_bg_subtract(frameIn):
    """Apply the pre-selected background subtraction algorithm to a given frame.

    Args:
        Param1 (frame): Frame for openCV 
    Returns:
        outFrame of type cv.[backgroung subtractor].apply, or None if bogus alorithm specified.         

    """
    outFrame = lambda x : x
    global bgSubInstance
    try:
        outFrame = globals()[bgSubtractAlg]
    except KeyError, e:
        print "Sorry brah, unsupported algorithm. Exception: %s" % e
    return outFrame(frameIn)


def mog2(frameIn):
    """MOG2 algorithm.

    Args:
        Param1 (frame): Frame for openCV 
    Returns:
        outFrame of type cv.createBackgroundSubtractioMOG2.apply.         

    """
    global bgSubInstance

    if not bgSubInstance:
        bgSubInstance =  cv2.createBackgroundSubtractorMOG2()
        print "Background subtraction set to Mog2." 
    outFrame = bgSubInstance.apply(frameIn)
 
    return outFrame


def mog():
    pass


def knn():
    pass

