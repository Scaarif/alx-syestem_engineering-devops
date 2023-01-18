# Automate the creating of a custom HTTP header response by an nginx server

# update packages
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx'],
}

# install nginx
exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

# add custom header in configuration
exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart nginx'],
}

# restart nginx once done with configuration
exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
