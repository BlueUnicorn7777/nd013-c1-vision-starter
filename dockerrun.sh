#docker run --gpus all -v ${PWD}:/app/project/ --network=host -ti -p 8888:8888 -p 6006:6006 project-dev bash

docker run --gpus all --device /dev/nvidia0:/dev/nvidia0 --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm -v ${PWD}:/app/project/ --network=host -ti -p 8888:8888 -p 6006:6006 project-dev bash
