emerge buildbot buildbot-slave


virtualenv venv-buildbot
source venv-buildbot/bin/activate

Install buildbot
----------------
For version >= 1.0
```
pip install buildbot
pip install buildbot-worker
```

For version < 1.0
```
pip install buildbot
pip install buildbot-slave
```

Setup master
------------
# Create working environment for buildbot
buildbot create-master -r buildbot-workspace
```
mkdir /home/clark/buildbot-workspace
creating /home/clark/buildbot-workspace/master.cfg.sample
populating public_html/
populating templates/
creating database (sqlite:///state.sqlite)
buildmaster configured in /home/clark/buildbot-workspace
```
cd buildbot-workspace
cp master.cfg.sample master.cfg
vi master.cfg

Setup slave
-----------

# buildbot 0.9.x uses worker. Adapt it to our need.
# buildbot-worker create-worker BASEDIR MASTERHOST:PORT WORKERNAME PASSWORD
buildslave create-slave vparser-slave-workspace localhost:9989 vparser-slave vparser-password
```
mkdir /home/clark/vparser-slave-workspace
mkdir /home/clark/vparser-slave-workspace/info
Creating info/admin, you need to edit it appropriately.
Creating info/host, you need to edit it appropriately.
Not creating info/access_uri - add it if you wish
Please edit the files in /home/clark/vparser-slave-workspace/info appropriately.
buildslave configured in /home/clark/vparser-slave-workspace
```
vi vparser-slave-workspace/info/admin
vi vparser-slave-workspace/info/host
The above modification identifies slaves only. The main configuration is in master.


Start master
------------
cd /home/clark
buildbot start buildbot-workspace

Start slaves
------------
buildslave start vparser-slave-workspace
