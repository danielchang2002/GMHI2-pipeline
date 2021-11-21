from . import utils
import os
import subprocess
from urllib.request import urlopen
from zipfile import ZipFile


def install_GRCh38_noalt_as():
    print("Installing GRCh38_noalt_as")

    url = "https://genome-idx.s3.amazonaws.com/bt/GRCh38_noalt_as.zip"
    target_dir = os.path.join(utils.DEFAULT_DB_FOLDER)
    proc = subprocess.call(["wget", "-P", target_dir, url], stdout=subprocess.PIPE)
    zip_location = os.path.join(target_dir, "GRCh38_noalt_as.zip")
    proc = subprocess.call(
        ["unzip", zip_location, "-d", os.path.join(target_dir)],
    )
