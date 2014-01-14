Code Written by Victor Uribe in collaboration with Kyle Beard, York Meyers, and Jordan Gietz.

*This code assumes that you have access to Futuregrid or some other HTC/HPC and have cctools installed properly.


########################################################
#                                                      #
#     Files needed for this project to be useful       #
#                                                      #
########################################################
  files required 
  to run code:
		grav.py
			-used to calculate the gravity given values in 
				density_grid.txt.
		prism.py
			-dependency used by grav.py to calculate gravity 
				in each prism.
		density_grid.txt
			-Predictions of subsurface water content 
				(ie density) change.
		grav_pos.txt
			-Measurement/prediction locations.
		makeMakeflow.sh
			-Main Script file used to create a custom 
				Makeflow file then runs torque on the 
				data outputing .out files with 3 values.
		addFiles.sh
			-Dependency of makeMakeflow.sh in order to 
				make more modular and simplify the 
				whole process.
                              
########################################################
#                                                      #
#            How to run makeMakeflow                   #
#                                                      #
########################################################

$ sh makeMakeflow.sh <density_file> <N> <gravity_pos_file>
  Where:
    <N> = Number of peices to chop the density file into
    
########################################################
#                                                      #
#                        OUTPUT                        #
#                                                      #
########################################################

Output files:
           OUT
            -Found in the present working directory
            
            
########################################################
#                                                      #
#                        Result                        #
#                                                      #
########################################################            

Final Result:
http://s243.photobucket.com/user/redryno1221/media/Gravity_Modeling/56e4v.gif.html
