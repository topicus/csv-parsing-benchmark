#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * This parser doesn't handle all the csv
 * dialects and should not be considered as
 * a real benchmark. It was created to
 * get a rough performance estimation.
 */
int main()
{
    FILE* stream = fopen("test.csv", "r");
    char *token;
    const char s[2] = ",";

    char line[1024];
    while (fgets(line, 1024, stream))
    {
        char* tmp = strdup(line);
        token = strtok(line, s);
        while( token != NULL )
        {
          token = strtok(NULL, s);
        }
        free(tmp);
    }
}