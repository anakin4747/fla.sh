#!/usr/bin/python3

import sys

vowels = "aeiouyáéíóúàèìòùâêîôû"

tenses = {
    "présent",
    "passé composé",
    "aller + infinitif",
    "imparfait",
    "futur",
    "conditionnel",
    "subjonctif",
    "plus-que-parfait",
    "conditionnel passé",
    "subjonctif passé",
}

while tense := sys.stdin.readline().strip():

    tense_buffer = ""

    if tense in tenses:

        je = sys.stdin.readline().strip()
        if je[0] in vowels:
            je = "J'" + je
        else:
            je = "Je " + je

        tu = sys.stdin.readline().strip()
        if tu[0] in vowels:
            tu = "T'" + tu
        else:
            tu = "Tu " + tu

        il_elle_on = sys.stdin.readline().strip()
        il = "Il " + il_elle_on
        elle = "Elle " + il_elle_on
        on = "On " + il_elle_on

        nous = "Nous " + sys.stdin.readline().strip()
        vous = "Vous " + sys.stdin.readline().strip()

        ils_elles = sys.stdin.readline().strip()
        ils = "Ils " + ils_elles
        elles = "Elles " + ils_elles

        print(tense, je,    sep=':')
        print(tense, tu,    sep=':')
        print(tense, il,    sep=':')
        print(tense, elle,  sep=':')
        print(tense, on,    sep=':')
        print(tense, nous,  sep=':')
        print(tense, vous,  sep=':')
        print(tense, ils,   sep=':')
        print(tense, elles, sep=':')


    if tense == "impératif":
        tu = sys.stdin.readline().strip()
        if tu[0] in vowels:
            tu = "T'" + tu
        else:
            tu = "Tu " + tu

        nous = "Nous " + sys.stdin.readline().strip()
        vous = "Vous " + sys.stdin.readline().strip()

        print(tense, tu,   sep=':')
        print(tense, nous, sep=':')
        print(tense, vous, sep=':')



