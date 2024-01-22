#!/bin/bash
chown -R nobody /Sites/online_test/codegnan_data
chmod -R a+rwX codegnan_data/output
chmod -R a+rX codegnan_data/data
chmod -R o-w codegnan_data/data
/usr/bin/sudo -su nobody python3 -m codegnan.code_server
