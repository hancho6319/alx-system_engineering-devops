#This is the Puppet manifest to fix a bug in wp-setting.php

exec { 'fix the php extension issue below':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
	path => '/usr/location/bin/:/bin/'
}
