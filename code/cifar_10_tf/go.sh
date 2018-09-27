TEMP_DIR=`pwd`/cifar-temp
if [[ -d $TEMP_DIR ]]; then
    rm -r $TEMP_DIR
fi
time python cifar_cnn.py
