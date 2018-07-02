# Visflow

## Introduction

Code Written by Victor Uribe
<img src="https://i.imgur.com/SzLKWcz.png">
*This code assumes that you have access to Futuregrid or some other HTC/HPC and have cctools installed properly.

> Purpose -
Create a script that automatically generates a Makeflow file and uses Futuregrid (or other HTC systems) to simulate the gravity data collected by a gravity detector.

<a href="https://prezi.com/vwknpr_-ewh2/visflow/?utm_campaign=share&utm_medium=copy">Here is a Prezi presentation for more infomation about this project.</a>

## Result 

Final Result: In red you can see the water (largest gravity) recede into the water table. About 7 seconds of simulation amounts to almost 7 hours of calculations on futuregrid. This simulations took several days to put together on a laptop workstation where it took only 7 hours on Futuregrid.<br>
![alt tag](http://i243.photobucket.com/albums/ff91/redryno1221/Gravity_Modeling/56e4v.gif)


## Code Samples

> 
$ sh makeMakeflow.sh density_file N gravity_pos_file  
&nbsp;&nbsp;&nbsp;Where:  N = Number of peices to chop the density file into
<br>

## Output files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OUT  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Found in the present working directory

## Installation

> Files required to run code:  
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
            