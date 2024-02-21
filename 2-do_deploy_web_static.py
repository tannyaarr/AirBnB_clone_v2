#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run, sudo 
from datetime import datetime
fom poxipath import basename

env.hosts = ["100.25.179.193", "54.174.161.74"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the folder /data/web_static/releases/<archive_filename_without_extension>
        archive_filename = basename(archive_path)
        release_folder = f"/data/web_static/releases/{archive_filename.split('.')[0]}"

        sudo(f"mkdir -p {release_folder}")
        sudo(f"tar -xzf /tmp/{archive_filename} -C {release_folder}")

        # Remove the uploaded archive
        run(f"rm /tmp/{archive_filename}")

        # Delete the symbolic link /data/web_static/current
        sudo("rm -f /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        sudo(f"ln -s {release_folder} /data/web_static/current")

        print("New version deployed successfully!")

        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return Falsedef do_deploy(archive_path):
