#!/usr/bin/env bash

for i in {01..10}; do
    infile=$i.md
    outfile=$i.pptx

    if [ -f $infile ]; then
        if [ $infile -nt $outfile ]; then
            echo "Converting $infile to $outfile..."
            pandoc --from gfm --to pptx --output $outfile --slide-level 2 $infile
        else
            echo "$outfile is up to date"
        fi
    fi
done
