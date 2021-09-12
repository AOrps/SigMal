# Intro to Countermeasures Demo

* **This demo uses a little make and makefile** 
    * Dw if you aren't experienced with it
    * I wrote it like a heathen for ease of use :) 
    <!-- Like I don't think this is how you are supposed to write it or best practices but lolz-->

## Purpose
* To demonstrate how system daemons work and how to exploit this!


## Demo Usage
* This assumes that you are ning all these commands from within the directory.

### Signal Example
* `make se`
    * This will compile the signal-example.c to signal-example

### Signal List
* `./signals.sh`
    * `Sit in awe`
    * This runs list of signals that can be generated on 

### Tinyweb Daemon
* `make tw`
    * This will compile tinyweb-daemon.c to tinywebd
    * It will also give root ownership of the file
    * It also executes the command as the owner as opposed to the user

### Process tinywebd
* `ps ax | grep tinywebd `
    * To check process
* `kill -9 <PID>` || `kill <PID>`
    * To signal a terminate signal to the system daemon
* `kill $(ps ax | grep tinywebd | awk '{print $1}' | python3 -c 'pid=input(); print(pid)')`
    * Will kill your first instance of tinywebd from it's PID
    * If it returns with 'bash: kill (SOME NUMBER) - No such process' ~ No tinywebd existed


### Make request to the system daemon
* `python3 -c 'import requests; requests.get("https://127.0.0.1:80")'`
    * This creates a get request to the system daemon that is running at localhost on Port 80

### Logs
* `sudo cat /var/log/tinywebd.log`
    * Since it is a system daemon, it doesn't have a terminal process attached with it and it writes to log files.
    * This will `cat` the contents of the log file of the tinyweb-daemon

### "Clean up" (Remove binaries)
* `make clean`
    * Removes Binaries
* `make deepc`
    * Remove Binaries and Log Files

## Step to Exploiting tinywebd

1. (If available) Analyze source code (Debuggers help with getting a deeper dive into the code and how it functions) 
1. Do a informed guess / conjecture of  vulnerability based on the state of the source code.
1. Write a script that will exploit the program
1. Optimize exploitation script

### For tinywebd

1. Figure out the offset between the request buffer and stored return address.
1. Overflow shellcode into the return address.
    - A helpful trick is to use a NOP sled and use that as the "landing" for the shellcode
1. Open shell with shellcode to run as root
1. Pwn and Take over the System

