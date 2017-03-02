#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   This module represents the first pass of an easy to use image recognition package for highlighting regions of interest and
   applying filters for further analysis. 
"""


import sys
import argparse

import cv2

from videoContainer import VideoContainer


"""First we setup an argparser for handling commandline opvideo. Yanking this boilerplate from img suff."""
parser = argparse.ArgumentParser(prog='main', description='Accept a /path/video with --video arg. Some foundation for further computer vision development is provided in the existing code base. Much further work is required but I want the basic structure for easily loading a video file or stream which will then have some regions or interest and filters applied. Next we want to grab the regions of interest and perform further contour analysis on the groupings of pixelzzz.')
parser.add_argument('--video', '-v', type=str , nargs='+', help='Accept a video with a path and do some cv')
parser.add_argument('--min_area', '-m', type=int, default=500,  nargs='+', help='Set the minimum area for foreground tracking')

args= parser.parse_args() 



def main(args):
    """Accep a video path and we will pull strings on OpenCv to draw boxes on moving groups of pixels."""
    #TODO: All of the things
 
    inVid = args.video[0]
    #minArea = args.min_area 
    firstFrame = None

    staticVideoContainerOne = VideoContainer(inVid)
    
    while(1):
        staticVideoContainerOne.run_video()



if __name__=='__main__':
    try:
        sys.argv[1]
    
    except IndexError:
        parser.print_help()
        sys.exit(1)
   
    main(args)



