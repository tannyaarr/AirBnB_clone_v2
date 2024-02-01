#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run
from datetime import datetime

env.hosts = ["100.25.179.193", "54.174.161.74"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(file_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, file_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(file_no_ext, file_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(file_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_no_ext))
        return True
    except:
        return False
