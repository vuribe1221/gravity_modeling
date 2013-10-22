def calc_prism( dx, dy, dz, dxMid, dyMid, dzMid, Hfin, posX, posY, posZ):
    #print    dx, dy, dz, dxMid, dyMid, dzMid, Hfin, posX, posY, posZ
    import math
    GAMMA=6.67e-8
    RHO=1

    x = [ dxMid - dx/2 - posX, dxMid + dx/2 - posX ]
    y = [ dyMid - dy/2 - posY, dyMid + dy/2 - posY ]
    z = [ dzMid - dz/2 - posZ, dzMid + dz/2 - posZ ]

    gsum = 0;
    for i in range(2):    
        for ii in range(2):
            for iii in range(2):
                rf = math.sqrt((math.pow(x[i],2) + math.pow(y[ii],2) + math.pow(z[iii],2)))
                gsum += math.pow(-1,(i+ii+iii+3))*(x[i]*math.log(y[ii] + rf) + y[ii] * math.log(x[i]+rf) -z[iii]*math.atan(x[i]*y[ii]/z[iii]/rf))

    return GAMMA * Hfin * RHO * 1e8 * gsum

def calc_pointmass( Hfin , dzMid, posZ, dx, dy, dz, rad):
#    print  Hfin , dzMid, posZ, dx, dy, dz, rad 
    return -6.67e-8 * Hfin * 1e8 * dx * dy * dz * (dzMid-posZ)/rad**3
   
def calc_macmillan( Hfin, dxMid, dyMid, dzMid, posX, posY, posZ, dx, dy, dz, rad):
    #print Hfin, dxMid, dyMid, dzMid, posX, posY, posZ, dx, dy, dz, rad
    alfa = 2*dx**2 - dy**2 - dz**2
    beta = -dx**2 + 2*dy**2 - dz**2
    ome = -dx**2 - dy**2 + 2*dz**2
    abg = alfa * (dxMid-posX)**2 + beta * (dyMid-posY)**2 + ome * (dzMid-posZ)**2

    tm1 = (dzMid-posZ) / rad**3
    tm2 = 5 * (dzMid - posZ) * abg / 24 / rad**7
    tm3 = -ome * (dzMid - posZ) / 24 / rad**5

    return -6.67e-8 * Hfin * 1e8 * dx * dy * dz * (tm1 + tm2 + tm3)
