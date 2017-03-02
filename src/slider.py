

#__file__ = slider.py

import cv2

from observable import Observable


class Slider(Observable):
    """Encapsulate and extend the cv2.trackbar functionality."""
    
    def __init__(self, sliderName, windowName, minVal, maxVal):
        self.windowName = windowName
        self.pos = 0
        cv2.createTrackbar(sliderName, self.windowName, minVal, maxVal, self.set_pos)


    def set_pos(self, pos):
        self.pos = pos
        return


    def read_position(self):
        return self.pos



