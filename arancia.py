#!/usr/bin/env python3
import sys
from tabulate import tabulate
import re


def main():
    if len(sys.argv) < 2:
        print("Argument not valid")
        sys.exit(1)

    code = sys.argv[1]

    data = {
        'brand': None,
        'model': None,
        'family': None,
        'notes': None,
        'ram-type': None,
        'ram-form-factor': None,
        'ram-ecc': None,
        'cas-latency': None,  # Not in tarallo
        'number-in-kit': None,  # Not in tarallo
        'low-profile': None,  # Not in tarallo
        'frequency-hertz': None
    }

    if code[:3] == "KVR":
        data['brand'] = "Kingston"
        data['model'] = code
        data['familiy'] = "ValueRAM"
        if code[3:6] == "400" or code[3:6] == "333" or "266" == code[3:6]:
            data['frequency-hertz'] = int(code[3:6]) * 10 ** 6
        else:
            print("Code not valid")
            sys.exit(1)

    print(tabulate(data.items(), headers=["Feature", "Value"]))


if __name__ == '__main__':
    main()
