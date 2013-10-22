#!/usr/bin/python

import sys
from prism import calc_prism, calc_macmillan, calc_pointmass
from math import sqrt, pow

dx, dy, dz = (10., 10., .1)

grav_pos = []
density_grid = []
r2exac = 10.
r2macm = 81.

# read density grid
fid = open(sys.argv[1],'r')
for line in fid:
    density_grid.append([float(x) for x in line.split()])
fid.close()

# read gravimeter positions
fid = open(sys.argv[2],'r')
for line in fid:
    grav_pos.append([float(x) for x in line.split()])
fid.close()
g, g_out  = ([],[])

fid = open(sys.argv[1]+'.out','w')
old_time_step = 1

for gp in grav_pos:
    g_sum = 0
    g_out =  []
    for prism in density_grid:
        time_step = prism[0]

        # there's a better way to do this
        if time_step != old_time_step:
            g_out.append([gp[0],old_time_step, g_sum])
            g_sum = 0;
            old_time_step = time_step
        
        dxMid = prism[1]
        dyMid = prism[2]
        dzMid = prism[3]
	hfin  = prism[4]
       
        # Calculate the distance to the mass to determine which formula to use
        rad = sqrt((dxMid-gp[1])**2 + 
                   (dyMid-gp[2])**2 +
                   (dzMid-gp[3])**2)
        r2  = rad**2
        dr2 = dx**2 + dy**2 + dz**2
        f2  = r2 / dr2
        #f2 = 1 
	if f2 <= r2exac: 
            #print 'prism'
            g_prism = calc_prism(dx, dy, dz,
                             dxMid, dyMid, dzMid,
                             hfin,
                             gp[1],gp[2],gp[3])
        elif f2 >= r2macm:
            #print ' mac'
            g_prism = calc_pointmass( hfin, dzMid, gp[3], dx, dy, dz, rad)
        else:
            #print 'pm'
            g_prism = calc_macmillan( hfin, dxMid, dyMid, dzMid, 
                                      gp[1], gp[2], gp[3],
                                      dx, dy, dz, rad)
        #g.append(g_prism)
        g_sum += g_prism
    # add final time step
    g_out.append([gp[0],old_time_step, g_sum])
    for line in g_out:
        fid.write('%i %i %3.3f\n'%(line[0],line[1],line[2]))
fid.close()


