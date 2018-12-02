#!/bin/sh
set -e
set -x

#TOP=`basename $0`/..
TOP=`readlink -m $0/../..`
BUILD_DIR=out
if [ -d $BUILD_DIR ]; then
    rm -rf $BUILD_DIR
fi
mkdir -p $BUILD_DIR
cd $BUILD_DIR
cmake -DCMAKE_BUILD_TYPE=Debug $TOP
make -j `nproc`
