# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # 虚拟机名字<boxName>
  config.vm.box = "u14evm"

  # 指定私钥文件路径
  config.ssh.private_key_path = 'id_rsa'
  
  # 桥接网络
  config.vm.network "public_network"

  # 映射文件夹
  config.vm.synced_folder ".", "/var/www/u-bbs"

  # shell脚本
  config.vm.provision "shell", inline: <<-SHELL
    # 切换为root用户运行
    sudo su
    # bash -ex /var/www/u-bbs/setup.sh
    bash -ex /var/www/u-bbs/restart.sh
  SHELL
end
