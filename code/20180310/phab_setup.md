Overview

Webserver: Gentoo + lighttpd + php + mysql
lighttpd runs on port 8081
Top dir for the whole phabricator -- /home/phabricator/
# Requrements:
USE="pcntl"  # for phd daemon

Install phabricator (run commands as root)

mkdir -p /home/phabricator/htdocs
cd /home/phabricator/htdocs

git clone https://github.com/phacility/libphutil.git
git clone https://github.com/phacility/arcanist.git
git clone https://github.com/phacility/phabricator.git

mkdir -p /home/phabricator/log
mkdir -p /home/phabricator/run
mkdir -p /home/phabricator/lighttpd-state
chown -R lighttpd:lighttpd /home/phabricator/log

/usr/sbin/lighttpd -f /home/phabricator/lighttpd-phabricator.conf

cd /home/phabricator/htdocs/phabricator
./bin/config set phabricator.base-uri 'http://172.104.75.62:8081/'

# setup mysql
./bin/config set mysql.host localhost
./bin/config set mysql.user root
./bin/config set mysql.pass rootspassword

# set php.ini, in case running into the following problem:
# Raw MySQL Error: Attempt to connect to root@localhost failed with error
#2002: No such file or directory.
vi /etc/php/cli-php7.1/php.ini and /etc/php/cgi-php7.1/php.ini
  mysqli.default_socket = /var/run/mysqld/mysqld.sock

# Generate mysql db
./bin/storage upgrade

# setup in webpage
Open browser to navigate http://172.104.75.62:8081
It will finish the setup.

# Post-installation:
# Setup storage for repos
cd /home/phabricator/htdocs/phabricator
./bin/config set repository.default-local-path /home/phabricator/repos
chown -R lighttpd:lighttpd /home/phabricator/repos

