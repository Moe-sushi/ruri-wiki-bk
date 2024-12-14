# 挂载系统资源
## 挂载文件：
ruri内置强大的挂载参数，您可以使用`-m`来挂载文件，`-M`来只读挂载。       
### 目录：
例如，`-m /sdcard /sdcard`来挂载宿主机/sdcard到容器的/sdcard，当然这并不安全，推荐的方式是通过`-M /sdcard /sdcard`来实现只读挂载。      
### 块设备：
例如，您可以使用`-m /dev/sda /mnt`挂载/dev/sda到/mnt。     
### 镜像文件：
例如，您可以使用`-m ./1.img /mnt`挂载./1.img到/mnt。      
### 根目录：
使用`-m 资源 /`来预先挂载根目录，例如，`-m ./rootfs.img /`可以将./rootfs.img挂载为容器根目录。       
### 其他文件：
ruri支持单个文件挂载，如`-m /tmp/1.sock /tmp/1.sock`理论上也是可行的。      
## 添加字符设备：
ruri支持使用`-I 文件名 主设备号 次设备号`来在/dev下添加字符设备，例如`-I kvm 10 232`或`-I dri/card0 226 0`。      