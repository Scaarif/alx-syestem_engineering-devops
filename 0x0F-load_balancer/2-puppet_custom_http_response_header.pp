# Automate the creating of a custom HTTP header response by an nginx server

# update packages
exec {'update':
  command => 'sudo apt-get -y update',
  before  => Exec['install Nginx'],
}

# install nginx
exec {'install nginx':
  command => 'sudo apt-get -y install nginx',
  before  => Exec['add_header'],
}

# add custom header in configuration
exec { 'add_header':
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

# restart nginx once done with configuration
exec { 'restart Nginx':
  command  => 'sudo service nginx restart',
}
