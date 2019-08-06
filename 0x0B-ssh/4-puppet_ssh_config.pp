# Manifest adds 2 lines to ssh configuration file
include stdlib

file_line { 'no_password':
  path   => '/etc/ssh/ssh_config',
  line   => '    PubkeyAuthentication no',
}

file_line { 'identity_file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}
