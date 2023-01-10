# Create a file in /tmp with the following requirements:
# path is /tmp/school, permission is 0744, owner is www-data
# group is www-data and contains 'I love Puppet'

$file_name = '/tmp/school'

file { $file_name:
  # ensure => 'present',
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
