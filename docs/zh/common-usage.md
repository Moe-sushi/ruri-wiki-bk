# 日常使用
## 关于权限：
ruri的大部分功能依赖root权限（sudo），除rootless部分外。    
## 安全停止容器：
您可以使用`-U [容器目录/配置文件]`来安全的卸载容器并（尽可能）杀死容器进程。       
## 开启unshare：
您可以使用`-u`选项来开启unshare功能，这通常不会影响容器运行并将提供更高安全性。      
## capability控制：
ruri内置了capability控制功能，您可以通过`-k capability`来保留某个cpability，使用`-d capability`来移除。注意capability应该全部小写。       
## 挂载宿主机目录：
你可以通过像`-m /sdcard /sdcard`的方式来挂载宿主机目录进容器。      
## 网络问题：
您可能会遇到像`temporary failure resolving xxxxx`或`bad address xxxxx`的错误。    
可以尝试在容器中运行：      
```sh
rm /etc/resolv.conf
echo nameserver 1.1.1.1 > /etc/resolv.conf
```
或者对于Android，您可尝试在容器中运行 https://github.com/Moe-hacker/daijin/raw/refs/heads/main/src/share/fixup.sh      
# 关于rootless容器：
如果在容器中遇到 `Couldn't create temporary file /tmp/apt.conf.sIKx3J for passing config to apt-key` 这样的错误，请 `chmod 777 /tmp`。   
您需要在宿主机上安装 uidmap。   
您可能需要在宿主机上配置/etc/subuid和/etc/subgid。       