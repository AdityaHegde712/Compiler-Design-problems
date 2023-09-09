#include <stdio.h>
#include <string.h>

void process_line(const char *line) {
    char datatypes[10][3]; // Assuming a maximum of 10 format specifiers
    const char *meanings[] = {"Integer", "Float", "Character"};
    int end_index = -1; // Stores the index of the last occurrence of the line delimiter.
    
    // Loop to find datatypes
    int line_length = strlen(line);
    int datatypes_count = 0;

    for (int i = 0; i < line_length; i++) {
        if (line[i] == '%') {
            if (line[i + 1] == 'd') {
                strcpy(datatypes[datatypes_count], "%d");
                datatypes_count++;
            } else if (line[i + 1] == 'f') {
                strcpy(datatypes[datatypes_count], "%f");
                datatypes_count++;
            } else if (line[i + 1] == 'c') {
                strcpy(datatypes[datatypes_count], "%c");
                datatypes_count++;
            }
            end_index = i + 1;
        }
    }

    end_index += 3;

    // Find the start and end positions of the variables
    const char *vars_start = line + end_index;
    const char *vars_end = strchr(vars_start, ')');

    if (vars_end == NULL) {
        printf("Error: Missing closing parenthesis in the input string.\n");
        return;
    }

    // Print the variables
    printf("Order: ");
    for (const char *ptr = vars_start; ptr < vars_end; ptr++) {
        if (*ptr == ',') {
            printf(" ");
        } else {
            printf("%c", *ptr);
        }
    }
    printf("\n");

    // Final output:
    for (int i = 0; i < datatypes_count; i++) {
        printf("%s : %s\n", datatypes[i], meanings[i]);
    }

    printf("No. Of variables: %d\n", datatypes_count);
    printf("Format Specifiers: ");
    for (int i = 0; i < datatypes_count; i++) {
        printf("%s ", datatypes[i]);
    }
    printf("\n");
}

int main() {
    const char *line = "printf('variables are %d%f%c', v1, v2, v3)";
    process_line(line);
    return 0;
}
