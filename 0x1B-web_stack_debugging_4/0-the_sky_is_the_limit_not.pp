# manifest changes worker-processes in nginx config file
exec { 'Change worker-processes in nginx.config':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart;",
  path    => ['/usr/bin', '/usr/sbin', '/bin',],
}
