#!/bin/bash

translate () {
    local french="$1"

    english=$(trans -b -no-auto fr:en "$french")
    echo "$french:$english" >> output.txt
}

# Export function so parallel can use it
export -f translate

# Run parallel with proper argument handling
parallel -j 8 translate ::: $(cat ./verbs_with_pronouns.txt)
