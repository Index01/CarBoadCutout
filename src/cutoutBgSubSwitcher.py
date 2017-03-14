
""" Switch between different background subtraction algorithms

OpenCv and other vision tools support a varity of background subtraction algorithms
which is an important part in isolating regions of interest. This module should 
allow us to switch between several BgSub algorithms and abstract away dependencies.
I want to keep this module to functional programming, from the perspective of the
videoPlayer which will be using these functions, the calling object should just say 
hey awesome funtion here is some value, give me somthing back. Calling objects must 
also setattr() for the algorithm it wants, this part may get a better interface 
definition in the future. 
"""

import cv2


bgSubtractAlg = None    #setattr() this value from calling object.
sbtktBgInstance = None
check_is_bgInst = lambda instArg: instArg is sbtktBgInstance

def apply_bg_subtract(frameIn):
    """Apply the pre-selected background subtraction algorithm to a given frame.

    Args:
        Param1 (frame): Frame for openCV 
    Returns:
        outFrame of type cv.[backgroung subtractor].apply, or None if bogus alorithm specified.         

    """
    outFrame = lambda x : x
    global sbtktBgInstance
    #TODO: Move this functionality up to the setattr(), caller should immdeiate except.
    try:
        outFrame = globals()[bgSubtractAlg]
    except KeyError, e:
        print "Sorry brah, unsupported algorithm. Exception: %s" % e

    return outFrame(frameIn)


def mog():
    pass

def mog2(frameIn):
    """MOG2 algorithm.

    Args:
        Param1 (frame): Frame for openCV 
    Returns:
        outFrame of type cv.createBackgroundSubtractioMOG2.apply.         

    """
    global sbtktBgInstance
    #sbtktBgInstanceMog2 = cv2.createBackgroundSubtractorMOG2()
    if not sbtktBgInstance:
        sbtktBgInstance =  cv2.createBackgroundSubtractorMOG2()
    outFrame = sbtktBgInstance.apply(frameIn)
 
    return outFrame


def gmg():
    pass


def knn():
    pass

