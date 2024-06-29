# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3 with increased timeout
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  install_options => ['--timeout=120'],
  require  => Package['python3-pip'],  # Ensure pip3 is installed before Flask
}
