#!/usr/bin/python3
def multiple_returns(sentence):
    return ((len(sentence), None) if not sentence else (len(sentence), sentence[0]))
