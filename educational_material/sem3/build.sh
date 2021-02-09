#!/usr/bin/env bash

for i in {01..10}; do
    infile=$i.md
    outfile=$i.pptx

    if [ -f $infile ]; then  # XX.md exists and is a file
        if [ $infile -nt $outfile ]; then  # XX.md is newer than XX.pptx
            echo "Converting $infile to $outfile..."
            pandoc --from gfm --to pptx --output $outfile --slide-level 2 $infile
        else
            echo "$outfile is up to date"
        fi
    fi
done
