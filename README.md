


# Car-board cutout

### Under construction 

Find groups of moving pixels and draw a nice little box around them. Create a variety of filters for removing color and algorithms for background subtraction, include sliders for changing some of the paramaters to test lighting and filter conditions in relation to object detection. Many addtional steps need to be taken in order to improve successful identification and contour resolution.



# Get it started
    virtualenv 1.11, pip 9.0.1, python2.7

## Real quick:
    > source [your/virtualenv/bin/activate]
    > pip install -r ./requirements.txt
    > cd ./src/ && python main.py --video ../static/inContent/20170219_freewayCarsStable.mp4


Protip: if you already have OpenCV=>3.1.0 (and cv2 for python) and you know it is working elsewhere on your system, you can copy the compiled shared object over to your site packages directory within your virtualenv. This also solves issues with NamedWindow errors from OpenCv. 

    > sudo find '/' -name 'cv2.so' 
    > cp /find/result/cv2.so /your/virtualenv/lib/python2.7/site-packages/cv2/cv2.so


If you do not have OpenCV installed and working prior to using this code, turn to page 43 and follow your own adventure for installing opencv from source, package manager, or other, for your specific platform. Installing with pip will only compile some of the OpenCv options which may cause unknown errors. If it does not work out of the box follow the nice guides over at opencv for installing from source.   




Running the quick start should produce the depicted results.
![Alt text](https://github.com/Index01/CarBoadCutout/blob/master/static/inContent/capture.png "Out of the box results.")

  
