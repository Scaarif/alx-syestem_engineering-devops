# Kills a process named 'killmenow'
# uses the exec resources and the pkill command

exec {'pkill killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
