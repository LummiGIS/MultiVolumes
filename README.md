# MultiVolumes
Loops the 3D analyst Surface Volume tool for a user defined range of values.


MultiVolumes for ArcGIS 10 and 10.1 and MultiVolumes for ArcGIS Pro


These tools will loop the surface volume tool in ArcToolbox 
(3D Analyst-Functional Surface-Surface Volumes) 
for a user-defined range of values and graduations.

Given a surface and an elevation graduation value, 
this tool will calculate the surface area, the volume, 
and the 3-D surface area at each graduation.  The data 
from each graduation are written to a comma delimited text 
file.

Input Parameters
1. A surface model. (raster)
2. An output text file to store results as a comma delimited text file.
3. Whether you want to calculate above or below your starting elevation value.
4. The starting elevation in surface model z units.
5. Z value scalar.
6. The graduation value in surface model z units.
7. The elevation to stop the calculations.


These tools has been tested on ArcGIS 10.1  - 10.8 and ArcGIS Pro v2.9.  These tools requires the 3-D Analyst extension.

NOTE:  The ArcGIS 10 version is better since it writes the graduation values, and the 2D areas, 3D areas, and volumes in a nicely formatted comma delimited txt file.
This comma delimited text file can be opened in LibreOffice Calc (or Excel if you are a sad victim of corporate hegemony) and the values manipulated to get the volumes at that graduation range only.  ArcGIS Pro outputs a heap of extra garbage text and I have not gotten around to parcing those data yet.  Sorry for that - stand by for an updated version.  Thanks again for finding new ways to ruin your software ESRI.  ArcGIS Pro sucks.
