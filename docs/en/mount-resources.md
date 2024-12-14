# Mounting System Resources
## Mounting Files:
Ruri has powerful built-in mounting options. You can use `-m` to mount a file, and `-M` to mount it as read-only.     
### Directories:
For example, `-m /sdcard /sdcard` mounts the host machine’s /sdcard to the container’s /sdcard. However, this is not secure. The recommended approach is to use `-M /sdcard /sdcard` for read-only mounting.      
### Block Devices:
For example, you can use `-m /dev/sda /mnt` to mount /dev/sda to /mnt.      
### Image Files:
For example, you can use `-m ./1.img /mnt` to mount ./1.img to /mnt.      
### Root Directory:
Use `-m resource /` to pre-mount the root directory. For instance, `-m ./rootfs.img /` can mount ./rootfs.img as the container’s root directory.      
### Other Files:
Ruri also supports mounting individual files. For example, `-m /tmp/1.sock /tmp/1.sock` is theoretically possible.      
## Adding Character Devices:
Ruri supports adding character devices under /dev using `-I filename major_number minor_number`. For example, `-I kvm 10 232` or `-I dri/card0 226 0`.       