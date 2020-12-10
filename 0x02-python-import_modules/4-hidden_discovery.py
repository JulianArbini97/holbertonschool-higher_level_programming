#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for string in range(len(dir(hidden_4))):
        if (dir(hidden_4)[string][:2]) != "__":
            print('{:s}'.format(dir(hidden_4)[string]))
