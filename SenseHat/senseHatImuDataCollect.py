#! /usr/bin/python3
from sense_hat import SenseHat
from time import sleep
import csv

csv.register_dialect("hashes", delimiter=",")
f = open('IMU_data.csv','w+')
sense = SenseHat()

prev_theta_pitch = 0.0
prev_theta_roll = 0.0
Ts = 0.01
Kp = 0.5

with f:
    # writer = csv.writer(f, dialect='hashes')
    writer = csv.writer(f)
    writer.writerow(['pitch','pitch_est','roll','roll_est'])  

    while True:
        orientation = sense.get_orientation_degrees()
        # print("p: {pitch}, r: {roll}, y: {yaw} \n".format(**orientation))

        orientation_radians = sense.get_orientation_radians()

        raw_accel = sense.get_accelerometer_raw()
        # print("x: {x}, y: {y}, z: {z} \n".format(**raw_accel))

        gyro_raw = sense.get_gyroscope_raw()
        #print("p_dot: {x}, r_dot: {y}, y_dot: {z}".format(**gyro_raw))

        ## fusion algorithm
		# pitch angle estimation
        theta_pitch = prev_theta_pitch + (gyro_raw['x'] + prev_theta_roll * gyro_raw['z']) * Ts + Kp * (raw_accel['x'] - prev_theta_pitch)
		# roll angle estimation
        theta_roll = prev_theta_roll + (gyro_raw['y'] - prev_theta_pitch * gyro_raw['z']) * Ts + Kp * (raw_accel['y'] - prev_theta_roll)

        prev_theta_pitch = theta_pitch
        prev_theta_roll = theta_roll

        writer.writerow([orientation_radians['pitch'],theta_pitch*-1.0,orientation_radians['roll'],theta_roll])
        print("theta_pitch_est: {}".format(theta_pitch))
        print("p: {pitch},\n".format(**orientation_radians))

        print("theta_roll_est: {}".format(theta_roll))
        print("r: {roll},\n".format(**orientation_radians))
	  
        sleep(Ts)

f.close()