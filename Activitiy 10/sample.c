#include <stdio.h>
int main() {
    int n, i, t1 = 0, t2 = 1, nextTerm;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");

    for (i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }

    // Induced Errors:
    // 1. Compile-time error (Lexical Analysis): Missing semicolon at the end of the next line.
    printf("Compile-time error" // Missing semicolon

    // 2. Compile-time error (Syntax Analysis): Mismatched curly braces.
    // No closing brace for the main function.

    // 3. Runtime error (Zero Division): Division by zero.
    int x = 0;
    int y = 1 / x;

    // 4. Runtime error (Index Error): Accessing an out-of-bounds index.
    int arr[3] = {1, 2, 3};
    int value = arr[5]; // Accessing index 5, which is out of bounds.

    // 5. Logical error: Printing Fibonacci numbers without updating them correctly.
    // The Fibonacci series will not be generated correctly.
    int a = 0, b = 1, next;
    for (int j = 0; j < n; j++) {
        printf("%d, ", a);
        a = b;
        b = next;
    }

    return 0;
