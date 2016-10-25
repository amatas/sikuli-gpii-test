# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "inclusivedesign/windows10-eval"

  config.vm.guest = :windows
  config.vm.provider "virtualbox" do |vb|
     vb.linked_clone = true
     vb.gui = true
     vb.memory = "2048"
     vb.cpus = "2"
     vb.customize ["modifyvm", :id , "--accelerate3d", "on" ]
     vb.customize ["modifyvm", :id , "--accelerate2dvideo", "on"]
     vb.customize ["modifyvm", :id , "--vram" , "85"]
     vb.customize ["modifyvm", :id , "--clipboard" , "bidirectional"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    copy c:\\vagrant\\tests\\GPII-installer.msi C:\\Users\\vagrant\\Desktop\\
    cd c:\\vagrant\\tests
    md c:\\Screenshots
    java -jar sikulixsetup-1.1.0.jar options 1.1 2 3
  SHELL

end
