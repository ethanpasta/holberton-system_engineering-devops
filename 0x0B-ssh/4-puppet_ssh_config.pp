# Manifest adds 2 lines to ssh configuration file
file_line { 'no_password':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    PubkeyAuthentication no',
}

file_line { 'identity_file':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/holberton',
}
