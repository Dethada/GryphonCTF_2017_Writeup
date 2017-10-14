#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// (cat payload; cat -) | nc {} {}

int vuln() {
    // Declare main variables
    char command[64];

    // Get user's input
    puts("PLEASE STATE YOUR COMMAND.");
    printf("Your response? ");
    gets(command);
}

int main() {
    // Disable output buffering
    setbuf(stdout, NULL);

    // Greet and meet
    puts("HELLO. I AM SMARTBOT ALPHA 0.1.0.");
    vuln();

    // Deny user wishes immediately.
    puts("YOUR WISHES ARE DENIED.");
}
