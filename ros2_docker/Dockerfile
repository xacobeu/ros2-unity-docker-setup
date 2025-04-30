FROM ros:foxy-ros-base

# Install required packages and tools
RUN apt update && apt install -y \
    git \
    python3-colcon-common-extensions \
    ros-foxy-dynamixel-sdk \
    ros-foxy-turtlebot3-msgs \
    ros-foxy-turtlebot3 \
    && rm -rf /var/lib/apt/lists/*

# Make ROS2 Workspace Dir
RUN mkdir -p /home/dev_ws/src

# Copy custom ROS2 packages into workspace
COPY ./ros2_packages/ /home/dev_ws/src

# Clone Unity ROS-TCP-Endpoint (ROS2 branch)
RUN git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint /home/dev_ws/src/ros_tcp_endpoint -b ROS2v0.7.0

# Set TurtleBot3 model (you can override this at runtime)
ENV TURTLEBOT3_MODEL=burger

# Reference script with commands to source workspace
COPY ./ros2_docker/source_ros.sh /home/dev_ws/source_ros.sh

# Fix: correct missing leading slash in "cd" and update bashrc
RUN echo "cd /home/dev_ws" >> /root/.bashrc \
    && echo ". install/local_setup.bash" >> /root/.bashrc

# Build the workspace
RUN /bin/bash -c "source /opt/ros/foxy/setup.bash && cd /home/dev_ws && colcon build"

RUN /bin/bash -c "source /home/dev_ws/install/setup.bash && colcon build && /home/dev_ws/source install/setup.bash"