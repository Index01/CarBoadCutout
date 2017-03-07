
"""VideoContainers have a videoPlayer and some Sliders and other things as we see fit.

Create a VideoContainer instance and for no additional cost you get a NamedWindow, some sliders connected to 
predefined functionality, maybe even a nice little histogram. 

"""

import cv2

import videoPlayer
import slider
from cutoutMessenger import Observable
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

        # Create some Observable instances with respective base classes.
        self.sliderObservable = Observable(slider)
        self.videoObservable = Observable(videoPlayer)
 
        #Create some sliders
        self.thresholdFloorSlider = slider.Slider('ThresFloor-Slider', 'ContainerOne', 0, 255 )
        self.thresholdMaxSlider = slider.Slider('ThresMax-Slider', 'ContainerOne', 0, 255 )
        self.thresholdAdaptSlider = slider.Slider('AdaptiveMax-Slider', 'ContainerOne', 0, 255 )
        self.filterViewSlider = slider.Slider('filterView-Slider', 'ContainerOne', 0, 1)
        self.histogramOne = HistoPyPlot('histoOne','ContainerOne')

        #Register some observers 
        self.sliderObservable.register(self.player)    #I'm registering these with the instance for now.
        self.videoObservable.register(self.histogramOne)

 
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
        filterView = self.filterViewSlider.read_position()
        self.sliderObservable.update_observers({'thresholdFloor': thresholdFloor, 
                                                'threshMax': thresholdMax,
                                                'threshAdaptiveMax': thresholdAdapt,
                                                'filterView': filterView}) 
 
        #Here is where the magic happens. Press play and get the frame respons as a dict.
        dplayResp = self.player.play(self.firstFrame) 

        try:
            self.firstFrame = dplayResp['firstFrame']
            threshFrame = dplayResp['threshFrame']
            frame = dplayResp['frame']
            dispFrame = dplayResp['displayFrame']
        except IndexError, e:
            print "Something missing here, brah. Exception: %s" % e 

        #self.videoObservable.update_observers({'frameIn': threshFrame})

        #Finally display some stuff.
        cv2.imshow('ContainerOne', dispFrame)

        """#20170306- This is a total hack. uncomment for debug print. 
        for k,v in dplayResp.iteritems():
            print "key: %s" % k
            print "val: %s" % v
        """
        if dplayResp['ret'] is None:  
            cv2.destroyAllWindows()

        return

