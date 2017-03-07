

#__file__ = slider.py

import cv2

from cutoutMessenger import Observable


class Slider(Observable):
    """Encapsulate and extend the cv2.trackbar functionality.
    
    """
    
    def __init__(self, sliderName, windowName, minVal, maxVal):
        """Make a nice little slider with a name and everything.
        
        Args:
            Param1 (str): Give an internally ref'd name.
            Param1 (str): Give a globally ref'd windowName.
            Param1 (int): Give minimum update val.
            Param1 (int): Give max val sent to update.
        
        """
        self.windowName = windowName
        self.pos = 0
        cv2.createTrackbar(sliderName, self.windowName, minVal, maxVal, self.set_pos)


    def set_pos(self, pos):
        """set_pos is called back by the openCv trackbar.
 
        One could theoretically want to call this independently. Callback for now. 
        """
        self.pos = pos
        return


    def read_position(self):
        """Just return the position of this particular instance.
   
        """
        return self.pos



