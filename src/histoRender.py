

import numpy as np
import matplotlib.pyplot as plt
#import cv2

from observer import Observer


class HistoPyPlot(Observer):

    def __init__(self, plotName, windowName):
        """Give me a plot name and a window name, I will create a histogram."""
        self.frameIn = np.zeros(shape=(5,2))
        self.fig = plt.figure()
        self.sp = self.fig.add_subplot(111) 
       
 
    def __plot_update__(self):
         
        self.sp.hist(self.frameIn.ravel(), 256, [0, 256]); self.fig.show()
        return

 
    def update(self, frameIn):
        self.frameIn = frameIn['frameIn']
        self.__plot_update__()
        return



