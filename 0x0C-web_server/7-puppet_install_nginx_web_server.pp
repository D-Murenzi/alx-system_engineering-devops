#This manifests installs and configures nginx on server.

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  }

file { '/etc/nginx/conf.d/hbnb_stat.conf':
ensure   => file,
content  => "server {
     listen 80;
     server_name dmurenzi.tech;

     location / {
     	      return 200 'Hello World!';
	      }
     location /redirect_me {
     	      return 301 'https://www.youtube.com/watch?v=qh2-TGUlwu4';
	      }
}\n",
  owner  => 'root',
  group  => 'root',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,   # Ensure Nginx starts on boot
  hasrestart => true,
  hasstatus  => true,
  require    => Package['nginx'],
  }
