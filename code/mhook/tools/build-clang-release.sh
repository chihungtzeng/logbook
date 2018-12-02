#!/bin/sh
set -e
set -x

#TOP=`basename $0`/..
TOP=`readlink -m $0/../..`
BUILD_DIR=out
export CC=clang
export CXX=clang++
if [ -d $BUILD_DIR ]; then
    rm -rf $BUILD_DIR
fi
mkdir -p $BUILD_DIR
cd $BUILD_DIR
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_USER_MAKE_RULES_OVERRIDE=${TOP}/ClangOverrides.txt -D_CMAKE_TOOLCHAIN_PREFIX=llvm- $TOP
make -j `nproc`
