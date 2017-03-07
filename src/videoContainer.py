
"""VideoContainers have a videoPlayer and some Sliders and other things as we see fit.

Create a VideoContainer instance and for no additional cost you get a NamedWindow, some sliders connected to 
predefined functionality, maybe even a nice little histogram. 

"""

import cv2

import videoPlayer
import slider
from observable import Observable
from histoRender import HistoPyPlot

 
class VideoContainer():
    """Primary object for videoPlayer setup.

    Pass the video file or url or similar resource and the VideoContainer will
    handle creating control surfaces and getting the player started. 

    """

    def __init__(self, inVid):
        """Create the VideoContainer with the /path/videoFile as string. 
        Args:
            Param1 (str): Single video file location

        """

        # Create a window and a video player
        cv2.namedWindow('ContainerOne', cv2.WINDOW_NORMAL)
        self.player = videoPlayer.StaticVideo(inVid)
        self.firstFrame = None
 
        #Create some sliders
        #TODO: Fix the obvious problems. 
        self.thresholdFloorSlider = slider.Slider('ThresFloor-Slider', 'ContainerOne', 0, 255 )
        self.threshFloorSliderObservable = Observable(self.thresholdFloorSlider)

        self.thresholdMaxSlider = slider.Slider('ThresMax-Slider', 'ContainerOne', 0, 255 )
        self.threshMaxSliderObservable = Observable(self.thresholdMaxSlider)

        self.thresholdAdaptSlider = slider.Slider('AdaptiveMax-Slider', 'ContainerOne', 0, 255 )
        self.threshAdaptSliderObservable = Observable(self.thresholdAdaptSlider)

        self.histogramOne = HistoPyPlot('histoOne','ContainerOne')
        self.videoObservable = Observable(self.player)
 
        #Register some observers 
        self.threshAdaptSliderObservable.register(self.player)
        #self.videoObservable.register(histogramOne)

 
    def run_video(self):
        """Create the VideoContainer with the /path/videoFile as string. 

        run_video() is where we press play on the videoPlayer and update interested parties.
        Displaying the video frames is also the responsibility of this method, allowing 
        the state and timing to be controlled at a high level.

        Args:
            Param1 (str): Single video file location
        Returns:
            Exception when no further video frames available.
        """

        thresholdFloor = self.thresholdFloorSlider.read_position()
        thresholdMax = self.thresholdMaxSlider.read_position()
        thresholdAdapt = self.thresholdAdaptSlider.read_position()
        #TODO: Clearly this is funky. Sort it out. 
        self.threshAdaptSliderObservable.update_observers({'thresholdFloor': thresholdFloor, 
                                                           'threshMax': thresholdMax,
                                                           'threshAdaptiveMax': thresholdAdapt}) 
 
        #Here is where the magic happens. Press play and get the frame respons as a dict.
        dplayResp = self.player.play(self.firstFrame) 

        try:
            self.firstFrame = dplayResp['firstFrame']
            threshFrame = dplayResp['threshFrame']
            frame = dplayResp['frame']
        except IndexError, e:
            print "Something missing here, brah. Exception: %s" % e 

        #videoObservable.update_observers({'frameIn': threshFrame})

        #Finally display some stuff.
        #cv2.imshow('ContainerOne', threshFrame)    # This is a  total hack. Uncoment to view filter.
        cv2.imshow('ContainerOne', frame)           # Right now I am switching between frames here.

        """#20170306- Hack again. uncomment for debug print. 
        for k,v in dplayResp.iteritems():
            print "key: %s" % k
            print "val: %s" % v
        """
        if dplayResp['ret'] is None:  
            cv2.destroyAllWindows()

        return

