try:
        import sys, arcpy, traceback
        arcpy.CheckOutExtension("3D")
        
        arcpy.AddMessage( "Multi-Volumes for ArcGIS 10")
        arcpy.AddMessage("Loop the 3D Analyst Surface Volume tools for a range of values...")
        arcpy.AddMessage("")
        arcpy.AddMessage("Copyright 2013, Gerry Gabrisch, GISP.  Lummi Natural Resources,  geraldg@lummi-nsn.gov")
        arcpy.AddMessage("")
        
        def GetValues(themessage, x):
                thevaluesatx = str(x)
                themessage = themessage.split("\n")
                thevalues = themessage[2].split("  ")
                for item in thevalues:
                        thevalue = item.split("=")
                        thevalue = thevalue[-1]
                        thevaluesatx = thevaluesatx + "," + str(thevalue)
                thevaluesatx = thevaluesatx +"\n"
                arcpy.AddMessage(thevaluesatx)
                return thevaluesatx
        
        
        #My_txt = r"C:\gTemp\Drone\MedicalCenter20200804\demUTMvolumesmeters.csv"
        #My_surface= r"C:\gTemp\Drone\MedicalCenter20200804\SurfaceModel\dirtpile"
        #direction = "ABOVE"
        #startingplane = 13
        #endingplane = 17.5
        #z = 1
        
        #graduations = 0.1
        ###q = 33
        
        My_surface= arcpy.GetParameterAsText(0)
        My_txt = arcpy.GetParameterAsText(1)
        direction = arcpy.GetParameterAsText(2)
        
        startingplane = float(arcpy.GetParameterAsText(3))
        z = float(arcpy.GetParameterAsText(4))
        graduations = float(arcpy.GetParameterAsText(5))
        endingplane = float(arcpy.GetParameterAsText(6))
        
        direction  = direction.upper()
        f = open(My_txt,'a')
        f.writelines(r"elevation, 2d_area, 3d_area, volume" + "\n")
        
        arcpy.AddMessage("Please wait, this script is processing...")
        
        if direction == "BELOW":
                arcpy.AddMessage("startingplane = " +str(startingplane))
                arcpy.AddMessage("endingplane = " +str(endingplane))
        
                while startingplane > endingplane:
                        arcpy.AddMessage("Getting Results...")
                        result = arcpy.SurfaceVolume_3d(My_surface, "", direction, startingplane)
                        thevaluesatx = GetValues(result.getMessages(0), startingplane)
                        f.writelines(thevaluesatx)
        
                        startingplane = startingplane - graduations
        
        if direction == "ABOVE":
                arcpy.AddMessage("Executing above...")
                x = startingplane
                while startingplane < endingplane:
                        result = arcpy.SurfaceVolume_3d(My_surface, "", direction, startingplane, z)
                        thevaluesatx = GetValues(result.getMessages(0), startingplane)
                        print thevaluesatx
                        f.writelines(thevaluesatx)
        
                        startingplane = startingplane + graduations
        
        
        f.close()
        
        arcpy.AddMessage("Finished without errors!")

except arcpy.ExecuteError: 
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs)  
#If the error is with the script, or with python, find error and report it to the screen...
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)

