
"""Create a VideoPlayer to display and peel off frames of video for further processing.

Video player objects will allow a static video or video stream to be passed in and the respective objects will serve as an 
entry point for further computer vision development. VideoPlayer objects have a stream or file name passed to them at the 
time of creation, allowing us to create several atomic instances of the VideoPlayer.  

TODO: 
    Define the video stream class.
    Create shared functions independent of videoPlayer types.

"""


import numpy as np
import ntpath

import imutils
import cv2

from cutoutMessenger import Observer, Observable

def frame_delta_thresh(videoPlayer, frame, firstFrame, dThreshLims):
    """Accept a frame of video and return a dictionary.

    Args:
        Param1 (): Frame object compatible with OpenCV, [frame].
        Param2 (): The first frame of the video, or none.
        Param3 (dict): dThreshLims must contain thresholdFloor, threshMax and threshAdaptiveMax.
        
    Returns:
        Dictionary of Frame results. 

    """
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray
       
    # Diff the first and last frame then apply MOG2 algorithm.
    frameDelta = cv2.absdiff(firstFrame, gray)     
    thresh = videoPlayer.fgroundBground.apply(gray) 
    
    #20170306 - These may be useful in different lighting, causing problems now
    try:
        #Set a threshold floor then apply adaptive threshold from cv2
        thresh = cv2.threshold(frameDelta, dThreshLims['thresholdFloor'], 
                                           dThreshLims['threshMax'], 
                                           cv2.THRESH_BINARY)[1]
        thresh = cv2.adaptiveThreshold(thresh, dThreshLims['threshAdaptiveMax'], 
                                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                               cv2.THRESH_BINARY, 127, 2) 
    except KeyError, e:
        print "Missing keys, brah. Exception: %s" % e

    # Return a dict with frame related info.
    return {'frameDelta': frameDelta, 'thresh': thresh, 'firstFrame': firstFrame}


def frame_contour(thresh):
    """Accept a thresh from the frame_delta_thresh.
      
    Thresh is a openCV frame object, post threshold processing and foreground 
    separation has occured. The frame_contour mathod wants a nice clean video frame
    for the highest possible success of identifying contour groups. 

    Args:
        Param1 (): Frame object compatible with OpenCV, [frame].
        
    Returns:
        List of contour cooidinates. 

    """
 
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contourResp = []
    #print "contours: %s"  % [cnts for cnts in contours[0]] 
    try:
        area = [cv2.contourArea(c) for c in contours] 
        maxIndex = np.argmax(area)
        contourResp = contours[maxIndex]
    except ValueError, e:
        raise e 
    return contourResp
 

def draw_rect(cnts, frameName):
    """Accepts contours and a frame to update, returns None.

    Args:
        Param1 (): Contours object compatible with OpenCV [contours].
        Param2 (): Name of the video frame to draw rectangles on.
        
    Returns:
        None if successful. 

    """
 
    try:
        x, y, w, h = cv2.boundingRect(cnts)
    except IndexError, e:
        print "No contours here, brah. Exception: %s" % e
    except TypeError, e:
        print "Not a numpy array, brah. ExceptionL %s" % e         
        
    cv2.rectangle(frameName,(x,y), (x+w, y+h), (0, 0, 255), 2)
    cv2.rectangle(frameName, (250, 120), (750, 450), (0, 255, 0), 2)
    return


class StaticVideo(Observer, Observable):
    """StaticVideo instances handle locally available video content.
    
    A StaticVideo will be created with a video accessible on the os path, no video no StaticVideo instance
    which intentionaly gives us a 1-to-1 relationship. Module implementations may create N number of 
    StaticVideo instances, for example allowing some to display color video and others to show filtered frames.   
  
    """
   
    def __init__(self, fullVidName):
        """ Create an instance with a video available on the OS Path

        Module implementations may create multiple instances of StaticVideo players and they can 
        be synced to show frames at the same time. They must have a video locally available.

        Args:
            Param1 (str): Relative or absolute path to video file object.

        """

        self.fullVidName = fullVidName
        self.vidName = ntpath.basename(fullVidName)
        self.vidPath = ntpath.dirname(fullVidName)
        self.camView = 0
        self.capture = cv2.VideoCapture(fullVidName) 

        self.fgroundBground = cv2.createBackgroundSubtractorMOG2()
        self.dThreshLims = {'thresholdFloor': 0, 'threshMax': 255, 'threshAdaptiveMax': 255}


    def update_threshLims(self, dThreshUpdate):
        """Accept a dictionary, if the keys match the threshold limits dictionary keys, update the vals.

        Args:
            Param1 (): Dictionary for threshold vals update.
        
        Returns:
            None if successful. 

        """
 
        try: 
            self.dThreshLims.update({k:v for k,v in dThreshUpdate.iteritems() 
                                                 if self.dThreshLims.has_key(k)})
        except AttributeError, e:
            print 'Not a dictionary, brah. Exception: %s' % e 
        return


    def update_camView(self, dUpdates):
        """If the filterview is true, switch

        Args: 
            Param1 (dict): update the camview based on filter flag
        """
        try: 
            self.camView = dUpdates['filterView']
        except KeyError, e:
            pass


    def update(self, dsliderPos):
        """This is the implementation of the the observer abstract function.
 
        The reason this function and the update_threshLims are both here and public
        is so we can fullfil the abstract contract and update local methods and shown below.
        If in the future we want to do other things, define another method and call it here.
        Args:
            Param1 (dict): Dictionary for threshold vals update.
        
        Returns:
            None if successful. 

        """
        
        self.update_threshLims(dsliderPos)
        self.update_camView(dsliderPos)
        return


    def play(self, firstFrame): 
        """Play the video file passed to StaticVideo object at time of creation.

        Here is our main entry point. The video player is given a video name and path at the 
        time of instantiation. Play only requires a firstFrame so the function can remain stateless. 

        Args:
            Param1 (): Dictionary for threshold vals update.
        
        Returns:
            Dictionary {'ret','frame','firstFrame','threshFrame','cnts','displayFrame'}. 

        """
        ret, frame = self.capture.read()
        frame = imutils.resize(frame, width=1000)
                    
        threshFrameDelta = frame_delta_thresh(self, frame, firstFrame, self.dThreshLims)
        firstFrame = threshFrameDelta['firstFrame']
        threshFrame = threshFrameDelta['thresh']
        cnts = [] 
        try: 
            # This state can occur on the first time through.
            cnts = frame_contour(threshFrame)   
            draw_rect(cnts, frame)
        except ValueError, e: 
            pass

        k = cv2.waitKey(30) & 0xff
            
        if ret is None: 
            print "release"
            cap.release()

        if self.camView:
            dispFrame = threshFrame
        else:
            dispFrame = frame
 
        return {'ret': ret, 'frame': frame, 'firstFrame': firstFrame,
                'threshFrame': threshFrame,'cnts': cnts, 'displayFrame': dispFrame} 
       



class VideoStream:
    pass





