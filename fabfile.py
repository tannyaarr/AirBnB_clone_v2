from fabric import task
import os
import tarfile

@task
def upload_and_unpack(c):
    if c.run('test -f /opt/mydata/myfile', warn=True).failed:
        c.put('myfiles.tgz', '/opt/mydata')
    c.run('tar -C /opt/mydata -xzvf /opt/mydata/myfiles.tgz')

@task
def do_pack(c):
    # Specify the source directory to be packed
    source_dir = "my_project/static_files"

    # Define the output archive filename
    archive_name = "my_project_archive.tar.gz"

    # Create the tarball
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    # Move the archive to a specific location (e.g., a backup directory)
    c.run(f"mv {archive_name} /path/to/backups/")

    print(f"Archive created: {archive_name}")

# Usage: fab -f my_fabfile.py do_pack
