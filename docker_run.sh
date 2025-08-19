# USAGE: docker_run.sh <image_name> <container_name>
# docker exec -it <container_name> bash
mount_dirs="-v /data/models:/models -v ${HOME}/projects/:/projects -v /mnt/:/mnt/"

image_name=$1
container_name=$2

docker pull ${image_name}

cmd="docker run --name ${container_name} -it -d  --network=host --device /dev/kfd --device /dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined ${mount_dirs} --shm-size=64G --ulimit core=0 --ulimit memlock=-1 --ulimit stack=67108864 -e VLLM_DISABLE_COMPILE_CACHE=1 ${image_name}"
echo ${cmd}
${cmd}
