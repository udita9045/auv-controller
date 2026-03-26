from navigation import distance, heading
from pid import PID
import time

print("AUV Controller Started")

depth_pid = PID(1.5, 0.05, 0.3)
yaw_pid = PID(2.0, 0, 0.5)

depth = 0
heading = 0

target_depth = 5
target_heading = 90

dt = 0.1

while True:
    depth_control = depth_pid.compute(target_depth, depth, dt)
    yaw_control = yaw_pid.compute(target_heading, heading, dt)

    print(f"Depth control: {depth_control}, Yaw control: {yaw_control}")

    depth += depth_control * dt
    heading += yaw_control * dt

    time.sleep(dt)
