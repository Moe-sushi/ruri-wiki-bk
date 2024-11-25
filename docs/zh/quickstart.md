# 快速开始
## 下载ruri：
ruri为arm64, armv7, armhf, riscv64, i386, loong64, s390x, ppc64le和x86_64平台提供官方二进制，使用以下命令自动下载二进制为./ruri:       
```sh
wget -q -O - https://getruri.crack.moe | bash -s -- -s
```
## 获取一个rootfs：
### 使用rurima（推荐）：
获取alpine edge镜像:     
```sh
wget -q -O - https://getrurima.crack.moe | bash -s -- -s
sudo ./rurima lxc pull -o alpine -v edge -s ./test 
```
BTW, rurima已经完整内置了ruri，所以事实上大家只需要一个rurima然后`rurima r`就能调用ruri。      
~~所以我们还下载ruri干什么呢~~      
### 使用rootfstool（已废弃）：
获取alpine edge镜像:      
```sh
git clone https://github.com/Moe-hacker/rootfstool
./rootfstool/rootfstool download -d alpine -v edge
mkdir test
sudo tar -xvf rootfs.tar.xz -C test
rm rootfs.tar.xz
```
### 配置dns：
```sh
sudo rm test/etc/resolv.conf
echo nameserver 1.1.1.1|sudo tee test/etc/resolv.conf
```
## 运行容器：
```sh
sudo ./ruri ./test
```
## 完结撒花～