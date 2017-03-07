

"""
   Create a VideoContainer instance and for no additional cost you get a NamedWindow, some sliders which are connected to 
   predefined functionality, maybe even a nice little histogram. 
"""

#__file__ = videoContainer.py


import cv2

import videoPlayer
import slider
from observable import Observable
from histoRender import HistoPyPlot

 
class VideoContainer():

    def __init__(self, inVid):
        """Early development. Instances can be simplified. I wanted to get it into version control."""

        """Create a window and a video player"""
        cv2.namedWindow('ContainerOne', cv2.WINDOW_NORMAL)
        self.player = videoPlayer.StaticVideo(inVid)
        self.firstFrame = None
 
        """Create some sliders"""
        #TODO: Fix the obvious problems. 
        self.thresholdFloorSlider = slider.Slider('ThresFloor-Slider', 'ContainerOne', 0, 255 )
        self.threshFloorSliderObservable = Observable(self.thresholdFloorSlider)

        self.thresholdMaxSlider = slider.Slider('ThresMax-Slider', 'ContainerOne', 0, 255 )
        self.threshMaxSliderObservable = Observable(self.thresholdMaxSlider)

        self.thresholdAdaptSlider = slider.Slider('AdaptiveMax-Slider', 'ContainerOne', 0, 255 )
        self.threshAdaptSliderObservable = Observable(self.thresholdAdaptSlider)

        self.histogramOne = HistoPyPlot('histoOne','ContainerOne')
        self.videoObservable = Observable(self.player)
 
        """Register some observers""" 
        self.threshAdaptSliderObservable.register(self.player)
        #self.videoObservable.register(histogramOne)

 
    def run_video(self):
        """Things that need to be updated on the regular"""
        thresholdFloor = self.thresholdFloorSlider.read_position()
        thresholdMax = self.thresholdMaxSlider.read_position()
        thresholdAdapt = self.thresholdAdaptSlider.read_position()
        #TODO: Clearly this is funky. Sort it out. 
        self.threshAdaptSliderObservable.update_observers({'thresholdFloor': thresholdFloor, 'threshMax': thresholdMax,
                                                    'threshAdaptiveMax': thresholdAdapt}) 
 
        """Here is where the magic happens. Press play and get the frame respons as a dict."""
        dplayResp = self.player.play(self.firstFrame) 

        try:
            self.firstFrame = dplayResp['firstFrame']
            threshFrame = dplayResp['threshFrame']
            frame = dplayResp['frame']
        except IndexError, e:
            print "Something missing here, brah. Exception: %s" % e 

        #videoObservable.update_observers({'frameIn': threshFrame})
        """Combine screen over lays and finally display some stuff."""
        #player.draw_rect(dplayResp['cnts'], threshFrame)
        #cv2.imshow('ContainerOne', threshFrame) 
        cv2.imshow('ContainerOne', frame) 
        """   
        for k,v in dplayResp.iteritems():
            print "key: %s" % k
            print "val: %s" % v
        """
        if dplayResp['ret'] is None:  
            cv2.destroyAllWindows()

        return

