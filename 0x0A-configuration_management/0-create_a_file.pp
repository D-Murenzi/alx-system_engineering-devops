#manifest to create school file.
file {'/tmp/school':
  ensure         => 'file',
  path           => '/tmp/school',
  mode           => '0744',
  owner          => 'www-data',
  group          => 'www-data',
  content        => 'I love Puppet',
  checksum_value => 'md5',
}