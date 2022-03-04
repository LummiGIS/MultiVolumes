import sys
import traceback
import numpy as np
from osgeo import gdal
try:
    #The input raster
    inras =r"Z:\GISpublic\GerryG\Python3\MultiVolumesFOSS4G\mt_swampy_forest.tif"
    #output file.
    output_csv = r"C:\gTemp\1a1a1a1a.csv"
    
    #The user defined graduations.  The output csv will contain a row for every graduation.
    graduations = 1
    
    #Create the gdal object...
    ds = gdal.Open(inras)
    
    def get_pixel_scaler(ds):
        '''reads the pixel sizes, multiplies them together to get the area of the cells.'''
        gt =ds.GetGeoTransform()
        return abs(gt[1]) * abs(gt[5])
    
    def get_value(ds):
        '''returns the nodata value, minimum, and maximum values of a single band raster'''
        band = ds.GetRasterBand(1)
        stat = band.GetStatistics(True, True)
        return (band.GetNoDataValue(), stat[0], stat[1])
    
    def  write_csv_line(this_elevation, graduation_area, graduation_volume):
        '''get and print the output file line values'''
        this_line =  str(this_elevation) + ',' + str(graduation_area) +','+ str(graduation_volume) + '\n'
        print(this_line)
        return this_line
           
    #Create the csv file and set to append values
    f = open(output_csv,'a')
    
    #Write the CSV header...
    f.writelines(r"elevation, 2d_area, volume" + "\n")
        
    #get the area of each pixel 
    pixel_scaler = get_pixel_scaler(ds)
    
    #get nodata, min, max values from the input raster...
    raster_values = get_value(ds)
    no_data = raster_values[0]
    ras_minimum = raster_values[1]
    ras_maximum = raster_values[2]
    
    #Summing up negative values will not work right.  If there are negative values in the input raster adjust all cell values to positive numbers by adding the absolute value of the
    #minimum value cell to all cells - if there are no minimum values then just add 0 below...
    if ras_minimum < 0:
        abs_min = abs(ras_maximum)
    else:
        abs_min = 0
    
    #Send the gdal object to a numpy array....
    myarray = np.array(ds.GetRasterBand(1).ReadAsArray())
    

    #a variable to store the total number of pixels.  This is just for quality control I guess. 
    total_pixel_count = 0
   
    #Here is the starting point for summing at increasing z raster values.
    this_elevation = ras_minimum
    
    while this_elevation <= ras_maximum:
        print('working on graduation ', this_elevation)
        this_graduation_pixel_count = 0
        #This hold the sum of all the pixel values above this graduation. Set it to 0 for this graduation
        graduation_total = 0           
        #Same as above but for volume calculations.
        graduation_volume = 0
        #Same as above but for area calculations
        graduation_area = 0
        
        #Iterate the numpy array
        for row in myarray: 
            for item in row:
                #do not sum nodata values or any value that is below the graduation value.
                if item != no_data and item >= this_elevation:
                    #make the adjustments for negative values.
                    item = item + abs_min
                    print(item)
                    #Track the sum of the pixels at this graduation.
                    graduation_total = graduation_total + item
                    #count the number of pixels at this graduation.
                    this_graduation_pixel_count +=1
                    #This is only needed at the first iteration as a quality control.
                    total_pixel_count +=1
                    
        #Just checking to see if the pixel count is correct for all pixels in the raster. 
        if this_elevation == ras_minimum:
            print('total data value pixel count = ',total_pixel_count)
        
        #get the volume which is sum of pixel heights * pixel area
        graduation_volume = graduation_total * pixel_scaler
        #Get the area of all the pixels in consideration which is pixel count * pixel area
        graduation_area = this_graduation_pixel_count * pixel_scaler
        #Write to the CSV file.
        this_line = write_csv_line(this_elevation, graduation_area, graduation_volume)
        f.writelines(this_line)
        this_elevation = this_elevation + graduations

    #close the csv file
    f.close()
    print('finished without error')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))