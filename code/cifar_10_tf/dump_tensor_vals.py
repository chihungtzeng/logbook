from tensorflow.python.tools import inspect_checkpoint as chkp
import numpy


def main():
    chkp.parse_numpy_printoption("threshold=1000000000")
    chkp.print_tensors_in_checkpoint_file(
        "model_export/model.ckpt-80",
        tensor_name="", all_tensors=True)

if __name__ == "__main__":
    main()
