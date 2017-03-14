
""" Switch between different background subtraction algorithms

OpenCv and other vision tools support a varity of background subtraction algorithms
which is an important part in isolation regions of interest. 
"""

import cv2


bgSubtractAlg = None
sbtktBgInstance = None
check_is_bgInst = lambda instArg: instArg is sbtktBgInstance

def apply_bg_subtract(frameIn):
    """Apply the pre-selected background subtraction algorithm to a given frame.

    Args:
        Param1 (frame): Frame for openCV 
    Returns:
        outFrame of type cv.[backgroung subtractor].apply, or None if bogus alorithm specified.         

    """
    bg = lambda x : x
    global sbtktBgInstance
    outFrame = None
    try:
        bg = globals()[bgSubtractAlg]
    except KeyError, e:
        print "Sorry brah, unsupported algorithm. Exception: %s" % e

    outFrame = bg(frameIn)

    return outFrame


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




def diff_some_frames():
    pass

def other_awesome_stuff():
    pass


