#This manifest execute pkill command.
exec{'killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  onlyif  => 'pgrep killmenow',
}
