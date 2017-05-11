echo "[gocd]
name     = GoCD YUM Repository
baseurl  = https://download.gocd.io
enabled  = 1
gpgcheck = 1
gpgkey   = https://download.gocd.io/GOCD-GPG-KEY.asc
" | sudo tee /etc/yum.repos.d/gocd.repo

sudo yum install -y java-1.8.0-openjdk
sudo yum install -y go-server
