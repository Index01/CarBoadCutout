

#__file__ = videoPlayer.py

"""
   Video player objects will allow a static video or video stream to be passed in and the respective objects will serve as an 
   entry point for further computer vision development. 
"""

import numpy as np
import ntpath

import imutils
import cv2

from observer import Observer
from observable import Observable


class StaticVideo(Observer, Observable):
    """sBout to get self-ie up in hurrr."""
   
    def __init__(self, fullVidName):
        self.fullVidName = fullVidName
        self.vidName = ntpath.basename(fullVidName)
        self.vidPath = ntpath.dirname(fullVidName)

        self.capture = cv2.VideoCapture(fullVidName) 

        self.dThreshLims = {'thresholdFloor': 0, 'threshMax': 255, 'threshAdaptiveMax': 255}

        self.fgroundBground = cv2.createBackgroundSubtractorMOG2()

    def __frame_delta_thresh__(self, frame, firstFrame):
        """Accept a frame of video and return a dictionary."""
 
        """Filter the frame. Maybe make this a switch later."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if firstFrame is None:
            print "first frame is None!!!"
            firstFrame = gray

        """Calculate the difference between the first, theoretically empty, frame and the most recent."""
        frameDelta = cv2.absdiff(firstFrame, gray)
 
        """Use some CV magic to contrast foreground and background"""
        thresh = self.fgroundBground.apply(gray) 
    
     
        """Set a threshold floor then apply adaptive threshold from cv2"""
        #thresh = cv2.threshold(frameDelta, self.dThreshLims['thresholdFloor'], self.dThreshLims['threshMax'], cv2.THRESH_BINARY)[1]
        #thresh = cv2.adaptiveThreshold(theFrame, self.dThreshLims['threshAdaptiveMax'], 
        #                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 127, 2) 

        """Return a dict with frame related info."""
        return {'frameDelta': frameDelta, 'thresh': thresh, 'firstFrame': firstFrame}


    def __frame_contour__(self, thresh):
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
 

    def draw_rect(self, cnts, frameName):
        try:
            x, y, w, h = cv2.boundingRect(cnts)
        except IndexError, e:
            print "No contours here, brah. Exception: %s" % e
        except TypeError, e:
            print "Not a numpy array, brah. ExceptionL %s" % e         
        
        cv2.rectangle(frameName,(x,y), (x+w, y+h), (0, 0, 255), 2)
        cv2.rectangle(frameName, (250, 120), (750, 450), (0, 255, 0), 2)
        return


    def update_threshLims(self, dThreshUpdate):
        """Accept a dictionary, if the keys match the threshold limits dictionary keys, update the vals."""
        try: 
            self.dThreshLims.update({k:v for k,v in dThreshUpdate.iteritems() 
                                                 if self.dThreshLims.has_key(k)})
        except AttributeError, e:
            print 'Not a dictionary, brah. Exception: %s' % e 
        return


    def update(self, dsliderPos):
        """This is the implementation of the the observer abstract function."""
        self.update_threshLims(dsliderPos)
        return


    def play(self, firstFrame): 
        """Here is our main entry point. The video player is given a video name and path at the 
           time of instantiation. Play only requires a firstFrame so the function can remain stateless.""" 
        ret, frame = self.capture.read()
        frame = imutils.resize(frame, width=1000)
        
        threshFrameDelta = self.__frame_delta_thresh__(frame, firstFrame)
            
        firstFrame = threshFrameDelta['firstFrame']
        threshFrame = threshFrameDelta['thresh']
        cnts = [] 
        try: 
            """This state can occur on the first time through."""
            cnts = self.__frame_contour__(threshFrame)   
            self.draw_rect(cnts, frame)
        except ValueError, e: 
            pass

        k = cv2.waitKey(30) & 0xff
            
        if ret is None: 
            print "release"
            cap.release()
 
        return {'ret': ret, 'frame': frame, 'firstFrame': firstFrame,
                'threshFrame': threshFrame,'cnts': cnts,} 
       



class VideoStream:
    pass





