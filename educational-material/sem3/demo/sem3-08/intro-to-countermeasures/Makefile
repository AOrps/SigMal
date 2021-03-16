SHELL=/bin/bash

.PHONY: all usage tw se clean deepc

all: usage

CC = gcc

# Prints Usage for Developers not familiar with the code
usage:
	@printf "Usage:\n"
	@printf "make se -> Compile signal-example to show how signals work\n   :-> ./signal-example\n"
	@printf "make tw -> Compile a tinyweb daemon and 'makes it interesting'\n   :-> ./tinywebd\n"


# Creates a tinywed daemon
tw: 
	@printf "Compiling tinyweb-daemon.c...\n"
	${CC} tinyweb-daemon.c -o tinywebd

	@echo "Giving root ownership of executable"
	sudo chown root ./tinywebd

	@echo "Making the user execute program from the permissions of the owner"
	sudo chmod u+s ./tinywebd


# Compiles the signal-example.c file to signal-example with gcc
se: 
	@printf "Compiling signal-example.c...\n"
	${CC} signal-example.c -o signal-example


# Checks if files are in the directory and if they are, they are removed.
clean:
ifneq (,$(wildcard ./signal-example))
	@echo "Removing signal-example..."
	@rm signal-example
endif

ifneq (,$(wildcard ./tinywebd))
	@echo "Removing tinywebd..."
	@rm tinywebd
endif

ifneq (, $(wildcard ./a.out))
	@echo "Removing any potential a.out..."
	@rm a.out
endif

#  deepc (DeepClean) -> Cleans all files that can be attached with the program and build
deepc: clean
	@echo "Removing tinywebd.log...."
	@sudo rm /var/log/tinywebd.log


