# installing a package using puppet
package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem',
}