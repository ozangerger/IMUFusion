# IMUFusion
 Different IMU fusion algorithms will be implemented and tested.
 
 First algorithm uses 6-dof IMU. Roll and pitch angles are coupled w.r.t yaw rate.

 Hardware:
 https://www.raspberrypi.org/products/raspberry-pi-4-model-b/ (4GB ram)
 https://www.raspberrypi.org/products/sense-hat/
 
 Coding language:
 Python
 
 The tests are validated against the ground truth data collected from internal 9-dof IMU fusion of SenseHat.
# Test 1 - Test drive on the road - Pitch and Roll Fusion using 6-dof IMU inside SenseHat of Raspberry PI 4
Raspberry Pi 4 is connected to my laptop through Thunderbolt port and powered from there. Data connection is made through ethernet port of the raspberry pi, and over usb-to-ethernet adaptor to the laptop. By assigning static IP's to both devices, SSH'ing is now possible and python script can be started using SSH protocol.

More figures and collected data are available for further analysis in this link: https://github.com/ozangerger/IMUFusion/tree/master/SenseHat/example2

![Example](/SenseHat/example2/setup.jpeg)
<p align="center">Figure 1: Test setup for the measurements</p>

![Example](/SenseHat/example2/IMU_data.png)
<p align="center">Figure 2: All inertial measurements and estimations for test drive from home to work </p>

![Example](/SenseHat/example2/IMU_data_t0_t250.png)
<p align="center">Figure 3: Roll-pitch measurements and estimations between t=0s and t=250s </p>

![Example](/SenseHat/example2/IMU_data_t1000_t1250.png)
<p align="center">Figure 4: Roll-pitch measurements and estimations between t=1000s and t=1250s </p>

# Test 2 - Pitch and Roll Fusion using 6-dof IMU inside SenseHat of Raspberry PI 4
![Example](/SenseHat/example1/imu_test_1_pitch.png)
<p align="center">Figure 5: Ground truth vs Estimated Pitch Angle [rad]</p>

![Example](/SenseHat/example1/imu_test_1_roll.png)
<p align="center">Figure 6: Ground truth vs Estimated Roll Angle [rad]</p>

# Test 3 - Pitch and Roll Fusion using 6-dof IMU inside SenseHat of Raspberry PI 4
![Example](/SenseHat/example1/imu_test_1_pitch.png)
<p align="center">Figure 7: Ground truth vs Estimated Pitch Angle [rad]</p>

![Example](/SenseHat/example1/imu_test_1_roll.png)
<p align="center">Figure 8: Ground truth vs Estimated Roll Angle [rad]</p>
