#!/bin/bash 
chown -R www-data /Sites/online_test
chown -R www-data /Sites/online_test/codegnan
chown -R nobody /Sites/online_test/codegnan_data
chmod -R 664 /Sites/online_test
chmod -R +X /Sites
/usr/sbin/apache2ctl -D FOREGROUND
