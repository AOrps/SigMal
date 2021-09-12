# Semester 3 Slides

Tentative list of topics:

1. Introduction
2. [Linux, Processors](02.md)
3. [Signatures, Magic Numbers, Hashing](03.md)
4. [Bypassing Signature based IDS/IDPS](04.md)
5. [Hacky Sig•Mal Tings (yes Tings)](05.md)
6. [Assembly, Debugging](06.md)
7. [Shellcode](07.md)
8. [Defensive Countermeasures / (hello-world)s](08.md)
9. [Buffer Overflows](09.md), TOR Routing
10. [Sem 3 End / Speedrun Recap / CTF Walkthroughs](10.md)

## Building

* Git and GitHub are best suited for tracking plaintext files. Therefore, we are experimenting with a workflow that generates PowerPoints from Markdown using [Pandoc](https://pandoc.org/). To build all files, simply run [`build.sh`](build.sh).

* Another experimental process is [mdToThing](https://github.com/njitacm/mdToThing) which uses [marp-cli](https://github.com/marp-team/marp-cli) for generating `{ .pptx | .pdf | .html }` files from `{ .md }` and will also have a custom CSS template.

## How to Contribute

* `<TEMPORARY THIS SHOULD EVENTUALLY BE DELETED>`

1. `cp template.md foo.md`
2. Push changes
3. Optional: Run mdToThing scripts on `foo.md` file to test compatibility
