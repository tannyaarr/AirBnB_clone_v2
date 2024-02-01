#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path import exists
from fabric.api import env
from fabric.api import put
from fabric.api import run
from datetime import datetime

env.hosts = ["100.25.179.193", "54.174.161.74"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Create a tar gzipped archive of the web_static directory
    """
    dt = datetime.utcnow()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(file_name))
    if result.failed:
        return None
    return "versions/{}".format(file_name)

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, folder_name))

        run("rm /tmp/{}".format(file_name))

        run("rm -f /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False

