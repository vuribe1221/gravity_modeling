Code Written by Victor Uribe in collaboration with Kyle Beard, York Meyers, and Jordan Gietz.

*This code assumes that you have access to Futuregrid or some other HTC/HPC and have cctools installed properly.

########################################################
#                                                      #
#                     Purpose                          #
#                                                      #
########################################################

&nbsp;&nbsp;&nbsp;Create a script that automatically generates a Makeflow file and uses futuregrid to simulate the gravity data collected by a gravitron.

########################################################
#                                                      #
#     Files needed for this project to be useful       #
#                                                      #
########################################################
files required to run code:  
1. grav.py   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*used to calculate the gravity given values in density_grid.txt.  
2. prism.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*dependency used by grav.py to calculate gravity in each prism.  
3. density_grid.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Predictions of subsurface water content (ie density) change.  
4. grav_pos.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Measurement/prediction locations.  
5. makeMakeflow.sh  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Main Script file used to create a custom Makeflow file then runs torque on the data outputing .out files with 3 values.  
6. addFiles.sh  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Dependency of makeMakeflow.sh in order to make more modular and simplify the whole process.  
                              
########################################################
#                                                      #
#            How to run makeMakeflow                   #
#                                                      #
########################################################

$ sh makeMakeflow.sh density_file N gravity_pos_file  
&nbsp;&nbsp;&nbsp;Where:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N = Number of peices to chop the density file into
    
########################################################
#                                                      #
#                        OUTPUT                        #
#                                                      #
########################################################

Output files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OUT  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Found in the present working directory
            
            
########################################################
#                                                      #
#                        Result                        #
#                                                      #
########################################################

Final Result: In red you can see the water (largest gravity) recede into the water table. About 7 seconds of simulation amounts to almost 7 hours of calculations on futuregrid.  
![alt tag](http://i243.photobucket.com/albums/ff91/redryno1221/Gravity_Modeling/56e4v.gif)
