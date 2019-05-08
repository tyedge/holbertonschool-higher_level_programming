#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        newtup = (len(sentence), sentence[0])
        length = newtup[0]
        first = newtup[1]
        return newtup
    else:
        newtup = (0, None)
        length = newtup[0]
        first = newtup[1]
        return newtup
