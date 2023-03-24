#!/usr/bin/env python3

from sys import argv
from argparse import ArgumentParser

ALPHABET = "abcdefgijklmnopqrstuvwxyz"

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
}

CODE_REVERSED = {value:key for key,value in CODE.items()}


def to_morse(str_param):
    return ' '.join(CODE.get(i.upper()) if i in ALPHABET else CODE.get(i) for i in str_param)


def from_morse(str_param):
    return ''.join(CODE_REVERSED.get(i) for i in str_param.split())


def main():
    ap = ArgumentParser(prog="PyMorse",
        description="Python morse code and decode")

    ap.add_argument('-c' ,'--code', help="to code morse")
    ap.add_argument('-d' ,'--decode', help="to decode morse")

    args = ap.parse_args()

    if len(argv) > 2:
        if str_param:=args.code:
            output = to_morse(str_param)
            print(output)
        elif str_param:=args.decode:
            output = from_morse(str_param)
            print(output)
        else:
            ap.print_help()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
