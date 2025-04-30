# ros2-unity-docker-setup
- - -
### First time setup
1) Install Docker Desktop (https://docs.docker.com/desktop/setup/install/windows-install/).
2) Make sure to run the Docker Desktop app before proceeding.
3) Create a folder to use as workspace and open a terminal there.
4) Clone the git repo into your folder of choice by doing ``` git clone https://github.com/xacobeu/ros2-unity-docker-setup.git ```.
5) Type ``` cd ros2-unity-docker-setup  ```
6) Then type ``` build.bat ```.
7) Once its done type ``` run.bat ```.
8) You can open more terminal windows by running ``` open_terminal.bat ```.
- - -
### Running with Unity
1) Open Docker Desktop.
2) Navigate to your folder and open a terminal.
3) Type ``` run.bat ```.
4) Once the container is open, type ``` ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0 ```
5) Open the unity project
6) Find the tab Robotics/ROS Settings in the top bar, and set these settings:

![image](https://github.com/user-attachments/assets/f02d3336-ed7d-41b1-b3f1-46587f9761e6)

7) Find turtlebot3_burger in the Hierarchy tab, click it, and in the Inspector tab ensure the AGV Controller mode is set to ROS:

![image](https://github.com/user-attachments/assets/ac342813-d6f1-4945-864a-00e96b9a1709)

8) Run the Unity project by clicking the 'play' button at the top:

![image](https://github.com/user-attachments/assets/83aae174-3048-441d-a5e8-526b0a62bf2b)

9) Open a second terminal in your folder and type ``` open_terminal.bat ```.
10) Once the new terminal is open, run ``` ros2 run turtlebot3_teleop teleop_keyboard ```.
11) You can now use the following keybinds to move the robot around in unity:

```
W - Move Forward (Increases forward velocity).

A - Turn Left (Decrease angular velocity to rotate left).

D - Turn Right (Increase angular velocity to rotate right).

X - Move Backward (Increase backward velocity).

S - Stop Movement (Zeroes out all velocity, stopping motion).
```
