# ඞ Binaries (Hello)

## Purpose 
* Looking at the executables of different programming languages

## Goal
* To determine how different the size of different `Hello\n` executables.

* **Note that, not all languages are written the same or for the same purpose so take the following with hefty amounts of salt. I thought it would be interesting to look at and really help me make up my mind about picking a dope language to master.**

---

## Chaos in Python
* It single-handedly language percentage of the SigMal repo

![](https://github.com/AOrps/SigMal/blob/master/educational-material/sem3/img/python_bruh.png)


* Zig also had a lot for one file compilation, but python really stepped it up!

---

## "Base Case"
* All programs need to print out "Hello" and then a newline char

* All programs ~_need_ to be compiled on the same architecture / same OS.
	* Test files are compiled on 64-bit architecture and for MacOSX

* Since this is a simple code, it should be all on one file.

---

## Result 

| Language | Result | 'Programming' :: or 'Scripting' Language
| :--: | :--- | :---
| Assembly | `32,944 bytes (37 KB on disk)` | Programming 
| Bash | ---- | Scripting
| C | `49,424 bytes (53 KB on disk)` | Programming
| C++ | `55,960 bytes (57 KB on disk)` | Programming
| C# | ~`3,072 bytes (4 KB on disk)` | Programming
| Golang | `2,146,968 bytes (2.2 MB on disk)` | Programming
| Haskell | `1,341,808 bytes (1.3 MB on disk)` | Programming
| Java | ~`409 bytes (4 KB on disk)` (.class) | Programming
| JavaScript | ---- | Scripting
| Lisp | ---- | Scripting
| python3 | `6,123,419 bytes (6.1 MB on disk)` | Scripting
| Rust | `344,320 bytes (348 KB on disk)` | Programming
| TypeScript | ---- | Scripting
| Zig | `453,240 bytes (455 KB on disk)` | Programming

---

## Considerations
* NB: `'Programming' or 'Scripting' Language` should be taken with a grain of salt. There can be many arguments whether they are valid.

* NB: This is very incomplete list of programming languages. And it only looks at the executable not everything that that comes along with the executable.

* C# compiles to .exe as opposed to a ELF or Mach-O executable bc Microsoft!
* Java compile to .class file because it is really the worst.

* MacOSX 11 (Big Sur) made it really difficult to use ld so, Assembly was linked and compiled with Gcc

* People don't really use rustc to compile a .rs file, they use the CHAD cargo and that makes it OP and really efficient and nice for certain projects.

* Java needs it's ~~dumb~~ Virtual Machine to work. (jvm)
<!-- AOrps does not like Java -->

* Some languages have features baked into them, like Safety (Rust / Zig) or being bad. ~~*cough cough* Java~~

* Some languages are dynamically linked while others are statically compiled. 

* Some languages have Type inference while others are statically typed. There are even varying levels of being statically typed.

* How difficult is it to work with?

* Community support? 

* What about dependencies? How difficult is it to add or work with external code. 

* Some languages just suck. ~~Like Java~~

* There are so many other things other considerations but note do your own research into it the topic if you are interested about a trying out a new language.
