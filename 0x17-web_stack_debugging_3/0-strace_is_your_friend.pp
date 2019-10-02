# puppet fixes apache2 server
exec { 'Replace line in wp-settings.php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/usr/bin', '/usr/sbin',],
}
