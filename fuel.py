import math

def calc_launch_fuel(mass, gravity):
    launch = int(mass*gravity*0.042-33)
    return launch

def calc_land_fuel(mass, gravity):
    land = int(mass*gravity*0.033-42)
    return land


def mass(ship_mass, params=[]):
    ov_fuel = 0
    params = params[::-1]

    for p in params:

        land = calc_land_fuel(ship_mass+ov_fuel, p[1])
        while(land>40):
            ov_fuel+=land
            land = calc_land_fuel(land, p[1])
        
        
        launch = calc_launch_fuel(ship_mass+ov_fuel, p[0])

        while(launch>40):
            ov_fuel+=launch
            print(launch)
            launch = calc_launch_fuel(launch, p[0])

    
    print(ov_fuel)
        
mass(28801, [(9.807, 1.62), (1.62, 9.807)])

