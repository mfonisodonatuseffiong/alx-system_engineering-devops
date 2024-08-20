# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard nofile/s/8192/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft nofile/s/500000000096/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}
