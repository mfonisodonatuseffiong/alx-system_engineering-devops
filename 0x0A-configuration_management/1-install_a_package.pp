# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 and compatible Werkzeug version using pip3
exec { 'install_flask_and_werkzeug':
  command => '/usr/local/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  path    => ['/usr/bin', '/usr/local/bin'],
  require => Package['python3-pip'],
}
