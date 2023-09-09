#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

#define MAX_MATCHES 100

int main() {
    char *file_path = "test.c";  // Replace with the path to your C file

    // Regular expression patterns
    char *keyword_pattern = "\\bauto\\|break\\|case\\|char\\|const\\|continue\\|default\\|do\\|double\\|else\\|enum\\|extern\\|float\\|for\\|goto\\|if\\|int\\|long\\|register\\|return\\|short\\|signed\\|sizeof\\|static\\|struct\\|switch\\|typedef\\|union\\|unsigned\\|void\\|volatile\\|while\\|main\\|include\\|stdio\\|stdlib\\|printf\\b";
    
    // Initialize content buffer and read the C file
    char content[10000];  // Adjust the buffer size as needed

    // Read the C file and tokenize it
    FILE *fp = fopen(file_path, "r");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), fp)) {
        strcat(content, line);
    }

    fclose(fp);

    // Tokenize and print keywords
    regex_t regex;
    regmatch_t matches[MAX_MATCHES];
    int status;

    status = regcomp(&regex, keyword_pattern, REG_EXTENDED);
    if (status != 0) {
        perror("Error compiling keyword regex");
        return 1;
    }

    status = regexec(&regex, content, MAX_MATCHES, matches, 0);
    if (status == 0) {
        printf("Keywords:");
        for (int i = 0; i < MAX_MATCHES && matches[i].rm_so != -1; i++) {
            printf(" %.*s", (int)(matches[i].rm_eo - matches[i].rm_so), &content[matches[i].rm_so]);
        }
        printf("\n");
    }

    // Begin repeating the process for operators, variables, and special symbols here

    // Free resources
    regfree(&regex);

    return 0;
}
