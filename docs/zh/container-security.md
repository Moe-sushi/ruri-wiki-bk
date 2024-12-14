# 如何增强容器安全：
ruri提供一系列安全选项，下面是它们的使用说明：      
## 日常：
### 使用rootless容器：
在现代的GNU/Linux上，一般只要配置好/etc/subuid和/etc/subgid，安装uidmap（shadow）包，即可使用rootless容器。      
如果你的设备支持，可以使用`-r`选项来以普通用户运行无特权容器。      
### 使用普通用户：
如果你的设备不支持，你还有一个选项，在容器中创建一个普通用户，并使用`-E username`选项来使用普通用户在容器中运行命令。请确保username在容器的/etc/passwd中有正确记录。      
如果你不需要使用sudo，可以同时开启no_new_privs（`-n`）选项。      
### 开启unshare：
ruri支持除网络外的常用命名空间（网络命名空间仅用于禁用网络），你可以使用`-u`选项尝试开启支持的命名空间。      
unshare功能至少依赖mount ns，并会默认使用pivot_root(2)来替代chroot(2)来提供更高的安全性。      
### Capabilities（权限集合）：
ruri支持Linux的capability控制，你可以使用`-d cap/num`来移除一个capability，`-k`来保留。      
ruri默认已经移除了大部分可能危害宿主机的capability，但如果你有其他不需要的特权，也可以选择移除。      
### 关闭.rurienv支持：
ruri默认会在容器中创建`/.rurienv`来统一容器配置，这份配置文件通过设置只读属性（immutable）和移除容器修改此属性的特权（CAP_LINUX_IMMUTABLE）来保证安全，如果你觉得还不够安全，可以使用`-N`选项禁用此文件。     
### 设置内存/cpu限制:
ruri支持cgroup的memory/cpu/cpuset控制组，你可以使用`-l`选项来设置这些限制。      
### 挂载外部挂载点为只读:
ruri支持挂载外部挂载点为只读，如果你只需要访问文件而不需要修改，请使用`-M`选项来代替`-m`选项。      
### 开启seccomp：
ruri内置了一份黑名单模式seccomp配置，你可以使用`-s`选项来开启它。      
## 极客:
### 自己编写Seccomp配置：
ruri内置的seccomp配置足以应对大多威胁，但如果你需要更激进的策略，可以手动编辑src/seccomp.c来写入自己的配置文件。      
## 激进：
### Hidepid:
ruri支持为/proc设置hidepid选项，使用`-i 1/2` 来开启。     
### 开启no_new_privs:
您可以使用`-n`选项来开启NO_NEW_PRIVS,开启后sudo等程序将无法运行。      
### 挂载根目录为只读：
您可以使用`-R`选项来使整个容器根目录只读。开启后，/sys和/proc也将为完全只读。     
### 禁用网络：
您可以使用`-x`选项来完全禁用容器网络，这需要NET命名空间，并会自动开启unshare。      
## 默认安全保护：
ruri默认还提供如下安全防护：      

- /dev下只创建必须文件      
- /sys和/proc下部分敏感目录/文件为只读，部分被直接屏蔽      
- 移除大部分可能导致危害宿主机的特权      