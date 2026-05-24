#Print the middle character(s) of a string. 
#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int len, mid;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove newline character if present
    str[strcspn(str, "\n")] = '\0';

    len = strlen(str);

    if (len % 2 == 0) {
        // Even length → print two middle characters
        mid = len / 2;
        printf("Middle characters: %c%c\n", str[mid - 1], str[mid]);
    } else {
        // Odd length → print one middle character
        mid = len / 2;
        printf("Middle character: %c\n", str[mid]);
    }

    return 0;
}
