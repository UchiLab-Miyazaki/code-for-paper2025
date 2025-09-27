# code-for-paper
This is the source code for the manuscript currently under peer review. Please handle it with care.

Marking and Saving Regions

(1) Launch MaZda and select "File" → "Load image..." to load an ultrasound image in BMP format.

(2) In the displayed image, mark the following regions:

  •	Region of Interest (ROI) with red

  •	Background region with green

(3) After completing the marking, select "File" → "Save ROI".

(4) In the "Save as type" dropdown, choose "non-overlapping regions (*.bmp)" and save the file as case001_ROI.bmp.



Extracting Image Features

(1) Prepare the following two files:
  
  •	Original image: case001.bmp
  
  •	ROI-marked image: case001_ROI.bmp

(2) Open a terminal or command prompt and run the following command:
  
  python CalcFeatures.py case001

(3) The extracted image features will be saved in a file named Features.csv.
