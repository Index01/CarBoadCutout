

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
    print sbtktBgInstance
    outFrame = None
    try:
        bg = globals()[bgSubtractAlg]
    except KeyError, e:
        print "Sorry brah, unsupported algorithm. Exception: %s" % e

    print "I'm here"
    outFrame = bg(frameIn)

    print "frame in:"
    print frameIn
    print "outout:"
    print outFrame 
    return outFrame


def mog():
    pass

def mog2(frameIn):
    global sbtktBgInstance
    print sbtktBgInstance 
    #sbtktBgInstanceMog2 = cv2.createBackgroundSubtractorMOG2()
    if not sbtktBgInstance:
        sbtktBgInstance =  cv2.createBackgroundSubtractorMOG2()
        print "i'm somewhere I shouldn't beee."

    outFrame = sbtktBgInstance.apply(frameIn)
    print "out from in" 
    print outFrame
 
    return outFrame

def gmg():
    pass




def diff_some_frames():
    pass

def other_awesome_stuff():
    pass


