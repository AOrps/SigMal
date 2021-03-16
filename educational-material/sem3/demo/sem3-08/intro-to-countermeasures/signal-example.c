#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

// Purpose meant to show how signals work

void signal_handler(int signal) {
    printf("Caught signal %d\t", signal);
    if (signal == SIGTSTP)
        printf("SIGTSTP (Ctrl-Z)");
    else if (signal == SIGWINCH)
        printf("Window size changed");

    printf("\n");
}

void sigint_handler(int x) {
    printf("Caught a Ctrl-C (SIGINT) in a separate handler\nExiting.\n");
    exit(0);
}

int main() {
    signal(SIGQUIT, signal_handler);
    signal(SIGWINCH, signal_handler);

    signal(SIGINT, sigint_handler);


    while(1) {}
}