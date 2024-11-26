# Common Usage
## About pervileges：
Most function of ruri needs to be run with root (sudo), except rootless part.           
## Stop container：
You can use `-U [CONTAINER_DIR/config]`to umount a container and try to kill all processes in it.             
## Enable unshare：
You can use `-u` option to enable unshare, this will not break container in most of the time and it will provide better security.           
## capability control：
ruri have built-in capability control function，you can use`-k capability` to keep a cpability，use `-d capability` to drop. Note that capability should be lower-case.          
## mount dir from host：
You can use `-m /sdcard /sdcard` to mount /sdcard into container.            
## Network problem：
You might found error like `temporary failure resolving xxxxx` or `bad address xxxxx`.    
Try to run the following command in container：      
```sh
rm /etc/resolv.conf
echo nameserver 1.1.1.1 > /etc/resolv.conf
```
Or for android, try running https://github.com/Moe-hacker/daijin/raw/refs/heads/main/src/share/fixup.sh in container.           
# About rootless container：
If you have error like `Couldn't create temporary file /tmp/apt.conf.sIKx3J for passing config to apt-key` please `chmod 777 /tmp`。   
Please install uidmap before you use rootless container.         
You might need to configure /etc/subuid and /etc/subgid。       