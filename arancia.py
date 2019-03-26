#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) < 2:
        print("Argument not valid")
        sys.exit(1)

    code = sys.argv[1]

    if code[:3] == "KVR":
        brand = "Kingston"
        if code[:6] == "400" or code[:6] == "333" or code[:6] == "266":
            frequency = int(code[:6])*10**6
        else:
            print("Code not valid")
            sys.exit(1)


if __name__ == '__main__':
    main()
