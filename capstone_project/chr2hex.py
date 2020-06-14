import re

alphanum2hex = {'a': "61",
           'b': "62",
           'c': "63",
           'd': "64",
           'e': "65",
           'f': "66",
           'g': "67",
           'h': "68",
           'i': "69",
           'j': "6A",
           'k': "6B",
           "l": "6C",
           "m": "6D",
           "n": "6E",
           "o": "6F",
           "p": "70",
           "q": "71",
           "r": "72",
           "s": "73",
           "t": "74",
           "u": "75",
           "v": "76",
           "w": "77",
           "x": "78",
           "y": "79",
           "z": "7A",
           "A": "41",
           "B": "42",
           "C": "43",
           "D": "44",
           "E": "45",
           "F": "46",
           "G": "47",
           "H": "48",
           "I": "49",
           "J": "4A",
           "K": "4B",
           "L": "4C",
           "M": "4D",
           "N": "4E",
           "O": "4F",
           "P": "50",
           "Q": "51",
           "R": "52",
           "S": "53",
           "T": "54",
           "U": "55",
           "V": "56",
           "W": "57",
           "X": "58",
           "Y": "59",
                "Z": "5A",
                "0": "30",
                "1": "31",
                "2": "32",
                "3": "33",
                "4": "34",
                "5": "35",
                "6": "36",
                "7": "37",
                "8": "38",
                "9": "39"
                }


def encode(string):
    if not re.match('^[a-zA-Z0-9]+$', string):
        return "String must be alpha-numeric only (uppercase, lowercase letters and numbers)"
    s = []
    for char in string:
        s.append(alphanum2hex[char])
    return "".join(s)


def decode(string):
    if not re.match('^[a-zA-Z0-9]+$', string):
        return "String must be alpha-numeric only (uppercase, lowercase letters and numbers)"
    s = []
    decode_list = [string[i:i + 2] for i in range(0, len(string), 2)]
    for pair in decode_list:
        for k, v in alphanum2hex.items():
            if pair == v:
                s.append(k)
    return "".join(s)
