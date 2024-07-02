# 7-puppet_install_nginx_web_server.pp
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'allow nginx through firewall':
  command => '/usr/sbin/ufw allow \'Nginx HTTP\'',
  unless  => '/usr/sbin/ufw status | grep -q "Nginx HTTP"',
  require => Package['nginx'],
}
