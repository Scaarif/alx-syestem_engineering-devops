# Using strace(yet another powerful debugging tool) to debug a webstack (apache returning status code 500)
exec { 'fix_apache_error':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin':'/usr/sbin':'/bin'
}
