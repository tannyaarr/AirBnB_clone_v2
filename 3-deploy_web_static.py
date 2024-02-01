#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to web servers using the function deploy
"""
from fabric.api import env, local
from os.path import isfile
from datetime import datetime

env.hosts = ['100.25.179.193', '54.174.161.74']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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
    if not isfile(archive_path):
        return False

    try:
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
