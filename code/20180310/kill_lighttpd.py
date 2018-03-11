#!/usr/bin/python
import subprocess
import os
import signal

def _get_lighttpd_pid():
    output = subprocess.check_output(["ps", "ax"])
    pid = None
    for line in output.splitlines():
        if "lighttpd-phabricator.conf" in str(line):
            pid = int(line.split()[0])
    return pid


if __name__ == "__main__":
    pid = _get_lighttpd_pid()
    print("Kill lighttpd pid: {}".format(pid))
    if pid is not None:
        os.kill(pid, signal.SIGKILL)
