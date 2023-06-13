# Too many open files on the system, so editing the limit in /etc/security/limits.conf

$hard_limit = '8192'
$soft_limit = '4096'

exec {'Limit':
  command => "sed -i 's/\\(holberton hard nofile \\)[0-9]*/\\1${hard_limit}/' /etc/security/limits.conf &&
              sed -i 's/\\(holberton soft nofile \\)[0-9]*/\\1${soft_limit}/' /etc/security/limits.conf",
  path    => '/bin',
}
