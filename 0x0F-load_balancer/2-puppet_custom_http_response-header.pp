exec { 'update':
  command  => '/usr/bin/apt-get update',
  provider => shell,
}

-> package { 'nginx':
  ensure => present,
}

-> file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By \$hostname;",
  match  => '^\tlocation / {',
  after  => '^\tlocation / {',
}

-> exec { 'restart service':
  command  => '/usr/sbin/service nginx restart',
  provider => shell,
}
