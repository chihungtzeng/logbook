TEMP_DIR=`pwd`/model_export
if [[ -d $TEMP_DIR ]]; then
    rm -r $TEMP_DIR
fi
time python cifar_cnn.py
