# The file "wp-settings.php" in /var/www/html has a mistyped extension (phpp)

exec { 'wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin'
}
