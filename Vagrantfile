  Vagrant.configure("2") do |config|
    config.vm.box = "centos-6.7"
    config.vm.network "forwarded_port", guest: 22, host: 2200
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.synced_folder ".", "/opt/data", type: "nfs"

    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "2048"
    end

    config.vm.provision "shell", path: "./install.sh"
  end
