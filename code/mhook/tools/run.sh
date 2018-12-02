#!/bin/sh
set -x
set -e

function use_gdb {
    gdb --args ~/openSource/qt-5.4-debug-install/examples/opengl/cube/cube
}

function normal_test {
    export LD_PRELOAD=./out/lib/libmhook.so 
    #bin/trivial_leak
    #bin/trivial_leak_cpp
    #ls
    ~/openSource/qt-5.4-debug-install/examples/opengl/cube/cube
}

#use_gdb
normal_test
