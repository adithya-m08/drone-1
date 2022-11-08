#import libraries
import time
from dronekit import *
#connect to vehicle
vehicle = connect('127.0.0.1:14551',baud = 921600,wait_ready=True)
#takeoff function
def arm_takeoff(height):
    #check if drone is ready
    while not vehicle.is_armable:
        print("waiting for drone")
        time.sleep(1)
    
    #change mode to guided and arm
    print("arming")
    vehicle.mode = VehicleMode('GUIDED')
    vehicle.armed=True

    #check if drone is armed
    while not vehicle.armed:
        print("waiting for arm")
    time.sleep(1)

    #takeoff
    print("takeoff")
    vehicle.simple_takeoff(10)

    #report altitude
    while True:
        
        print('reached',vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt>=height*0.95):
            print("reached target")
            break
        time.sleep(1)


#call takeoff function
arm_takeoff(10)
#hover for 10 secs
time.sleep(10)
#land
print("land")
vehicle.mode=VehicleMode("RTL")
time.sleep(20)

#close the connection
vehicle.close()