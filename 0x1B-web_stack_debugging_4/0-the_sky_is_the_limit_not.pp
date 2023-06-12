# Substituting `root /usr/share/nginx/html;` with `root /var/www/html;`

exec {'Substitute root path':
  command => "sed -i 's#root /usr/share/nginx/html;#root /var/www/html;#' /etc/nginx/sites-available/default" ,
  path    => '/bin',
}

exec {'nginx restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin',
}
