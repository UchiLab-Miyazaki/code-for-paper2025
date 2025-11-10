# -*- coding: utf-8 -*-

# -------------------------------------------------------------
#   Program to extract image features from ultrasound images
#  [How to run]
#    > python CalcFeatures.py bmp_filename
#    Do not add an extension to the bmp_filename
#  [Output]
#    Features.csv
# -------------------------------------------------------------

from xml.etree.ElementPath import get_parent_map
import numpy as np
import cv2
import sys

def main():
    argvs = sys.argv 
    argc = len(argvs) 
    if  (argc !=2):
        print('Usage: python CalcFeatures.py bmp_filename') 
        sys.exit(-1)
    # Get file name
    FileName = argvs[1]
    print(FileName)
    ImageFileName = FileName + '.bmp'    # Setting file name of input image
    ROIFileName = FileName + '_ROI.bmp'  # Setting file name of ROI image
    # Load image data
    OrgImage = cv2.imread(ImageFileName)
    ROIimage = cv2.imread(ROIFileName)
    # Convert the input image to a grayscale image
    GrayImage = TransGyarImage(OrgImage)
    # Converting the ROI image into grayscale values ​​for each region
    MarkerImage = Make_MarkerImage(ROIimage)
    # Calculation of image features
    roi_ave, contrast = CalcImageFeatures(GrayImage, MarkerImage)
    # Output of results (append mode)
    output = format("%s, %3.2f, %3.2f\n" % (FileName, roi_ave, contrast))
    with open("Features.csv", "a") as f:
        f.write(output)

# ---------------------------------------------------------------------
#    Converting the ROI image into grayscale values ​​for each region
#  [INPUT]
#    ROIimage : Marked image for each region
#  [RETURN]
#    MakerImage : Image with grayscale values ​​for each region
# ---------------------------------------------------------------------
def Make_MarkerImage(ROIimage):
    height, width, channel = ROIimage.shape  # The third element contains the color information.
    MarkerImage = np.zeros((height, width, 1), dtype=np.uint8)  # Initialization
    for y in range(height):
        for x in range(width):
            Red = ROIimage[y, x, 2].astype(np.float64)
            Green = ROIimage[y, x, 1].astype(np.float64)
            Blue = ROIimage[y, x, 0].astype(np.float64)
            if Red == 255 and Green == 0 and Blue == 0: MarkerImage[y, x] = 1
            if Red == 0 and Green == 255 and Blue == 0: MarkerImage[y, x] = 2
    return MarkerImage
    
# ------------------------------------------------------------------
#    Calculation of image features
#  [INPUT]
#    GrayImage : Gray scale of original image  
#    MarkerImage : Image with grayscale values ​​for each region
#  [RETURN]
#    roi_ave  : Average pixel value of the region of interest
#    contrast : Contrast of the area of ​​interest
# ------------------------------------------------------------------
def CalcImageFeatures(GrayImage, MarkerImage):
    height, width, channel = GrayImage.shape
    # Calculate the average pixel value of the region of interest
    roi_ave = 0.0
    roi_num = 0.0
    for y in range(height):
        for x in range(width):
            if MarkerImage[y, x] == 1:
                roi_ave += GrayImage[y, x].astype(np.float64)
                roi_num += 1.0
    if roi_num != 0.0: roi_ave = roi_ave / roi_num

    # Calculate the average pixel value of background
    bg_ave = 0.0
    bg_num = 0.0
    for y in range(height):
        for x in range(width):
            if MarkerImage[y, x] == 2:
                bg_ave += GrayImage[y, x].astype(np.float64)
                bg_num += 1.0
    if bg_num != 0.0: bg_ave = bg_ave / bg_num

    # Calculate contrast
    contrast = 0.0
    if bg_num != 0.0: contrast = roi_ave - bg_ave

    return roi_ave, contrast

# -------------------------------------------------------
#   Function for converting images to grayscale
# [INPUT]
#   InImage : Input image
# [RETURN]
#   OutImage : Output image
# -------------------------------------------------------
def TransGyarImage(InImage):
    height, width, channel = InImage.shape
    OutImage = np.zeros((height, width, 1), dtype=np.uint8)  # Initializing the output image
    for y in range(height):
        for x in range(width):
            Red = InImage[y, x, 2].astype(np.float64)
            Green = InImage[y, x, 1].astype(np.float64)
            Blue = InImage[y, x, 0].astype(np.float64)
            vale =  0.299 * Red + 0.587 * Green + 0.114 * Blue 
            OutImage[y, x] = vale.astype(np.uint8)
    return(OutImage)

if __name__ == '__main__':
    main()


