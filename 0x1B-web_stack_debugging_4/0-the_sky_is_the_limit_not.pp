# Setting the limit from 15 to 4096 in the file /etc/default/nginx

exec {'Substitute root path':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/bin',
} ->

exec {'nginx restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin',
}
