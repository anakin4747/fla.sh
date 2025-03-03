#!/bin/bash

translate () {

    IFS=":" read -r tense french <<< "$1"
    english=$(trans -b -no-auto fr:en "$french")
    echo "$tense:$french:$english:0"
}

export -f translate

parallel -j 100 translate
