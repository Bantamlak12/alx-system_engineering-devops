#!/usr/bin/env bash
# Set up a client SSH configuration file using puppet to connect to
# a server without typing a password.

# the `path` attribute in the following code looks for the path of the `echo` command.

exec { 'echo "IdentifyFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config':  path => '/bin/'
}
