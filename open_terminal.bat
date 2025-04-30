@echo off
set CONTAINER_NAME=foxy_unity

REM Open a new terminal and exec into the container while sourcing ROS 2 setup
docker exec -it %CONTAINER_NAME% bash -c "source /opt/ros/foxy/setup.bash && exec bash"
