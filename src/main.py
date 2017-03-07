#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pull it all together. Ultimately this should be renamed to reflect the name of the package.

This module represents the first pass of an easy to use image recognition package for highlighting regions of interest and
applying filters for further analysis. 
"""


import sys
import argparse

import cv2

from videoContainer import VideoContainer


#First we setup an argparser for handling commandline video options.
parser = argparse.ArgumentParser(prog='main', description='Accept a /path/video with --video arg.\
                                              Foundation for further computer vision development. \
                                              Currently we can easily load a video file, apply filters and background \
                                              separation, identify contours and draw a box around them. Next steps \
                                              include contour analysis refinement. and Unittests.') 
parser.add_argument('--video', '-v', type=str , nargs='+', help='Accept a video with a path and do some cv')
parser.add_argument('--min_area', '-m', type=int, default=500,  nargs='+', help='Set the minimum area for foreground tracking')

args= parser.parse_args() 


def main(args):
    """Accep a video path and we will pull strings on OpenCv to draw boxes on moving groups of pixels.
    
    A loop needs to run in order to process each frame of video. I keep the loop at a high level
    in order to reduce statefullness further down the stack.
    """
 
    inVid = args.video[0]
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


