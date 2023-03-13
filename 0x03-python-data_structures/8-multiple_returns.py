#!/usr/bin/python3


def multiple_returns(sentence):
    n = len(sentence)
    return (n, sentence[0] if sentence is not None else None)
