# code-for-paper
This is the source code for the manuscript "Yamashita N, Kodama Y, Irisa H, Ifuku T, Nakatani K, Uchiyama Y, Moritake H, Watanabe N. Mid-coronary Artery Wall Echogenicity Can Contribute to the Initial Diagnosis of Kawasaki Disease: Quantitative Measurements by Transthoracic Echocardiography. J Am Soc Echocardiogr. 2025 Dec 27:S0894-7317(25)00721-7. doi: 10.1016/j.echo.2025.12.013. Epub ahead of print. PMID: 41461298."


**Marking and Saving Regions**

1. Launch MaZda and select "File" → "Load image..." to load an ultrasound image in BMP format.

2. In the displayed image, mark the following regions:

  * Region of Interest (ROI) with red

  * Background region with green

3. After completing the marking, select "File" → "Save ROI".

4. In the "Save as type" dropdown, choose "non-overlapping regions (*.bmp)" and save the file as case001_ROI.bmp.



**Extracting Image Features**

1. Prepare the following two files:
  
 *	Original image: case001.bmp
  
 *	ROI-marked image: case001_ROI.bmp

 2. Open a terminal or command prompt and run the following command:

```
python CalcFeatures.py case001
```

3. The extracted image features will be saved in a file named Features.csv.
