# IMUFusion
 Different IMU fusion algorithms will be implemented and tested.
 
 First algorithm uses 6-dof IMU. Roll and pitch angles are coupled w.r.t yaw rate.

 Hardware:
 https://www.raspberrypi.org/products/raspberry-pi-4-model-b/ (4GB ram)
 https://www.raspberrypi.org/products/sense-hat/
 
 Coding language:
 Python
 
 The tests are validated against the ground truth data collected from internal 9-dof IMU fusion of SenseHat.

# Test 1 - Pitch and Roll Fusion using 6-dof IMU inside SenseHat of Raspberry PI 4
![Example](/SenseHat/imu_test_1_pitch.png)
<p align="center">Figure 1: Ground truth vs Estimated Pitch Angle [rad]</p>

![Example](/SenseHat/imu_test_1_roll.png)
<p align="center">Figure 2: Ground truth vs Estimated Roll Angle [rad]</p>

# Test 2 - Pitch and Roll Fusion using 6-dof IMU inside SenseHat of Raspberry PI 4
![Example](/SenseHat/imu_test_1_pitch.png)
<p align="center">Figure 3: Ground truth vs Estimated Pitch Angle [rad]</p>

![Example](/SenseHat/imu_test_1_roll.png)
<p align="center">Figure 4: Ground truth vs Estimated Roll Angle [rad]</p>
