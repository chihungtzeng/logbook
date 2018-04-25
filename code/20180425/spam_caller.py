#! -*- coding: utf-8 -*-
import spam

def main():
    ret = spam.system("ls -l")
    print(ret)

if __name__ == "__main__":
    main()
