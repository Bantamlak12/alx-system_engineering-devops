# Setting the limit from 15 to 4096 in the file /etc/default/nginx

exec {'increase_the_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin',
} ->

# Restarting nginx
exec {'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/:/bin',
}
