@echo off
echo Building Docker image 'foxy'...
docker build -t foxy -f ros2_docker/Dockerfile .
echo Done!