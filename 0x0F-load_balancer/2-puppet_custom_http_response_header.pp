# Automate the task of creating a :wq
# custom HTTP header response

# update packages
exec { 'update':
  command => 'sudo apt-get -y update',
  before  => Exec['install Nginx'],
}

# install nginx
exec { 'install nginx':
  command => 'sudo apt-get -y install nginx',
  before  => Exec['add_header'],
}

# add the custom header
exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i \'49i\\tadd_header X-Served-By "$HOST";\' /etc/nginx/sites-available/default',
  before      => Exec ['restart Nginx'],
}

# restart nginx
exec {'restart nginx':
  command => 'sudo service nginx restart',
}
