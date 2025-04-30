# ros2-unity-docker-setup
- - -
### First time setup
- Install Docker Desktop (https://docs.docker.com/desktop/setup/install/windows-install/).
- Make sure to run the Docker Desktop app before proceeding.
- Create a folder to use as workspace and open a terminal there.
- Clone the git repo into your folder of choice by doing ``` git clone https://github.com/xacobeu/ros2-unity-docker-setup.git ```.
- Then type ``` build.bat ```.
- Once its done type ``` run.bat ```.
- You can open more terminal windows by running ``` open_terminal.bat ```.
- - -
### Running with Unity
- Open Docker Desktop.
- Navigate to your folder and open a terminal.
- Type ``` run.bat ```.
- Once the container is open, type ``` ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0 ```
- Open the unity project
- Find the tab Robotics/ROS Settings in the top bar, and set these settings:

![image](https://github.com/user-attachments/assets/f02d3336-ed7d-41b1-b3f1-46587f9761e6)

- Run the Unity project by clicking the 'play' button at the top:

![image](https://github.com/user-attachments/assets/83aae174-3048-441d-a5e8-526b0a62bf2b)

- Open a second terminal in your folder and type ``` open_terminal.bat ```.
- Once the new terminal is open, run ``` ros2 run turtlebot3_teleop teleop_keyboard ```.
- You can now use the following keybinds to move around in unity:
W - Move Forward (Increases forward velocity).
A - Turn Left (Decrease angular velocity to rotate left).
D - Turn Right (Increase angular velocity to rotate right).
X - Move Backward (Increase backward velocity).

S - Stop Movement (Zeroes out all velocity, stopping motion).
