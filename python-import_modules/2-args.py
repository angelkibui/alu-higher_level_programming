#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    length = len(argv)

    print(f"{length} argument{'s' if length != 1 else ''}{'.' if length == 0 else ':'}")

    for i in range(length):
        print(f"{i + 1}: {argv[i]}")
