# MultiVolumes
1. See MultiVolume10 for an ArcGIS 10x Toolbox tool (3d Analyst Required).

2. See Multivolumes for an ArcGIS Pro Toolbox tool (3d Analyst Required).

3. See the MultiVolumesFOSS4G for generating volume and fill tables using opensource tools.  This directory includes a read me.

For MultiVolumes10 and Multivolumes 

These tools will loop the surface volume tool in ArcToolbox (3D Analyst-Functional Surface-Surface Volumes) 
for a user-defined range of values and graduations.
These tools has been tested on ArcGIS 10.1  - 10.8 and ArcGIS Pro v2.9.  
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


The resulting comma delimited text file can be opened in LibreOffice Calc (or Excel if you are a sad victim of corporate hegemony) and the values manipulated to get the volumes at that graduation range only.  ArcGIS Pro outputs descriptive text to each line and the resulting CSV needs to be cleaned up.

NOTE:  The ArcGIS 10 version is better since it writes the graduation values, and the 2D areas, 3D areas, and volumes in a nicely formatted comma delimited txt file.  Note:  The FOSS4G tools are better since they do not skip or drop pixels and generate a complete table for all volumes.

