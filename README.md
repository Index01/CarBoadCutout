


# Car-dboard cutout

#################################################################
### Under construction 
#################################################################

Find groups of moving pixels and a draw a nice little box around them. Create a variety of filters for removing color channel data, include sliders for changing some of the paramaters to test lighting and filter conditions in relation to object detect or recognition. Many addtional steps need to be taken in order to improve the successful identification and contour resolution.



# Get it started
    pip 9.0.1, python2.7

## Real quick:
    > source [your/virtualenv/bin/activate]
    > pip install -r ./requirements.txt
    > python main.py --video ../static/inContent/20170219_freewayCarsStable.mp4


Protip: if you already have OpenCV=>3.1.0 (and cv2 for python) and you know it is working elsewhere on your system, you can copy the compiled shared object over to your site packages directory within your virtualenv. This also solves issues with NamedWindow errors from OpenCv. 

    > sudo find '/' -name 'cv2.so' 
    > mv /find/result/cv2.so /your/virtualenv/lib/python2.7/site-packages/cv2/cv2.so


If you do not have OpenCV installed, turn to page 43 and follow your own adventure for installing opencv from source, package manager, or other, for your specific platform.   



![alt text] (../static/inContent/capture.png "Running the quick start should produce the depicted results.")



  