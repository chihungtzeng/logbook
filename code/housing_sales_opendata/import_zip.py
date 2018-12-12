# -*- coding: utf-8 -*-
import os
import logging
import argparse
import tempfile
import subprocess
from base_xml_parser import BaseXMLParser


def __import_zip(zip_file, temp_dir_root="/mnt/ramdisk"):
    if not os.path.isdir(temp_dir_root):
        temp_dir_root = "/tmp"
    temp_dir = tempfile.mkdtemp(dir=temp_dir_root)
    cmd = ["unzip", zip_file]
    logging.info("unzip %s in %s", zip_file, temp_dir)
    subprocess.call(cmd, cwd=temp_dir)

    for root, _dirs, files in os.walk(temp_dir):
        for fname in files:
            if not fname.endswith("_a.xml"):
                continue
            fullpath = os.path.join(root, fname)
            logging.info("Handle %s", fullpath)
            xmlparser = BaseXMLParser(fullpath)
            xmlparser.parse()

    cmd = ["rm", "-r", temp_dir]
    subprocess.call(cmd)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip-file", "-f", required=True)
    args = parser.parse_args()
    __import_zip(args.zip_file)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
