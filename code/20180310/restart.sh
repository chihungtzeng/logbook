#!/bin/bash
set -x
readonly top=$(readlink -e $(dirname $0))
readonly config_file=${top}/lighttpd-phabricator.conf

python kill_lighttpd.py
/usr/sbin/lighttpd -f ${config_file}

