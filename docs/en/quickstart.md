# Quickstart:
## Get ruri：
ruri provides binary for arm64, armv7, armhf, riscv64, i386, loong64, s390x, ppc64le and x86_64 platform，You can use the following command to download ruri as ./ruri:       
```sh
wget -q -O - https://getruri.crack.moe | bash -s -- -s
```
## Get a rootfs：
### Use rurima（Recommend）：
Get alpine edge image:     
```sh
wget -q -O - https://getrurima.crack.moe | bash -s -- -s
sudo ./rurima lxc pull -o alpine -v edge -s ./test 
```
BTW, rurima have a built-in ruri, so you can also use `rurima r` instead ruri.           
### Use rootfstool（Discarded）：
Get alpine edge image:      
```sh
git clone https://github.com/Moe-hacker/rootfstool
./rootfstool/rootfstool download -d alpine -v edge
mkdir test
sudo tar -xvf rootfs.tar.xz -C test
rm rootfs.tar.xz
```
### Set up dns：
```sh
sudo rm test/etc/resolv.conf
echo nameserver 1.1.1.1|sudo tee test/etc/resolv.conf
```
## Run container：
```sh
sudo ./ruri ./test
```
## That's all.