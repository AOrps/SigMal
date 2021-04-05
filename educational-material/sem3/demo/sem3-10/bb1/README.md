# Baffling Buffer 1

The following is a walk-through of a problem taken from [MetaCTF](https://metactf.com/) CyberGames 2020. I have no idea how long their server will keep hosting this problem. No copyright infringement is intended.

## Problem

After pointing out the initial issue, the developers issued a new update on the login service and restarted it at `host1.metaproblems.com 5151`. Looking at the [binary](bb1) and [source code](bb1.c), you discovered that this code is still vulnerable.

## Solution

### Examining the Stack Layout

The C code is fairly simple. If the user enters `"Sup3rs3cr3tC0de"`, then `"Access granted!"` is printed. `"Invalid auth."` is supposed to be printed for any other inputs. This, however, is not the flag we are looking for. It appears from the code that if the function `win` were to somehow be executed, then the flag would be printed.

As the name suggests, the function `vuln` has a buffer overflow vulnerability due to it's use of the notoriously dangerous `gets`. We can get a better understanding of the stack layout by using GNU debugger.

```sh
chmod u+x bb1
gdb --quiet bb1
```

After executing `break vuln` and `run`, the program will run until it hits the breakpoint in `vuln`.

```txt
(gdb) break vuln
Breakpoint 1 at 0x401190
(gdb) run
Starting program: [redacted]

Breakpoint 1, 0x0000000000401190 in vuln ()
```

The output of `backtrace` shows where execution left off in each function. How do programs remember where each function left off? Every time `f` calls `g`, `f` pushes its "where I left off" address to the stack before jumping to `g`.

```txt
(gdb) backtrace
#0  0x0000000000401190 in vuln ()
#1  0x0000000000401238 in main ()
```

The output of `x/5i vuln` shows an assembler code dump of the first 5 instructions of `vuln` and also shows an arrow pointing at the next instruction to be executed. The next instruction `sub $0x30,%rsp` is for allocating 48 bytes on the stack for `char buf[48]`.

```txt
(gdb) x/5i vuln
   0x40118c <vuln>:     push   %rbp
   0x40118d <vuln+1>:   mov    %rsp,%rbp
=> 0x401190 <vuln+4>:   sub    $0x30,%rsp
   0x401194 <vuln+8>:   lea    0xe7b(%rip),%rdi        # 0x402016
   0x40119b <vuln+15>:  callq  0x401030 <puts@plt>
```

The output of `x/2a $rsp` shows two address-width (8 bytes each) values on the top of the stack. Since `push %rbp` was the most recent stack operation, the saved value of `%rpb` resides on the top of the stack. Next comes the address `0x401238` which is the same address we saw in `backtrace`.

```txt
(gdb) x/2a $rsp
0x7fffffffdba0: 0x7fffffffdbb0  0x401238 <main+74>
```

Using `print win` is one of **many** ways to obtain the address of `win`. The goal of our attack will be to overwrite the return address `0x401238` with `0x401172` so that control goes to `win` instead of back to `main`.

```txt
(gdb) print win
$1 = {<text variable, no debug info>} 0x401172 <win>
```

### Crafting the Attack String

We have located the region of memory that needs to be overwritten. A couple of considerations must be made for the attack string.

1. The string must start with the access code, otherwise `exit(-1)` will be executed and the attack will fail.
2. Memory addresses are 8 bytes, stored in little endian. This means the lowest bytes must be printed out first.

Here is a table that describes all of the contents of the attack string.

| #    | Bytes | Contents                              |
| :--- | :---- | :------------------------------------ |
| 1    | 16    | `"Sup3rs3cr3tC0de"`, ends with `NUL`  |
| 2    | 32    | Padding, any character sequence       |
| 3    | 8     | `0x00007fffffffde90` in little endian |
| 4    | 8     | `0x0000000000401172` in little endian |
| 5    | 1     | Line feed                             |

The string that needs to be typed in contains unprintable characters. Therefore, I created a small C program [`mal.c`](mal.c) that outputs the necessary string.

```sh
gcc mal.c -o mal
echo 'dummy flag' > flag.txt
./mal | ./bb1
```

This did not work locally on my machine. Running it with `gdb` told me that `flag.txt` did not exist. I suspect this is some kind of binary compatibility issue. However, this did work on the real problem server which is good enough.

```sh
./mal | nc host1.metaproblems.com 5151
```

```txt
Enter the access code:
Access granted!
MetaCTF{c_strings_are_the_best_strings}
```

The flag has been captured! I hope you enjoyed this demo.

:triangular_flag_on_post:
